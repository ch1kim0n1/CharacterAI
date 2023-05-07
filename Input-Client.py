import tkinter as tk
import os
from __main__ import *

def text_to_speech(text):
    # Import the necessary modules.
    import subprocess

    # Get the path to the Text-to-Speech.py file.
    text_to_speech_path = os.path.join(os.path.dirname(__file__), "Text-to-Speech.py")

    # Run the Text-to-speech.py file with the user's input as the argument.
    subprocess.call(["python", text_to_speech_path, text])
    
def gettext():
    text = input_box.get()
    return text

# Create the window.
window = tk.Tk()

# Create the input box.
input_box = tk.Entry(window)
input_box.pack()

# Set the window's size.
window.geometry("500x300")

# Set the input box's width.
input_box.config(width=50)

# Create the submit button.
submit_button = tk.Button(window, text="Submit", command=lambda: text_to_speech(input_box.get()))
submit_button.pack()

# Run the main loop.
window.mainloop()
