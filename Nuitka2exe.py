import customtkinter as ctk
from tkinter import filedialog, messagebox, Menu
import subprocess
import threading
import time

# Define a larger font size
large_font = ("Arial", 14)

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    entry_file.delete(0, ctk.END)
    entry_file.insert(0, filename)

def browse_output_dir():
    directory = filedialog.askdirectory()
    entry_output_dir.delete(0, ctk.END)
    entry_output_dir.insert(0, directory)

def browse_data_file():
    filename = filedialog.askopenfilename()
    entry_data_file.delete(0, ctk.END)
    entry_data_file.insert(0, filename)

def browse_icon_file():
    filename = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])
    entry_icon_file.delete(0, ctk.END)
    entry_icon_file.insert(0, filename)

def convert():
    script_file = entry_file.get()
    output_dir = entry_output_dir.get()
    python_version = entry_python_version.get()
    data_file = entry_data_file.get()
    icon_file = entry_icon_file.get()
    plugin_name = entry_plugin_name.get()
    options = []

    # General Options
    if var_standalone.get():
        options.append("--standalone")
    if var_onefile.get():
        options.append("--onefile")
    if var_follow_imports.get():
        options.append("--follow-imports")
    if var_debug.get():
        options.append("--debug")
    if var_lto.get():
        options.append("--lto")
    if var_mingw64.get():
        options.append("--mingw64")
    if var_disable_console.get():
        options.append("--windows-disable-console")
    if var_remove_output.get():
        options.append("--remove-output")
    if var_no_prefer_source.get():
        options.append("--no-prefer-source")
    if var_assume_yes.get():
        options.append("--assume-yes-for-downloads")
    include_package = entry_include_package.get()
    if include_package:
        options.append(f"--include-package={include_package}")
    include_module = entry_include_module.get()
    if include_module:
        options.append(f"--include-module={include_module}")
    nofollow_import_to = entry_nofollow_import_to.get()
    if nofollow_import_to:
        options.append(f"--nofollow-import-to={nofollow_import_to}")        

    # Output Options
    if output_dir:
        options.append(f"--output-dir={output_dir}")
    if python_version:
        options.append(f"--python-version={python_version}")
    if data_file:
        options.append(f"--include-data-file={data_file}={data_file}")
    if icon_file:
        options.append(f"--windows-icon-from-ico={icon_file}")
    if plugin_name:
        options.append(f"--plugin-enable={plugin_name}")

    command = ["python", "-m", "nuitka"] + options + [script_file]

    def run_conversion():
        try:
            progress_bar.set(0)
            progress_bar.configure(fg_color="blue")  # Reset color to blue
            status_label.configure(text="Converting...")
            threading.Thread(target=simulate_progress).start()
            subprocess.run(command, check=True)
            progress_bar.set(1)
            status_label.configure(text="Conversion completed successfully!")
            messagebox.showinfo("Success", "Conversion completed successfully!")
        except subprocess.CalledProcessError as e:
            progress_bar.set(0)
            progress_bar.configure(fg_color="red")  # Change color to red on failure
            status_label.configure(text="Conversion failed.")
            messagebox.showerror("Error", f"Conversion failed: {e}")

    def simulate_progress():
        for i in range(101):
            time.sleep(0.1)  # Simulate time delay for progress
            progress_bar.set(i / 100)
            percentage_label.configure(text=f"{i}%")
            app.update_idletasks()

    threading.Thread(target=run_conversion).start()

def show_info():
    info_message = (
        "Nuitka Converter v1.0 By Zied Boughdir 2024\n"
        "How to use this app:\n"
        "- Always check the 'Standalone' option.\n"
        "- You can check other options as needed.\n"
        "- Browse and select the Python script you want to convert.\n"
        "- Specify the output directory.\n"
        "- Optionally, specify the Python version and additional files.\n"
        "- Click 'Convert' to start the conversion process."
    )
    messagebox.showinfo("Information", info_message)

app = ctk.CTk()
app.title("Nuitka Converter GUI v1.0")

# Create a menu bar using tkinter
menu_bar = Menu(app)
app.config(menu=menu_bar)

# Add an "Info" menu
info_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Info", menu=info_menu)
info_menu.add_command(label="How to Use", command=show_info)

frame = ctk.CTkFrame(app)
frame.pack(padx=10, pady=10)

# General Options
ctk.CTkLabel(frame, text="Additional Options:", font=large_font).grid(row=12, column=0, sticky="w", pady=(10, 0))
var_assume_yes = ctk.BooleanVar()
ctk.CTkCheckBox(frame, text="Assume Yes for Downloads", variable=var_assume_yes, font=large_font).grid(row=13, column=0, sticky="w", pady=5)

ctk.CTkLabel(frame, text="Include Package:", font=large_font).grid(row=14, column=0, sticky="e", pady=5)
entry_include_package = ctk.CTkEntry(frame, width=300, height=30, font=large_font)
entry_include_package.grid(row=14, column=1, pady=5)

ctk.CTkLabel(frame, text="Include Module:", font=large_font).grid(row=15, column=0, sticky="e", pady=5)
entry_include_module = ctk.CTkEntry(frame, width=300, height=30, font=large_font)
entry_include_module.grid(row=15, column=1, pady=5)

