import tkinter as tk
import pytube
import os
import subprocess
import time

# https://www.youtube.com/watch?v=Ys7XbRslm1o
# https://www.youtube.com/watch?v=k2_5MHUDFVE
# https://www.youtube.com/watch?v=l4PXTV8k-C0

def download_mp3():
    links = link_entry.get("1.0", "end").splitlines()

    for link in links:
        try:
            video = pytube.YouTube(link)
            audio_stream = video.streams.filter(only_audio=True).first()
            output_path = "path/to/save/directory"
            base_file_name = video.title
            output_file = os.path.join(output_path, f"{base_file_name}.mp3")
            
            # Check if the file already exists, if yes, append a number to the name
            count = 1
            while os.path.exists(output_file):
                base_file_name = f"{video.title} ({count})"
                output_file = os.path.join(output_path, f"{base_file_name}.mp3")
                count += 1
            
            audio_stream.download(output_path=output_path)
            print(output_file)
            print({video.title}, '\n')
            
            # Convert the downloaded file to MP3 using ffmpeg
            subprocess.call(['ffmpeg', '-i', os.path.join(output_path, f"{video.title}.mp4"), output_file])
            
            # Remove the original downloaded file
            os.remove(os.path.join(output_path, f"{video.title}.mp4"))
            
            print(f"{base_file_name}.mp3 downloaded successfully!")
        except Exception as e:
            print(f"Error downloading {link}: {e}")
        else:
            try:
                time.sleep(1)
                os.remove(os.path.join(output_path, f"{video.title}.mp4")) # Remove the downloaded video file
            except OSError as e:
                print(f"Error removing file: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("YouTube MP3 Downloader")

# Create a label and an entry for entering the YouTube links
link_label = tk.Label(window, text="Enter YouTube links (one per line):")
link_label.pack()

link_entry = tk.Text(window, height=10, width=50)
link_entry.pack()

# Create a button to start the download
download_button = tk.Button(window, text="Download MP3", command=download_mp3)
download_button.pack()

# Start the GUI event loop
window.mainloop()
