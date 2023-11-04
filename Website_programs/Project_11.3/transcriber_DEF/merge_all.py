from pytube import YouTube
import speech_recognition as sr
import sys
import os
from os import path
import time
# import threading

# def show_progress():
#     while converter_1.is_alive():
#         for char in ['\\', '|', '/']:
#             print(f'\rWorking: {char} ', end='')
#             time.sleep(0.2)



def mp3_downloader(url):
    yt = YouTube(url)
    print(yt.title)
    video = yt.streams.filter(only_audio=True).first()
    new_filename = 'file_test.mp4'
    download_path = '/Users/fradere/Documents/projects_dir/Project_11/Project_11.3/transcriber_DEF'
    print("Downloading...")
    video.download(output_path=download_path, filename=new_filename)
    print("\nDownload complete!")

def os_converter():
    input_video_path = '/Users/fradere/Documents/projects_dir/Project_11/Project_11.3/transcriber_DEF/file_test.mp4'
    output_audio_path = '/Users/fradere/Documents/projects_dir/Project_11/Project_11.3/transcriber_DEF/file_test.mp3'
    output_audio_wav_path = '/Users/fradere/Documents/projects_dir/Project_11/Project_11.3/transcriber_DEF/converted_audio.wav'
    os.system(f'ffmpeg -i {input_video_path} -vn -acodec mp3 -ab 192k -ar 44100 -y {output_audio_path}')
    sleep = 1
    os.system(f"ffmpeg -i {output_audio_path} -acodec pcm_s16le -ar 16000 {output_audio_wav_path}")

def converter_1(audio_file, output_filename_2):
    recognizer = sr.Recognizer()
    # first converter
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_sphinx(audio)
            with open(f"{output_filename_2}", "a") as file:
                file.write(text)
                file.write('\n')
            print ('-- first conversion completed')
        except sr.UnknownValueError as e:
            print(f"An error occurred: {str(e)}")
            print('-- first converter failed')
        except sr.RequestError as e:
            print(f"An error occurred: {str(e)}")
            print('-- first converter failed')
    # second converter
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_data, language='en-US', key='your_api_key_here') 
            with open(f"{output_filename_2}", "a") as file:
                file.write(text)
            print ('-- second conversion completed')
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print('-- second converter failed')


# input('Paste your URL: ') 
url = 'https://www.youtube.com/watch?v=ry9SYnV3svc'
mp3_downloader(url)
os_converter()

file_name = input('what would you like to call the transcription file? ')
if file_name == '':
    print('the name will be set as transcription_file.txt')
    output_filename = 'transcription_file.txt'
else:
    output_filename = file_name + '.txt'
audio_file = '/Users/fradere/Documents/projects_dir/Project_11/Project_11.3/transcriber_DEF/converted_audio.wav'
output_filename_2 = f'/Users/fradere/Documents/projects_dir/Project_11/Project_11.3/transcriber_DEF/{output_filename}'
print('''
The conversion may take a while depending on the length of the video.
do something else for 5 to 10 minutes.
''')
converter_1(audio_file, output_filename_2)

# This is the threading to show that the program is still running (uses the function show_progress())
# progress_thread = threading.Thread(target=show_progress)
# progress_thread.start()
# converter_1(audio_file= audio_file, output_filename_2=output_filename)
# progress_thread.join()


file_path_1 = '/Users/fradere/Documents/projects_dir/Project_11/Project_11.3/transcriber_DEF/file_test.mp3'
file_path_2 = '/Users/fradere/Documents/projects_dir/Project_11/Project_11.3/transcriber_DEF/file_test.mp4'
try:
    os.remove(file_path_1)
    os.remove(file_path_2)
    os.remove(audio_file)
    print('Excess files deleted.')
except OSError as e:
    print('Error: file not found')

