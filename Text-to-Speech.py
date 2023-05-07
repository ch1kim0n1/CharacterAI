import pyttsx3
import gtts
import os

# Get the user's input.
user_input = input("What would you like me to say? ")

# Convert the user's input to speech.
tts = gtts.gTTS(user_input)

# Create a pyttsx3 engine object.
engine = pyttsx3.init()

engine.setProperty('rate', 150)
# Set volume 0-1
engine.setProperty('volume', 0.7)

# Speak text using the engine object.
engine.say(tts)

# Stop the engine
engine.stop()

# Save the converted audio in a file.
tts.save("user_input.mp3")

# Play the converted audio.
os.system("start user_input.mp3")
