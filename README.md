This application is a graphical user interface (GUI) for converting Python scripts into standalone executables using Nuitka. Nuitka is a Python-to-C compiler that can compile Python code into highly optimized C code, which can then be executed as a standalone program. The GUI is built using the `customtkinter` library, which provides a modern look and feel for Tkinter applications.

![image](https://github.com/user-attachments/assets/fd36b5d7-3190-42b7-a494-d5fe5b42721a)


### Features

- **File Browsing**: Users can browse and select the Python script they want to convert, specify the output directory, and optionally select additional files and an icon file.
- **Conversion Options**: The app provides several options for customizing the conversion process, such as:
  - Standalone mode
  - Onefile mode
  - Follow imports
  - Debug mode
  - Optimization (LTO)
  - Use of MinGW64
  - Disabling the console
  - Removing output
  - No prefer source
  - Assume yes for downloads
- **Plugin and Version Support**: Users can specify a plugin name and Python version for the conversion.
- **Progress Indication**: A progress bar and percentage label indicate the conversion progress, and a status label provides feedback on the conversion status.
- **Menu and Information**: The app includes a menu with an "Info" section that provides guidance on how to use the application.

### How to Use

1. **Select the Python Script**: Use the "Browse" button to select the Python script you want to convert.
2. **Specify Output Directory**: Choose the directory where the output executable will be saved.
3. **Set Additional Options**: Check the options you need for the conversion process.
4. **Convert**: Click the "Convert" button to start the conversion process. The progress bar will indicate the progress, and a message box will notify you upon completion.

This tool is designed to simplify the process of converting Python scripts into standalone executables, making it accessible even to users who may not be familiar with command-line tools.
