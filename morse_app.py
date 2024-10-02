import tkinter as tk  # Import tkinter for GUI functionality
import tkinter.font as tkFont  # Import font module for custom fonts

# Morse code dictionary mapping letters and numbers to their Morse code equivalents
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
    '(': '-.--.', ')': '-.--.-'
}

# Function to convert text to Morse code
def text_to_morse(text):
    morse_code = ""  # Initialize an empty string to store the Morse code
    for char in text.upper():  # Loop through each character in the input text, converted to uppercase
        if char != " ":  # If the character is not a space
            morse_code += MORSE_CODE_DICT.get(char, "") + " "  # Convert it to Morse code and add a space
        else:
            morse_code += " / "  # Add a separator for spaces ("/")
    return morse_code.strip()  # Return the Morse code, removing any trailing spaces

# Function to convert Morse code to text
def morse_to_text(morse_code):
    morse_code += " "  # Add a space to the end of the input to process the last character
    decipher = ""  # Initialize an empty string to store the decoded text
    citext = ""  # Initialize a string to store each Morse code symbol
    for char in morse_code:  # Loop through each character in the Morse code
        if char != " ":  # If the character is not a space
            i = 0  # Reset space counter
            citext += char  # Add character to Morse symbol
        else:
            i += 1  # Count the spaces
            if i == 2:  # If two spaces are found, it indicates a new word
                decipher += " "  # Add space to separate words
            else:
                # Find the letter corresponding to the Morse code symbol
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ""  # Reset the Morse code symbol string
    return decipher  # Return the decoded text

# Function to update the result label with the Morse code or text
def update_result_label(result, label):
    label.config(text=result)  # Set the label's text to the result
    blink_result(result, label)  # Start blinking effect on the result

# Function to create a blinking effect for the result text
def blink_result(result, label):
    if not result:
        return  # Stop blinking if result is empty

    current_text = ""  # Initialize an empty string to store the blinking text
    index = 0  # Start index for character-by-character display

    # Inner function to update the text one character at a time
    def blink():
        nonlocal index, current_text  # Use outer variables
        if index < len(result):  # If more characters are left to display
            current_text += result[index]  # Add the next character
            index += 1  # Move to the next character
        label.config(text=current_text)  # Update the label with the current text
        label.after(500, blink)  # Set a delay of 500ms before the next blink

        # Toggle the text color between white and black for blinking effect
        if index <= len(result):
            label.config(fg='white' if label.cget('fg') == 'black' else 'black')

    blink()  # Start the blinking effect

# Function to display welcome message letter by letter
def show_welcome_message():
    welcome_text = "Welcome\n" + text_to_morse("Welcome")
    current_text = ""
    index = 0

    def display():
        nonlocal index, current_text
        if index < len(welcome_text):
            current_text += welcome_text[index]
            welcome_label.config(text=current_text)  # Update welcome label
            index += 1
            welcome_label.after(150, display)  # Delay for 150ms
        else:
            # Stop blinking once the welcome message is fully displayed
            welcome_label.config(fg='white')

    display()  # Start displaying the welcome message

# Function to show a specific frame and reset previous results
def show_frame(frame):
    result_label.config(text="")  # Clear the result label on "Text to Morse" page
    result_label_morse.config(text="")  # Clear the result label on "Morse to Text" page
    frame.tkraise()  # Bring the selected frame to the front

# Main application window setup
root = tk.Tk()  # Create the main window
root.title("Morse Code Translator")  # Set the window title
root.geometry("450x400")  # Set the window size
root.configure(bg='black')  # Set the background color to black

# Define a custom font for text and labels
custom_font = tkFont.Font(family="Arial", size=12, weight="bold")

# Create frames for different pages (Main, Text to Morse, and Morse to Text)
main_frame = tk.Frame(root, bg='black')  # Main menu frame
text_to_morse_frame = tk.Frame(root, bg='black')  # Text to Morse conversion frame
morse_to_text_frame = tk.Frame(root, bg='black')  # Morse to Text conversion frame

# Position the frames in a grid layout (only one is visible at a time)
for frame in (main_frame, text_to_morse_frame, morse_to_text_frame):
    frame.grid(row=0, column=0, sticky='nsew')

# Main page widgets
welcome_label = tk.Label(main_frame, text="", bg='black', fg='white', font=("Arial", 16), justify='center')
welcome_label.pack(pady=20)  # Add padding around the welcome label

