import yt_dlp

def download_audio_channels(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(id)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])
        audio_channels = [f for f in formats if f.get('acodec')]
        print(audio_channels)

        for i, channel in enumerate(audio_channels):
            print(f"Baixando canal de áudio {i+1}...")
            ydl_opts['outtmpl'] = f"{info_dict['id']}_channel_{i+1}.wav"
            with yt_dlp.YoutubeDL(ydl_opts) as download_ydl:
                download_ydl.download([url])

url = "https://www.youtube.com/watch?v=xR21W_2AKhU"
download_audio_channels(url)
