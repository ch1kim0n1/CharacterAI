import gtts
import os
from Input-Client import *

precoded_text = Input-Client.gettext()

# Convert the precoded text to speech.
tts = gtts.gTTS(precoded_text)

# Save the converted audio in a file.
tts.save("precoded_input.mp3")

# Play the converted audio.
os.system("start precoded_input.mp3")
