#!/bin/bash
echo "URL video da trascrivere: "
read url
var_ur="$url"
python mp4_downloader.py "$var_ur" &
sleep 10
ffmpeg -i file_test.mp4 -vn -acodec mp3 -ab 192k -ar 44100 -y output_audio.mp3
sleep 1
ffmpeg -i output_audio.mp3 -acodec pcm_s16le -ar 16000 converted_audio.wav
echo ' '
echo 'last bit of the program, this may take a while...'
sleep 1
other_file="converted_audio.wav"
echo "------------converter_1--------------" >> transcription_def.txt
python converter_1.py "$other_file" >> transcription_def.txt
echo 'first converter --done'
echo "------------converter_2--------------" >> transcription_def.txt
python converter_2.py "$other_file" >> transcription_def.txt
echo 'second converter --done'
rm /Users/fradere/Documents/projects_dir/Project_11/Project_11.3/transcriber_glued/file_test.mp4
rm /Users/fradere/Documents/projects_dir/Project_11/Project_11.3/transcriber_glued/output_audio.mp3
rm /Users/fradere/Documents/projects_dir/Project_11/Project_11.3/transcriber_glued/converted_audio.wav
echo 'remove extra files -- done'