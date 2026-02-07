#!/usr/bin/env python3
"""
TTLocalizerEnglish.py String Replacer
=====================================

Reads TTLocalizerEnglish.py, identifies "safe" string literals (UI text, dialogue,
NPC names, zone names, quest text, etc.) and replaces them with lines drawn from
a user-supplied text file — while NEVER touching strings that the game engine
depends on (font paths, model paths, phase file references, DNA references,
format-string placeholders, template tokens, import lines, etc.).

Usage:
    python tt_string_replacer.py <TTLocalizerEnglish.py> <replacement_lines.txt> [-o OUTPUT]

The replacement text file should have one replacement string per line.
Lines are drawn sequentially (cycling if the file runs out).

A dry-run mode (--dry-run) will print stats without writing anything.
"""

import ast
import re
import sys
import argparse
import random
from pathlib import Path
from typing import List, Tuple, Set

# ─────────────────────────────────────────────────────────────────────
#  PROTECTION RULES — strings matching ANY of these are left alone
# ─────────────────────────────────────────────────────────────────────

# 1. File paths / asset references
PATH_PATTERNS = [
    re.compile(r'phase_\d+/'),           # phase_3/models/fonts/...
    re.compile(r'\.ttf', re.I),          # font files
    re.compile(r'\.bam', re.I),          # Panda3D binary model
    re.compile(r'\.egg', re.I),          # Panda3D egg model
    re.compile(r'\.ogg', re.I),          # audio
    re.compile(r'\.wav', re.I),          # audio
    re.compile(r'\.mid', re.I),          # midi
    re.compile(r'\.mp3', re.I),          # audio
    re.compile(r'\.jpg', re.I),          # texture
    re.compile(r'\.png', re.I),          # texture
    re.compile(r'\.rgb', re.I),          # texture
    re.compile(r'\.rgba', re.I),         # texture
    re.compile(r'\.txo', re.I),          # panda texture
    re.compile(r'\.dna', re.I),          # DNA scene files
    re.compile(r'\.bdna', re.I),         # binary DNA
    re.compile(r'\.prc', re.I),          # Panda config
    re.compile(r'models/'),              # model path fragment
    re.compile(r'fonts/'),               # font path fragment
    re.compile(r'maps/'),                # texture map fragment
    re.compile(r'audio/'),               # audio path fragment
]

# 2. Format-string / template placeholders that the engine substitutes at runtime
TEMPLATE_PATTERNS = [
    re.compile(r'%[sd]'),                # printf-style %s, %d
    re.compile(r'%\(.+?\)[sd]'),         # %(name)s style
    re.compile(r'_toNpcName_'),          # NPC name token
    re.compile(r'_where_'),              # location token
    re.compile(r'_avName_'),             # avatar name token
    re.compile(r'_linebreak_'),          # linebreak token
    re.compile(r'\x01.*?\x02'),          # Panda3D text formatting \x01...\x02
]

# 3. Variable names that are known to hold engine-critical values
#    (the variable NAME on the left side of =, meaning we protect entire lines)
PROTECTED_VARIABLE_NAMES: Set[str] = {
    # Font paths
    'InterfaceFont', 'ToonFont', 'SuitFont', 'SignFont', 'MinnieFont',
    'FancyFont', 'BuildingNametagFont', 'BuildingNametagShadow',
    'NametagFonts', 'NametagFontNames',
    # Any Shadow tuples
    'InterfaceFontShadow', 'ToonFontShadow', 'SuitFontShadow',
    'SignFontShadow', 'MinnieFontShadow', 'FancyFontShadow',
    # Import / code plumbing
    'commitmantst',
}

