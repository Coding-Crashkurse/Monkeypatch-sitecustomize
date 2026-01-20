import os
import sys
import site

MAGIC_CODE = """
import sys
import tkinter as tk
from tkinter import messagebox

print("\\n[SYSTEM SECURITY LAYER LOADED]\\n")

def show_popup_handler(exc_type, exc_value, exc_traceback):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("CRITICAL ERROR", f"Process crashed!\\n\\nReason: {exc_value}")
    root.destroy()
    sys.exit(1)

sys.excepthook = show_popup_handler
"""

def get_magic_path():
    packages_dirs = site.getsitepackages()
    return os.path.join(packages_dirs[0], "sitecustomize.py")

def toggle_magic():
    target_file = get_magic_path()
    print(f"Target: {target_file}")
    
    if os.path.exists(target_file):
        os.remove(target_file)
        print("-> REMOVED. System normal.")
    else:
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(MAGIC_CODE)
        print("-> INJECTED. Magic active.")

if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        print("WARNING: Not in a venv! Press ENTER to continue...")
        input()
        
    toggle_magic()