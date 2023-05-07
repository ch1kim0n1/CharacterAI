import gtts
import os

# Get the user's input.
user_input = input("What would you like me to say? ")

# Convert the user's input to speech.
tts = gtts.gTTS(user_input, lang="en-us-female")

# Save the converted audio in a file.
tts.save("user_input.mp3")

# Play the converted audio.
os.system("start user_input.mp3")
