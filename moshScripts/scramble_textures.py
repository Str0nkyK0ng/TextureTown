import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image

class TextureScramblerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Texture Scrambler")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        # Style
        style = ttk.Style()
        style.theme_use('clam')

        # Variables
        self.target_dir = tk.StringVar()
        self.source_dir = tk.StringVar()
        self.status_var = tk.StringVar(value="Ready")

        # --- UI Layout ---
        
        # Target Folder Section (The Game Phase Folder)
        lbl_target = ttk.Label(root, text="1. Select Target Folder (e.g., phase_3.5):", font=("Arial", 10, "bold"))
        lbl_target.pack(pady=(15, 5), anchor="w", padx=20)
        
        frame_target = ttk.Frame(root)
        frame_target.pack(fill="x", padx=20)
        entry_target = ttk.Entry(frame_target, textvariable=self.target_dir)
        entry_target.pack(side="left", fill="x", expand=True, padx=(0, 10))
        btn_target = ttk.Button(frame_target, text="Browse", command=self.select_target)
        btn_target.pack(side="right")

        # Source Folder Section (Your Random Images)
        lbl_source = ttk.Label(root, text="2. Select Replacement Images Folder:", font=("Arial", 10, "bold"))
        lbl_source.pack(pady=(15, 5), anchor="w", padx=20)
        
        frame_source = ttk.Frame(root)
        frame_source.pack(fill="x", padx=20)
        entry_source = ttk.Entry(frame_source, textvariable=self.source_dir)
        entry_source.pack(side="left", fill="x", expand=True, padx=(0, 10))
        btn_source = ttk.Button(frame_source, text="Browse", command=self.select_source)
        btn_source.pack(side="right")

        # Progress Bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=100, mode="determinate")
        self.progress.pack(fill="x", padx=20, pady=(30, 5))
        
        self.lbl_status = ttk.Label(root, textvariable=self.status_var, font=("Arial", 9))
        self.lbl_status.pack(pady=5)

        # Run Button
        btn_run = ttk.Button(root, text="SCRAMBLE TEXTURES", command=self.run_scramble)
        btn_run.pack(fill="x", padx=50, pady=20)

    def select_target(self):
        folder = filedialog.askdirectory(title="Select Folder to Modify")
        if folder:
            self.target_dir.set(folder)

    def select_source(self):
        folder = filedialog.askdirectory(title="Select Folder with Random Images")
        if folder:
            self.source_dir.set(folder)

    def get_all_images(self, folder, extensions={'.jpg', '.jpeg', '.png'}):
        """Recursively finds all valid images in a folder."""
        images = []
        for root, _, files in os.walk(folder):
            for file in files:
                if os.path.splitext(file)[1].lower() in extensions:
                    images.append(os.path.join(root, file))
        return images

    def run_scramble(self):
        target_path = self.target_dir.get()
        source_path = self.source_dir.get()

        if not target_path or not source_path:
            messagebox.showerror("Error", "Please select both folders first.")
            return

        # 1. Gather all replacement images
        replacements = self.get_all_images(source_path)
        if not replacements:
            messagebox.showerror("Error", "No images found in the replacement folder!")
            return

        # 2. Gather all target JPGs
        targets = []
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.lower().endswith(".png"):
                    targets.append(os.path.join(root, file))

        if not targets:
            messagebox.showerror("Error", "No .png files found in the target folder to replace.")
            return

        # 3. Process
        total_files = len(targets)
        self.progress["maximum"] = total_files
        success_count = 0
        
        self.status_var.set(f"Processing {total_files} files...")
        self.root.update()

        for i, target_file in enumerate(targets):
            try:
                # A. Get info about the original file
                with Image.open(target_file) as original_img:
                    orig_size = original_img.size  # (width, height)
                    orig_mode = original_img.mode  # RGB, L, etc.

                # B. Pick a random replacement
                random_source = random.choice(replacements)

                # C. Open random source, resize it, and convert mode
                with Image.open(random_source) as new_img:
                    # Resize to match original exactly
                    resized_img = new_img.resize(orig_size, Image.Resampling.LANCZOS)
                    
                    # Ensure color mode matches (prevents RGB vs Grayscale errors)
                    if resized_img.mode != orig_mode:
                        resized_img = resized_img.convert(orig_mode)
                    
                    # D. Overwrite the target file
                    resized_img.save(target_file, quality=95)
                    success_count += 1

            except Exception as e:
                print(f"Failed to replace {target_file}: {e}")

            # Update UI
            self.progress["value"] = i + 1
            if i % 10 == 0:  # Update text every 10 files to keep GUI responsive
                self.root.update()

        self.status_var.set(f"Done! Scrambled {success_count} / {total_files} files.")
        messagebox.showinfo("Success", f"Chaos complete.\nReplaced {success_count} files.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextureScramblerApp(root)
    root.mainloop()