ctk.CTkLabel(frame, text="No Follow Import To:", font=large_font).grid(row=16, column=0, sticky="e", pady=5)
entry_nofollow_import_to = ctk.CTkEntry(frame, width=300, height=30, font=large_font)
entry_nofollow_import_to.grid(row=16, column=1, pady=5)

ctk.CTkLabel(frame, text="Add Python Script:", font=large_font).grid(row=0, column=0, sticky="e", pady=5)
entry_file = ctk.CTkEntry(frame, width=300, height=30, font=large_font)  # Increased width and height
entry_file.grid(row=0, column=1, pady=5)
ctk.CTkButton(frame, text="Browse", command=browse_file, font=large_font).grid(row=0, column=2, pady=5)

ctk.CTkLabel(frame, text="Add Output Directory:", font=large_font).grid(row=1, column=0, sticky="e", pady=5)
entry_output_dir = ctk.CTkEntry(frame, width=300, height=30, font=large_font)  # Increased width and height
entry_output_dir.grid(row=1, column=1, pady=5)
ctk.CTkButton(frame, text="Browse", command=browse_output_dir, font=large_font).grid(row=1, column=2, pady=5)

ctk.CTkLabel(frame, text="Additional Files(optional):", font=large_font).grid(row=2, column=0, sticky="e", pady=5)
entry_data_file = ctk.CTkEntry(frame, width=300, height=30, font=large_font)  # Increased width and height
entry_data_file.grid(row=2, column=1, pady=5)
ctk.CTkButton(frame, text="Browse", command=browse_data_file, font=large_font).grid(row=2, column=2, pady=5)

ctk.CTkLabel(frame, text="Icon File(optional):", font=large_font).grid(row=3, column=0, sticky="e", pady=5)
entry_icon_file = ctk.CTkEntry(frame, width=300, height=30, font=large_font)  # Increased width and height
entry_icon_file.grid(row=3, column=1, pady=5)
ctk.CTkButton(frame, text="Browse", command=browse_icon_file, font=large_font).grid(row=3, column=2, pady=5)

ctk.CTkLabel(frame, text="Plugin Name(optional):", font=large_font).grid(row=4, column=0, sticky="e", pady=5)
entry_plugin_name = ctk.CTkEntry(frame, width=300, height=30, font=large_font)  # Increased width and height
entry_plugin_name.grid(row=4, column=1, pady=5)

ctk.CTkLabel(frame, text="Python Version(optional):", font=large_font).grid(row=5, column=0, sticky="e", pady=5)
entry_python_version = ctk.CTkEntry(frame, width=300, height=30, font=large_font)  # Increased width and height
entry_python_version.grid(row=5, column=1, pady=5)

# General Options
ctk.CTkLabel(frame, text="General Options:", font=large_font).grid(row=6, column=0, sticky="w", pady=(10, 0))
var_standalone = ctk.BooleanVar(value=True)  # Standalone option always checked
ctk.CTkCheckBox(frame, text="Standalone", variable=var_standalone, font=large_font).grid(row=7, column=0, sticky="w", pady=5)
var_onefile = ctk.BooleanVar()
ctk.CTkCheckBox(frame, text="Onefile", variable=var_onefile, font=large_font).grid(row=7, column=1, sticky="w", pady=5)
var_follow_imports = ctk.BooleanVar()
ctk.CTkCheckBox(frame, text="Follow Imports", variable=var_follow_imports, font=large_font).grid(row=8, column=0, sticky="w", pady=5)
var_debug = ctk.BooleanVar()
ctk.CTkCheckBox(frame, text="Debug", variable=var_debug, font=large_font).grid(row=8, column=1, sticky="w", pady=5)
var_lto = ctk.BooleanVar()
ctk.CTkCheckBox(frame, text="Optimization (LTO)", variable=var_lto, font=large_font).grid(row=9, column=0, sticky="w", pady=5)
var_mingw64 = ctk.BooleanVar()
ctk.CTkCheckBox(frame, text="Use MinGW64", variable=var_mingw64, font=large_font).grid(row=9, column=1, sticky="w", pady=5)
var_disable_console = ctk.BooleanVar()
ctk.CTkCheckBox(frame, text="Disable Console", variable=var_disable_console, font=large_font).grid(row=10, column=0, sticky="w", pady=5)
var_remove_output = ctk.BooleanVar()
ctk.CTkCheckBox(frame, text="Remove Output", variable=var_remove_output, font=large_font).grid(row=10, column=1, sticky="w", pady=5)
var_no_prefer_source = ctk.BooleanVar()
ctk.CTkCheckBox(frame, text="No Prefer Source", variable=var_no_prefer_source, font=large_font).grid(row=11, column=0, sticky="w", pady=5)

ctk.CTkButton(app, text="Convert", command=convert, font=large_font).pack(pady=10)

# Add a progress bar with style
progress_bar = ctk.CTkProgressBar(app, width=600, height=20, border_width=2, fg_color="blue", bg_color="lightgray")
progress_bar.pack(pady=5)
progress_bar.set(0)

# Add a percentage label
percentage_label = ctk.CTkLabel(app, text="0%", anchor="w", font=large_font)
percentage_label.pack(fill=ctk.X)

# Add a status label
status_label = ctk.CTkLabel(app, text="", anchor="w", font=large_font)
status_label.pack(fill=ctk.X)

app.mainloop()