import speech_recognition as sr
from os import path
import sys
if len(sys.argv) != 2:
    print("sus")
    sys.exit(1)

def converter(audio_file):
    recognizer = sr.Recognizer() # start the recogniser
    def callback(recognizer, audio):
        print("Transcribing audio...")

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_sphinx(audio)
            print(text)
        except sr.UnknownValueError:
            print("Sphinx could not understand the audio -- first converter failed")
        except sr.RequestError as e:
            print(f"Could not request results from Sphinx; {e}")
            print('-- first converter failed')

audio_file = sys.argv[1]
converter(audio_file)
