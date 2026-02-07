import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pydub import AudioSegment

# Check if pydub can find ffmpeg immediately
try:
    AudioSegment.converter_which("ffmpeg")
except Exception:
    print("WARNING: FFMPEG not found. Audio conversion might fail.")

class AudioScramblerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Scrambler (Chaos Edition)")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.theme_use('clam')

        # Variables
        self.target_dir = tk.StringVar()
        self.source_dir = tk.StringVar()
        self.status_var = tk.StringVar(value="Waiting for mayhem...")
        
        # Counters
        self.target_count_var = tk.StringVar(value="No folder selected")
        self.source_count_var = tk.StringVar(value="No folder selected")

        # --- UI Layout ---

        # 1. Target Folder
        lbl_target = ttk.Label(root, text="1. Target Game Folder (phase_x/audio):", font=("Arial", 10, "bold"))
        lbl_target.pack(pady=(15, 5), anchor="w", padx=20)
        
        frame_target = ttk.Frame(root)
        frame_target.pack(fill="x", padx=20)
        entry_target = ttk.Entry(frame_target, textvariable=self.target_dir)
        entry_target.pack(side="left", fill="x", expand=True, padx=(0, 10))
        btn_target = ttk.Button(frame_target, text="Browse", command=self.select_target)
        btn_target.pack(side="right")
        
        lbl_target_stats = ttk.Label(root, textvariable=self.target_count_var, font=("Arial", 8), foreground="gray")
        lbl_target_stats.pack(anchor="w", padx=20)

        # 2. Source Folder
        lbl_source = ttk.Label(root, text="2. Replacement Sounds Folder:", font=("Arial", 10, "bold"))
        lbl_source.pack(pady=(15, 5), anchor="w", padx=20)
        
        frame_source = ttk.Frame(root)
        frame_source.pack(fill="x", padx=20)
        entry_source = ttk.Entry(frame_source, textvariable=self.source_dir)
        entry_source.pack(side="left", fill="x", expand=True, padx=(0, 10))
        btn_source = ttk.Button(frame_source, text="Browse", command=self.select_source)
        btn_source.pack(side="right")

        lbl_source_stats = ttk.Label(root, textvariable=self.source_count_var, font=("Arial", 8), foreground="gray")
        lbl_source_stats.pack(anchor="w", padx=20)

        # 3. Options
        frame_opts = ttk.Frame(root)
        frame_opts.pack(fill="x", padx=20, pady=10)
        
        self.normalize_var = tk.BooleanVar(value=True)
        chk_norm = ttk.Checkbutton(frame_opts, text="Normalize Volume (Prevent ear explosion)", variable=self.normalize_var)
        chk_norm.pack(side="left")

        # Progress
        self.progress = ttk.Progressbar(root, orient="horizontal", length=100, mode="determinate")
        self.progress.pack(fill="x", padx=20, pady=(20, 5))
        
        self.lbl_status = ttk.Label(root, textvariable=self.status_var, font=("Arial", 9, "bold"))
        self.lbl_status.pack(pady=5)

        # Run
        btn_run = ttk.Button(root, text="SCRAMBLE AUDIO", command=self.run_scramble)
        btn_run.pack(fill="x", padx=50, pady=20)

    def scan_folder(self, folder, extensions):
        files_found = []
        for root, _, files in os.walk(folder):
            for file in files:
                if os.path.splitext(file)[1].lower() in extensions:
                    files_found.append(os.path.join(root, file))
        return files_found

    def select_target(self):
        folder = filedialog.askdirectory(title="Select Game Audio Folder")
        if folder:
            self.target_dir.set(folder)
            found = self.scan_folder(folder, {'.ogg', '.mp3', '.wav'})
            self.target_count_var.set(f"Found {len(found)} game sounds.")

    def select_source(self):
        folder = filedialog.askdirectory(title="Select Meme Sounds Folder")
        if folder:
            self.source_dir.set(folder)
            found = self.scan_folder(folder, {'.ogg', '.mp3', '.wav', '.flac', '.m4a'})
            self.source_count_var.set(f"Found {len(found)} replacement sounds.")

    def run_scramble(self):
        target_path = self.target_dir.get()
        source_path = self.source_dir.get()

        if not target_path or not source_path:
            messagebox.showerror("Error", "Please select both folders.")
            return

        # 1. Get Lists
        replacements = self.scan_folder(source_path, {'.ogg', '.mp3', '.wav', '.flac', '.m4a'})
        targets = self.scan_folder(target_path, {'.ogg', '.mp3', '.wav'})

        if not replacements:
            messagebox.showerror("Error", "No audio files found in source folder!")
            return
        if not targets:
            messagebox.showerror("Error", "No audio files found in target folder!")
            return

        # 2. Process
        total_files = len(targets)
        self.progress["maximum"] = total_files
        success_count = 0
        
        self.status_var.set(f"Converting and Scrambling {total_files} files...")
        self.root.update()

        for i, target_file in enumerate(targets):
            try:
                # A. Identify Target Format (game engine expects this)
                target_ext = os.path.splitext(target_file)[1].lower().replace('.', '') # e.g., 'ogg'
                
                # B. Pick Random Source
                random_source = random.choice(replacements)

                # C. Load and Convert
                sound = AudioSegment.from_file(random_source)
                
                # Optional: Normalize Volume (Toontown audio is usually quiet, memes are loud)
                if self.normalize_var.get():
                    change_in_dBFS = -20.0 - sound.dBFS
                    sound = sound.apply_gain(change_in_dBFS)

                # D. Export over the target
                # We force the format to match the target extension so the game doesn't crash
                sound.export(target_file, format=target_ext)
                
                success_count += 1

            except Exception as e:
                print(f"Failed to replace {target_file}: {e}")

            if i % 2 == 0: # Update UI
                self.progress["value"] = i + 1
                self.root.update()

        self.progress["value"] = total_files
        self.status_var.set(f"Done! Ruined {success_count} sounds.")
        messagebox.showinfo("Success", f"Ears will bleed.\nReplaced {success_count} files.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioScramblerApp(root)
    root.mainloop()