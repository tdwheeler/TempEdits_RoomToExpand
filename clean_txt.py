import os
import re
import tkinter as tk
from tkinter import filedialog

def clean_text_file():
    # Create a Tkinter root window (it will not be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog for the user to select the file
    input_path = filedialog.askopenfilename(title="Select a .txt file to clean", filetypes=[("Text Files", "*.txt")])

    if not input_path:  # If no file is selected, exit the function
        print("No file selected. Exiting.")
        return

    # Get the directory and filename
    directory, original_filename = os.path.split(input_path)
    base_name, _ = os.path.splitext(original_filename)
    
    # Define the output path in the same directory as the script
    output_path = os.path.join(directory, f"{base_name}_cleaned.txt")

    # Read the original file and ensure it is in UTF-8 encoding
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    # Remove special characters, keeping only common punctuation, letters, and numbers
    # Preserve spacing and newlines
    cleaned_content = re.sub(r'[^\w\s.,;:!?\'"-]', '', content)
    
    # Write the cleaned content to a new file in UTF-8 encoding
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

    print(f"File cleaned and saved to {output_path}")

# Run the function
clean_text_file()