# 4. Line-level patterns — entire lines matching these are never touched
PROTECTED_LINE_PATTERNS = [
    re.compile(r'^\s*(from|import)\s'),                # import statements
    re.compile(r'^\s*#'),                               # comments
    re.compile(r'^\s*OL\.'),                            # OTPLocalizer plumbing
    re.compile(r'GlobalStreetNames'),                   # references dict lookups
    re.compile(r'CatalogAccessoryItemGlobals'),         # catalog imports
    re.compile(r'accessoryStyleDescription'),           # accessory style dict
    re.compile(r'AccessoryNamePrefix'),                 # accessory name prefix dict
    re.compile(r'AwardManagerAccessoryNames'),          # award manager lookups
    re.compile(r'accessoryInfo'),                       # accessory info lookups
    re.compile(r'^\s*for\s+'),                          # for loops (plumbing)
    re.compile(r'^\s*(if|elif|else)\s'),                # conditionals
    re.compile(r'^\s*def\s'),                           # function defs
    re.compile(r'^\s*class\s'),                         # class defs
    re.compile(r'^\s*checkLanguage'),                   # language check
    re.compile(r'^\s*try\s*:'),                         # try blocks
    re.compile(r'^\s*except\s'),                        # except blocks
    re.compile(r'^\s*assert\s'),                        # assertions
    re.compile(r'^\s*print\s'),                         # print statements (debug/plumbing)
    re.compile(r'^\s*return\s'),                        # return statements
    re.compile(r'^\s*raise\s'),                         # raise statements
    re.compile(r'\blen\s*\('),                          # len() calls — plumbing
    re.compile(r'\brange\s*\('),                        # range() calls — plumbing
    re.compile(r'\bappend\s*\('),                       # .append() — building lists
    re.compile(r'\bupdate\s*\('),                       # .update() — dict merging
    re.compile(r'\bdict\s*\('),                         # dict() calls
    re.compile(r'\bcopy\s*\('),                         # .copy() calls
    re.compile(r'\biterkeys\s*\('),                     # .iterkeys() — py2 dict iteration
    re.compile(r'\bitems\s*\('),                        # .items() — dict iteration
]

# 5. Strings that are too short to be meaningful UI text (likely keys/codes)
#    Raised to 5 to catch accessory IDs like 'hbb1', 'srt2', DNA codes, etc.
MIN_MEANINGFUL_LENGTH = 5

# 6. Strings that look like pure numeric / hex / identifier codes / coded keys
CODE_PATTERNS = [
    re.compile(r'^[\d.]+$'),             # purely numeric "1234", "3.14"
    re.compile(r'^0x[0-9a-fA-F]+$'),     # hex
    re.compile(r'^[A-Z_]+$'),            # ALL_CAPS_CONSTANT
    re.compile(r'^\w+\.\w+'),            # module.attribute references
    re.compile(r'^[a-z]{1,4}\d+$'),      # coded keys: hbb1, srt2, gls3, shw1, etc.
    re.compile(r'^[a-zA-Z]\w{0,5}$'),    # very short alphanumeric tokens (<=6 chars, single word, no spaces)
]

# 7. URL patterns — don't replace URLs
URL_PATTERN = re.compile(r'https?://')

# 8. Color / shadow tuples (None, (r,g,b,a), etc)
TUPLE_PATTERN = re.compile(r'^\s*\([\d., ]+\)\s*$')

# 9. Strings used as dictionary keys — the string appears inside [] brackets
#    e.g. someDict['hbb1'] or accessoryStyleDescription['striped']
DICT_KEY_CONTEXT_RE = re.compile(r'\[\s*[\'"]')

# 10. Strings that contain no spaces and no punctuation — likely identifiers/codes
#     (real UI text almost always has spaces or sentence-like structure)
NO_SPACE_SHORT_RE = re.compile(r'^[^\s]{1,15}$')  # up to 15 chars, no whitespace

# ─────────────────────────────────────────────────────────────────────
#  DETECTION HELPERS
# ─────────────────────────────────────────────────────────────────────

def is_protected_string(s: str) -> bool:
    """Return True if this string value must NOT be replaced."""
    stripped = s.strip()

    # Empty or trivially short
    if len(stripped) < MIN_MEANINGFUL_LENGTH:
        return True

    # File path / asset reference
    for pat in PATH_PATTERNS:
        if pat.search(s):
            return True

    # Pure code / identifier
    for pat in CODE_PATTERNS:
        if pat.match(stripped):
            return True

    # URL
    if URL_PATTERN.search(s):
        return True

    # Tuple-looking
    if TUPLE_PATTERN.match(s):
        return True

    # No spaces AND short — almost certainly a code/key, not UI text
    # Real UI text like "Cog Gallery" has spaces; codes like "striped" don't
    if NO_SPACE_SHORT_RE.match(stripped) and ' ' not in stripped:
        return True

    return False


