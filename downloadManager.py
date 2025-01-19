import yt_dlp
import subprocess
import os
import re

class DownloadManager:
    def __init__(self):
        self.url = None
        self.out = "downloading"

        self.ydl_opts = {
            'quiet': True,
            'extract_flat': True,
        }

    def download(self, url, out, format, audio_ext=None):
        video_links = []
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            result = ydl.extract_info(url, download=False)
            if 'entries' in result:
                for video in result['entries']:
                    video_links.append(video['url'])
                for video in video_links:
                    if format == 'VIDEO':
                        self.downloadVideo(video, out)
                    elif format == 'AUDIO':
                        self.downloadAudio(video, out, audio_ext)
            else:
                if format == 'VIDEO':
                    self.downloadVideo(url, out)
                elif format == 'AUDIO':
                    self.downloadAudio(url, out, audio_ext)
    
    def downloadVideo(self, url, out):
        self.url = url
        self.out = out

        self.video_opts = {
            'format': 'bestvideo/best',
            'outtmpl': f'{self.out}/%(title)s_video.%(ext)s',
        }
        self.audio_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{self.out}/%(title)s_audio.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }],
        }

        with yt_dlp.YoutubeDL(self.video_opts) as video_ydl:
            video_info_dict = video_ydl.extract_info(self.url, download=True)
            video_file = video_ydl.prepare_filename(video_info_dict)

        with yt_dlp.YoutubeDL(self.audio_opts) as audio_ydl:
            audio_info_dict = audio_ydl.extract_info(self.url, download=True)
            ext = audio_info_dict['ext']
            audio_file = audio_ydl.prepare_filename(audio_info_dict).replace('.'+ext, '.wav')

        safe_title = re.sub(r'[<>:"/\\|?*]', '_', video_info_dict["title"])
        output_file = f'{self.out}/{safe_title}.mp4'

        subprocess.run([
            'ffmpeg', 
            '-i', video_file, 
            '-i', audio_file, 
            '-c:v', 'copy', 
            '-c:a', 'aac', 
            '-strict', 'experimental', 
            output_file,
        ])

        if os.path.exists(video_file):
            os.remove(video_file)
        if os.path.exists(audio_file):
            os.remove(audio_file)

        os.startfile(self.out)

    def downloadAudio(self, url, out, audio_ext):
        self.url = url
        self.out = out

        self.audio_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{self.out}/%(title)s_audio.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': audio_ext,
            }],
        }

        with yt_dlp.YoutubeDL(self.audio_opts) as audio_ydl:
            audio_info_dict = audio_ydl.extract_info(self.url, download=True)

        os.startfile(self.out)