import yt_dlp


def download_youtube_video(url, output_path='videos'):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print('\nDownload completed successfully.')
        except yt_dlp.utils.DownloadError as e:
            print(f'\nError: {e}')


url = 'https://youtu.be/ICfGdpZCE1Q'

download_youtube_video(url, output_path='videos')
