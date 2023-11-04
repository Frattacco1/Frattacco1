import os
import time

# URL for the download
download_url = "your_download_url"

# Path to the downloaded file
downloaded_file = "output_audio.mp3"

# Customize the maximum wait time in seconds
max_wait_time = 120  # You can adjust this as needed

# Download the file (use your download code here)

# Check if the downloaded file exists and wait until it does
start_time = time.time()
while not os.path.exists(downloaded_file):
    if time.time() - start_time > max_wait_time:
        print("Download took too long. Exiting.")
        break
    time.sleep(1)  # Wait for 1 second




################
if os.path.exists(downloaded_file):
    print("Downloaded file is ready, starting conversion.")
    os.system(f"ffmpeg -i {downloaded_file} -acodec pcm_s16le -ar 16000 converted_audio.wav")
else:
    print("Downloaded file not found. Check your download process.")
################