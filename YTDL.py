import os
import tkinter as tk
import tkinter.messagebox as messagebox
import clipboard
import time
from pytube import YouTube
from moviepy.editor import *
from tqdm import tqdm

def download_video(url, output_path):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    
    return video.download(output_path)

def convert_to_mp3(video_path, output_path):
    video = VideoFileClip(video_path)
    return video.audio.write_audiofile(output_path)

def download_and_convert_videos(urls, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for url in tqdm(urls, desc="Downloading and converting"):
        try:
            video_p = download_video(url, output_path)
            print(video_p, 'video_p')
            # video_file = os.path.join(output_path, url.split('=')[-1] + '.mp4')
            mp3_file = os.path.join(output_path, video_p.replace('.mp4','').split('=')[-1] + '.mp3')
            print(mp3_file, 'mp3_file')

            convert_to_mp3(output_path, mp3_file)
            
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")
        else:
            print(f"Downloaded and converted: {mp3_file}")

            try :
                time.sleep(1)
                os.remove(video_p) # Remove the downloaded video file
            except OSError as e:
                print(f"Error removing file: {str(e)}")

def download_button_clicked():
    video_urls = url_text.get("1.0", "end-1c").split("\n")
    output_directory = output_text.get("1.0", "end-1c")

    download_and_convert_videos(video_urls, output_directory)

    status_label.config(text="Download complete!")

def clipboard_monitor():
    previous_clipboard = clipboard.paste()
    while True:
        current_clipboard = clipboard.paste()
        if current_clipboard != previous_clipboard:
            if "youtube.com" in current_clipboard:
                url_text.insert("end-1c", current_clipboard + "\n")
                messagebox.showinfo("YouTube URL Detected", "YouTube URL copied to the program!")
        previous_clipboard = current_clipboard

# Create the main window
window = tk.Tk()
window.title("YouTube MP3 Downloader")

# Create URL input label and text box
url_label = tk.Label(window, text="Enter YouTube URLs (one per line):")
url_label.pack()
url_text = tk.Text(window, height=5, width=50)
url_text.pack()

# Create output directory input label and text box
output_label = tk.Label(window, text="Output Directory:")
output_label.pack()
output_text = tk.Text(window, height=1, width=50)
output_text.pack()

# Create download button
download_button = tk.Button(window, text="Download", command=download_button_clicked)
download_button.pack()

# Create status label
status_label = tk.Label(window, text="")
status_label.pack()

# # Start clipboard monitoring in a separate thread
# window.after(0, clipboard_monitor)

# Run the GUI
window.mainloop()
