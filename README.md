# Morse Code Translator

## Description
The Morse Code Translator is a desktop application that allows users to convert text to Morse code and vice versa. The application features an attractive user interface built with Tkinter, where users can easily input their text or Morse code and get instant translations. Additionally, a welcoming message appears on startup, enhancing the user experience.

## Features
- Text to Morse code conversion
- Morse code to text conversion
- User-friendly interface with attractive design
- Animated welcome message displayed upon startup
- Easy navigation between conversion types

## Technologies Used
- Python 3.x
- Tkinter (for GUI)
- Morse Code Dictionary (for conversion logic)


## Creating a Desktop Executable
To package the application into a standalone executable, use PyInstaller. Follow these steps:

1. Install PyInstaller if you haven't already:
   ```bash
   pip install pyinstaller
   ```

2. Navigate to your project directory where `morse_app.py` is located:
   ```bash
   cd <repository-name>
   ```

3. Run PyInstaller to create the executable:
   ```bash
   pyinstaller --onefile --windowed --icon=img.ico morse_app.py
   ```

   Replace `img.ico` with the relative path to your icon image file in the repository.

4. After running the command, the executable will be created in the `dist` folder within your project directory.

## Usage
1. Run the application.
2. Choose the conversion type (Text to Morse or Morse to Text).
3. Input your text or Morse code.
4. Click the Convert button to see the results.