def string_has_templates(s: str) -> bool:
    """Return True if the string contains format tokens that must be preserved."""
    for pat in TEMPLATE_PATTERNS:
        if pat.search(s):
            return True
    return False


def is_protected_line(line: str) -> bool:
    """Return True if the entire line should be skipped."""
    for pat in PROTECTED_LINE_PATTERNS:
        if pat.search(line):
            return True
    return False


def is_protected_variable(line: str) -> bool:
    """Return True if the line assigns to a protected variable name."""
    # Match "VarName = ..." at the start of a line
    m = re.match(r'^\s*(\w+)\s*=', line)
    if m and m.group(1) in PROTECTED_VARIABLE_NAMES:
        return True
    return False


# ─────────────────────────────────────────────────────────────────────
#  STRING FINDER — finds quoted string literals on a line
# ─────────────────────────────────────────────────────────────────────

# Matches single-quoted or double-quoted strings, handling escaped quotes.
# This is intentionally simple and doesn't handle triple-quotes or multiline,
# but TTLocalizerEnglish.py uses almost exclusively single-line strings.
STRING_LITERAL_RE = re.compile(
    r"""(?P<quote>['"])"""          # opening quote
    r"""(?P<body>(?:\\.|(?!(?P=quote)).)*?)"""  # body (with escapes)
    r"""(?P=quote)""",             # closing quote
    re.DOTALL
)


def find_replaceable_strings(line: str) -> List[Tuple[int, int, str, str]]:
    """
    Find all string literals in a line that are safe to replace.
    Returns list of (start, end, original_match, inner_text).
    """
    results = []

    # If the line contains dict-key bracket access with string keys, skip the whole line.
    # This catches patterns like: someDict['key'], foo['bar'], x['hbb1']
    # where strings are being used as lookup keys, not display text.
    if DICT_KEY_CONTEXT_RE.search(line):
        # But only skip if the line doesn't also contain obvious display text
        # (long strings with spaces are probably mixed — still skip to be safe)
        return results

    for m in STRING_LITERAL_RE.finditer(line):
        full_match = m.group(0)   # includes quotes
        inner = m.group('body')   # just the content

        if is_protected_string(inner):
            continue
        if string_has_templates(inner):
            continue

        results.append((m.start(), m.end(), full_match, inner))

    return results


# ─────────────────────────────────────────────────────────────────────
#  REPLACEMENT ENGINE
# ─────────────────────────────────────────────────────────────────────

def escape_for_python_string(s: str, quote_char: str) -> str:
    """Escape a replacement string so it's valid inside Python quotes."""
    s = s.replace('\\', '\\\\')
    s = s.replace(quote_char, '\\' + quote_char)
    # Preserve bell characters (\a / \x07) if the original had them
    return s


def process_file(
    input_path: str,
    replacements: List[str],
    output_path: str,
    shuffle: bool = False,
    dry_run: bool = False,
    verbose: bool = False,
):
    """
    Read TTLocalizerEnglish.py, replace safe strings, write output.
    """
    input_text = Path(input_path).read_text(encoding='utf-8', errors='replace')
    lines = input_text.splitlines(keepends=True)

    if shuffle:
        random.shuffle(replacements)

    rep_index = 0
    total_replaced = 0
    total_protected = 0
    total_lines_skipped = 0

    output_lines = []

    for line_no, line in enumerate(lines, 1):
        # Check line-level protections first
        if is_protected_line(line) or is_protected_variable(line):
            output_lines.append(line)
            total_lines_skipped += 1
            continue

        # Find all replaceable string literals on this line
        matches = find_replaceable_strings(line)

        if not matches:
            output_lines.append(line)
            continue

        # Replace from right to left so indices stay valid
        new_line = line
        for start, end, original, inner in reversed(matches):
            quote_char = original[0]  # ' or "

            # Get next replacement text
            if rep_index < len(replacements):
                rep_text = replacements[rep_index]
                rep_index += 1
            else:
                # Cycle back to start
                rep_index = 0
                rep_text = replacements[rep_index]
                rep_index += 1

            escaped = escape_for_python_string(rep_text.strip(), quote_char)
            new_string = f'{quote_char}{escaped}{quote_char}'

            new_line = new_line[:start] + new_string + new_line[end:]
            total_replaced += 1

            if verbose:
                print(f"  L{line_no}: {inner[:60]!r}  →  {rep_text[:60]!r}")

        output_lines.append(new_line)

    # Count protected strings (for stats)
    for line in lines:
        if not is_protected_line(line) and not is_protected_variable(line):
            for m in STRING_LITERAL_RE.finditer(line):
                inner = m.group('body')
                if is_protected_string(inner) or string_has_templates(inner):
                    total_protected += 1

    # Report
    print(f"\n{'=' * 60}")
    print(f"  TTLocalizerEnglish String Replacer — Summary")
    print(f"{'=' * 60}")
    print(f"  Input:              {input_path}")
    print(f"  Replacement file:   {len(replacements)} lines loaded")
    print(f"  Strings replaced:   {total_replaced}")
    print(f"  Strings protected:  {total_protected}")
    print(f"  Lines skipped:      {total_lines_skipped}")
    print(f"{'=' * 60}\n")

    if dry_run:
        print("  [DRY RUN] No file written.")
        return

    output = ''.join(output_lines)
    Path(output_path).write_text(output, encoding='utf-8')
    print(f"  Output written to: {output_path}")


