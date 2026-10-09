#text to speach
from gtts import gTTS
import os

# Text to be converted to speech
text = input("Enter a text-to convert to  speech conversion ")

# Language in which you want to convert
language = 'en'

# Creating the gTTS object
tts = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file
tts.save("output.mp3")

# Playing the converted file
os.system("output.mp3")