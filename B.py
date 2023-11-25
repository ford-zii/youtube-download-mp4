import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import Playlist, YouTube 
import os
import subprocess
import time
def download_playlist():
    playlist_url = playlist_entry.get("1.0", "end").splitlines()
    save_path = filedialog.askdirectory()
    print(f'playlist_url: {playlist_url}')
    
    for link in playlist_url:
        try:
            playlist = Playlist(link)
            path_c = 1
            while os.path.exists(save_path):
                save_path = f"{save_path} {path_c}"
                path_c += 1
            # playlist._video_regex = r"\"url\":\"(/watch\?v=[\w-]*)"

            # playlist.populate_video_urls()
            
            # for url in playlist.video_urls:
            #     print(f' --> url: {url}')
            #     video = YouTube(url)
            #     video.streams.get_audio_only().download(output_path=save_path)
            #     time.sleep(5)
            time.sleep(1)
            for link in playlist.video_urls:
                try:
                    video = YouTube(link)
                    audio_stream = video.streams.filter(only_audio=True).first()
                    output_path = save_path
                    base_file_name = video.title.replace(" ", "")
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
                    # os.remove(os.path.join(output_path, f"{video.title}.mp4"))
                    
                    print(f"{base_file_name}.mp3 downloaded successfully!")
                except Exception as e:
                    print(f"Error downloading {link}: {e}")
                else:
                    try:
                        time.sleep(1)
                        os.remove(os.path.join(output_path, f"{video.title}.mp4")) # Remove the downloaded video file
                    except OSError as e:
                        print(f"Error removing file: {str(e)}")

            
            # messagebox.showinfo("Success", "Playlist downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    messagebox.showinfo("Success", "Playlist downloaded successfully!")

# Create the main window
window = tk.Tk()
window.title("YouTube Playlist Downloader")

# Create the playlist URL label and entry field
playlist_label = tk.Label(window, text="Playlist URL:")
playlist_label.pack()
playlist_entry = tk.Text(window, height=50, width=100)
playlist_entry.pack()


# Create the download button
download_button = tk.Button(window, text="Download Playlist", command=download_playlist)
download_button.pack()

# Start the main window loop
window.mainloop()

# https://www.youtube.com/watch?v=s8QzkOulL5w&list=RDCLAK5uy_mM9KAjdJ5fcD34qUO3IclaRMLPNO-ChN4
# https://www.youtube.com/watch?v=2dSGCzeuPlA&list=RDCLAK5uy_mZUgygi3RFeG-_hkk5hhoM_2LOXyxNSZ4
# https://www.youtube.com/watch?v=AH7A9hBntE4&list=RDCLAK5uy_mg0s8OVhK8HgyAHeDYr7geocCCEfEs7d4
# https://www.youtube.com/watch?v=cqQAzpZBpAw&list=RDCLAK5uy_mtBelM5Zoku9XQJOHatr0451unVlouwQQ
# https://www.youtube.com/watch?v=HkMNOlYcpHg&list=RDHkMNOlYcpHg
# https://www.youtube.com/watch?v=qjrUDZoqWRY&list=RDGMEM6ijAnFTG9nX1G-kbWBUCJAVMqjrUDZoqWRY
# https://www.youtube.com/watch?v=7zhwihAXMlI&list=RD7zhwihAXMlI
# https://www.youtube.com/watch?v=h7EK6aOzqWg&list=RDh7EK6aOzqWg
# https://www.youtube.com/watch?v=eVD9j36Ke94&list=RDeVD9j36Ke94
# https://www.youtube.com/watch?v=3T1Rb_iM2no&list=RD3T1Rb_iM2no
# https://www.youtube.com/watch?v=jf8m9INK2n4&list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbAVMjf8m9INK2n4
# https://www.youtube.com/watch?v=FTTy57qqUCY&list=RDFTTy57qqUCY
# https://www.youtube.com/watch?v=5omQSCqnES0&list=RD5omQSCqnES0
# https://www.youtube.com/watch?v=F8Cg572dafQ&list=RDGMEMHDXYb1_DDSgDsobPsOFxpAVMF8Cg572dafQ