# ─────────────────────────────────────────────────────────────────────
#  CLI
# ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Replace safe UI/dialogue strings in TTLocalizerEnglish.py "
                    "with lines from a text file, while protecting game-critical "
                    "strings (fonts, models, paths, format tokens, etc.)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic replacement
  python tt_string_replacer.py TTLocalizerEnglish.py funny_lines.txt

  # Dry run to see what would change
  python tt_string_replacer.py TTLocalizerEnglish.py funny_lines.txt --dry-run -v

  # Shuffle replacement order and write to specific output
  python tt_string_replacer.py TTLocalizerEnglish.py lines.txt -o Modified.py --shuffle

Protected string categories (NEVER replaced):
  • Font paths          (phase_3/models/fonts/...)
  • Model paths         (*.bam, *.egg, phase_*/...)
  • Texture paths       (*.jpg, *.png, *.rgb, maps/...)
  • Audio paths         (*.ogg, *.wav, *.mid, audio/...)
  • DNA / scene files   (*.dna, *.bdna)
  • Config files        (*.prc)
  • Format tokens       (%s, %d, %(name)s)
  • Template variables  (_toNpcName_, _where_, _avName_)
  • Panda3D formatting  (\\x01...\\x02 blocks)
  • Import statements   (from ... import ...)
  • URLs                (https://...)
  • Short strings       (< 4 chars — likely keys/flags)
  • ALL_CAPS constants  (likely enum/constant identifiers)
  • OTPLocalizer lines  (OL.SpeedChat... plumbing)
  • Protected vars      (InterfaceFont, ToonFont, SuitFont, etc.)
        """,
    )
    parser.add_argument('input', help='Path to TTLocalizerEnglish.py')
    parser.add_argument('replacements', help='Path to text file with replacement strings (one per line)')
    parser.add_argument('-o', '--output', default=None,
                        help='Output file path (default: <input>_modified.py)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show stats without writing output')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Print each replacement made')
    parser.add_argument('--shuffle', action='store_true',
                        help='Shuffle replacement lines randomly before applying')
    parser.add_argument('--seed', type=int, default=None,
                        help='Random seed for --shuffle (for reproducibility)')

    args = parser.parse_args()

    # Load replacement lines
    rep_path = Path(args.replacements)
    if not rep_path.exists():
        print(f"Error: Replacement file not found: {rep_path}")
        sys.exit(1)

    replacements = [
        line for line in rep_path.read_text(encoding='utf-8').splitlines()
        if line.strip()  # skip blank lines
    ]

    if not replacements:
        print("Error: Replacement file is empty (no non-blank lines).")
        sys.exit(1)

    # Determine output path
    if args.output:
        output_path = args.output
    else:
        inp = Path(args.input)
        output_path = str(inp.parent / f"{inp.stem}_modified{inp.suffix}")

    if args.seed is not None:
        random.seed(args.seed)

    process_file(
        input_path=args.input,
        replacements=replacements,
        output_path=output_path,
        shuffle=args.shuffle,
        dry_run=args.dry_run,
        verbose=args.verbose,
    )


if __name__ == '__main__':
    main()