show_welcome_message()  # Show the welcome message

main_title = tk.Label(main_frame, text="Select Conversion Type", bg='black', fg='white', font=("Arial", 16))  # Title label
main_title.pack(pady=20)  # Add padding around the title

# Button to navigate to "Text to Morse" page
text_to_morse_btn = tk.Button(main_frame, text="Text to Morse", command=lambda: show_frame(text_to_morse_frame), bg='gray', fg='white', font=("Arial", 12))
text_to_morse_btn.pack(pady=5)  # Add padding around the button

# Button to navigate to "Morse to Text" page
morse_to_text_btn = tk.Button(main_frame, text="Morse to Text", command=lambda: show_frame(morse_to_text_frame), bg='gray', fg='white', font=("Arial", 12))
morse_to_text_btn.pack(pady=5)  # Add padding around the button

# "Text to Morse" page widgets
text_title = tk.Label(text_to_morse_frame, text="Text to Morse Converter", bg='black', fg='white', font=("Arial", 16))  # Title label
text_title.pack(pady=20)  # Add padding

# Label and entry field for text input
text_label = tk.Label(text_to_morse_frame, text="Enter Text:", bg='black', fg='white', font=custom_font)  # Input label
text_label.pack(pady=10)  # Add padding
text_entry = tk.Entry(text_to_morse_frame, width=50, font=custom_font)  # Entry widget for text input with custom font
text_entry.pack(padx=10, pady=10)  # Add padding

# Label to display the Morse code result
result_label = tk.Label(text_to_morse_frame, text="", bg='black', fg='green', font=("Arial", 12))
result_label.pack(pady=20)  # Add padding

# Function for converting text to Morse code and displaying the result
def convert_text_to_morse():
    text = text_entry.get()  # Get the input text from the entry widget
    morse_result = text_to_morse(text)  # Convert the text to Morse code
    update_result_label(morse_result, result_label)  # Update the result label

# Button to trigger the conversion from text to Morse code
convert_text_btn = tk.Button(text_to_morse_frame, text="Convert", command=convert_text_to_morse, bg='gray', fg='white', font=("Arial", 12))
convert_text_btn.pack(pady=5)  # Add padding

# Button to go back to the main menu
back_to_main_btn = tk.Button(text_to_morse_frame, text="Back", command=lambda: show_frame(main_frame), bg='gray', fg='white', font=("Arial", 12))
back_to_main_btn.pack(pady=5)  # Add padding

# "Morse to Text" page widgets
morse_title = tk.Label(morse_to_text_frame, text="Morse to Text Converter", bg='black', fg='white', font=("Arial", 16))  # Title label
morse_title.pack(pady=20)  # Add padding

# Label and entry field for Morse code input
morse_label = tk.Label(morse_to_text_frame, text="Enter Morse Code:", bg='black', fg='white', font=custom_font)  # Input label
morse_label.pack(pady=10)  # Add padding
morse_entry = tk.Entry(morse_to_text_frame, width=50, font=custom_font)  # Entry widget for Morse code input with custom font
morse_entry.pack(padx=10, pady=10)  # Add padding

# Label to display the text result
result_label_morse = tk.Label(morse_to_text_frame, text="", bg='black', fg='green', font=("Arial", 12))
result_label_morse.pack(pady=20)  # Add padding

# Function for converting Morse code to text and displaying the result
def convert_morse_to_text():
    morse_text = morse_entry.get()  # Get the input Morse code from the entry widget
    text_result = morse_to_text(morse_text)  # Convert the Morse code to text
    update_result_label(text_result, result_label_morse)  # Update the result label

# Button to trigger the conversion from Morse code to text
convert_morse_btn = tk.Button(morse_to_text_frame, text="Convert", command=convert_morse_to_text, bg='gray', fg='white', font=("Arial", 12))
convert_morse_btn.pack(pady=5)  # Add padding

# Button to go back to the main menu
back_to_main_btn_morse = tk.Button(morse_to_text_frame, text="Back", command=lambda: show_frame(main_frame), bg='gray', fg='white', font=("Arial", 12))
back_to_main_btn_morse.pack(pady=5)  # Add padding

# Show the main frame on startup
main_frame.tkraise()  # Display the main frame first

# Start the GUI event loop
root.mainloop()  # Run the application
