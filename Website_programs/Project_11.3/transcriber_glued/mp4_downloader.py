from pytube import YouTube
import sys

if len(sys.argv) != 2:
    print("Uso: python <nome_file>")
    sys.exit(1)

url = sys.argv[1]

def mp3_downloader(url):
    yt = YouTube(url)
    print(yt.title)
    video = yt.streams.filter(only_audio=True).first()
    new_filename = 'file_test.mp4'
    download_path = '/Users/fradere/Documents/projects_dir/Project_11/Project_11.3/transcriber_glued'
    print("Downloading...")
    video.download(output_path=download_path, filename=new_filename)
    print("\nDownload complete!")

mp3_downloader(url)