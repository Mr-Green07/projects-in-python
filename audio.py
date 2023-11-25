import nltk
import pyttsx3

# Create a speaker
speaker = pyttsx3.init()

# Set the speaker's voice
speaker.setProperty('voice', 'english')

# Say something
speaker.say("Hello, world!")

# Wait for the speaker to finish
speaker.runAndWait()