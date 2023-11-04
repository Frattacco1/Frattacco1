import speech_recognition as sr
import sys
if len(sys.argv) != 2:
    print("sus")
    sys.exit(1)

def converter_2(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.listen(source)
        
        try:
           text = r.recognize_google(audio_data, language='en-US')
           print(text)
        except:
           print('doesn\'t work, indian guy lied')

audio_file = sys.argv[1]
converter_2(audio_file)