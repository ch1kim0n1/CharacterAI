import gtts
import os
import tkinter as tk

# Define a function to handle the submit button.
def submit():
    # Get the user's input.
    user_input = entry_field.get()

    # Convert the user's input to speech.
    tts = gtts.gTTS(user_input)

    # Save the converted audio in a file.
    tts.save("user_input.mp3")

    # Play the converted audio.
    os.system("start user_input.mp3")

# Create a window.
window = tk.Tk()

# Set the window size.
window.geometry("500x300")

# Add a label to the window.
label = tk.Label(text="What would you like me to say?")
label.pack()

# Add an entry field to the window.
entry_field = tk.Entry()
entry_field = tk.Entry(width=50)
entry_field.pack()

# Add a button to the window.
button = tk.Button(text="Submit", command=submit)
button.pack()

# Run the main loop.
window.mainloop()
