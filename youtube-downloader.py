import tkinter as tk
from tkinter import ttk, messagebox
from yt_dlp import YoutubeDL
import os
import subprocess

class YouTubeDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        
        # Set window size and position
        window_width = 600
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # URL input field
        url_frame = ttk.Frame(root)
        url_frame.pack(pady=10, padx=10, fill='x')
        
        ttk.Label(url_frame, text="YouTube URL:").pack(side='left')
        self.url_entry = ttk.Entry(url_frame)
        self.url_entry.pack(side='left', fill='x', expand=True, padx=(5, 0))

        # Download type selection
        type_frame = ttk.Frame(root)
        type_frame.pack(pady=10, padx=10)
        
        self.download_type = tk.StringVar(value="audio")
        ttk.Radiobutton(type_frame, text="Audio (MP3)", 
                       variable=self.download_type, 
                       value="audio",
                       command=self.toggle_quality_selector).pack(side='left', padx=10)
        ttk.Radiobutton(type_frame, text="Video (MP4)", 
                       variable=self.download_type, 
                       value="video",
                       command=self.toggle_quality_selector).pack(side='left', padx=10)
        ttk.Radiobutton(type_frame, text="Subtitle", 
                       variable=self.download_type, 
                       value="subtitle",
                       command=self.toggle_quality_selector).pack(side='left', padx=10)

        # Video quality selection
        self.quality_frame = ttk.Frame(root)
        self.quality_frame.pack(pady=10, padx=10)
        
        ttk.Label(self.quality_frame, text="Video Quality:").pack(side='left')
        self.quality_var = tk.StringVar(value="1080p")
        self.quality_combo = ttk.Combobox(self.quality_frame, 
                                        textvariable=self.quality_var,
                                        values=["2160p", "1440p", "1080p", "720p", "480p", "360p"],
                                        state="readonly",
                                        width=10)
        self.quality_combo.pack(side='left', padx=5)

        # Subtitle language selection
        self.subtitle_frame = ttk.Frame(root)
        self.subtitle_frame.pack(pady=10, padx=10)
        
        ttk.Label(self.subtitle_frame, text="Subtitle Language:").pack(side='left')
        self.subtitle_lang = tk.StringVar(value="en")
        self.subtitle_combo = ttk.Combobox(self.subtitle_frame, 
                                         textvariable=self.subtitle_lang,
                                         values=["en", "zh-Hans", "ja", "ko", "auto"],
                                         state="readonly",
                                         width=10)
        self.subtitle_combo.pack(side='left', padx=5)
        
        # Initially hide quality and subtitle selections (default is audio mode)
        self.quality_frame.pack_forget()
        self.subtitle_frame.pack_forget()

        # Download button
        ttk.Button(root, text="Download", 
                  command=self.start_download).pack(pady=10)

        # Progress label
        self.status_label = ttk.Label(root, text="")
        self.status_label.pack(pady=5)

    def toggle_quality_selector(self):
        download_type = self.download_type.get()
        self.quality_frame.pack_forget()
        self.subtitle_frame.pack_forget()
        
        if download_type == "video":
            self.quality_frame.pack(pady=10, padx=10)
        elif download_type == "subtitle":
            self.subtitle_frame.pack(pady=10, padx=10)

    def start_download(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return

        download_type = self.download_type.get()
        self.status_label.config(text="Starting download...")
        
        try:
            if download_type == "audio":
                self.download_audio(url)
            elif download_type == "video":
                quality = self.quality_var.get()
                self.download_video(url, quality)
            else:  # subtitle
                lang = self.subtitle_lang.get()
                self.download_subtitle(url, lang)
            
            self.status_label.config(text="Download completed!")
            messagebox.showinfo("Success", "Download completed!")
        except Exception as e:
            self.status_label.config(text="Download failed!")
            messagebox.showerror("Error", f"Download failed: {str(e)}")

    def download_subtitle(self, url, lang):
        ydl_opts = {
            'writeautomaticsub': True,
            'writesubtitles': True,
            'subtitleslangs': [lang],
            'skip_download': True,
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegSubtitlesConvertor',
                'format': 'txt'
            }]
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def download_audio(self, url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': 'C:\\ffmpeg\\bin\\ffmpeg.exe',
            'outtmpl': '%(title)s.%(ext)s'
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def download_video(self, url, quality):
        quality_format = {
            '2160p': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',
            '1440p': 'bestvideo[height<=1440]+bestaudio/best[height<=1440]',
            '1080p': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            '720p': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
            '480p': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
            '360p': 'bestvideo[height<=360]+bestaudio/best[height<=360]'
        }

        ydl_opts = {
            'format': quality_format.get(quality, 'best'),
            'ffmpeg_location': 'C:\\ffmpeg\\bin\\ffmpeg.exe',
            'outtmpl': '%(title)s.%(ext)s'
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            downloaded_file = ydl.prepare_filename(info)
            
            # Convert if not mp4
            if not downloaded_file.endswith('.mp4'):
                self.convert_video(downloaded_file)

    def convert_video(self, input_file):
        output_file = os.path.splitext(input_file)[0] + '.mp4'
        ffmpeg_path = 'C:\\ffmpeg\\bin\\ffmpeg.exe'
        
        if input_file.lower().endswith('.webm'):
            command = [
                ffmpeg_path,
                '-i', input_file,
                '-c:v', 'copy',
                '-c:a', 'copy',
                output_file
            ]
        elif input_file.lower().endswith('.mkv'):
            command = [
                ffmpeg_path,
                '-i', input_file,
                '-c:v', 'copy',
                '-c:a', 'aac',
                '-strict', 'experimental',
                output_file
            ]
        else:
            return
        
        try:
            subprocess.run(command, check=True)
            os.remove(input_file)  # Remove original file
            return output_file
        except subprocess.CalledProcessError as e:
            raise Exception(f"Video conversion failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderGUI(root)
    root.mainloop()