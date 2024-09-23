import yt_dlp
import argparse
import os

def download_video(video_url, quality, output_format):
    ydl_opts = {
        'format': quality,
        'outtmpl': f'downloads/%(title)s.%(ext)s',
        'merge_output_format': output_format if output_format else None,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def display_welcome_message():
    print("Welcome to the YouTube Downloader CLI!")
    print("You can download audio, video, or entire playlists.")
    print("Usage:")
    print("  python download.py [VIDEO_URL] [OPTIONS]")
    print("\nOptions:")
    print("  --audio              Download audio only.")
    print("  --video              Download video only (default).")
    print("  --playlist           Download the entire playlist.")
    print("  --quality QUALITY    Specify the quality (e.g., best, worst, 720).")
    print("  --output-format FORMAT Specify output format (mp4, mkv, webm, mp3).")
    print("\nExample:")
    print("  python download.py https://www.youtube.com/watch?v=example --video --quality 720")
    print("  python download.py https://www.youtube.com/playlist?list=example --playlist")

def main():
    parser = argparse.ArgumentParser(description="Download audio, video, or playlists from YouTube.")
    parser.add_argument('url', nargs='?', help='The URL of the video or playlist to download.')
    parser.add_argument('--audio', action='store_true', help='Download audio only.')
    parser.add_argument('--video', action='store_true', help='Download video only (default).')
    parser.add_argument('--playlist', action='store_true', help='Download the entire playlist.')
    parser.add_argument('--quality', type=str, default='best', help='Specify the quality (e.g., best, worst, 720p).')
    parser.add_argument('--output-format', type=str, choices=['mp4', 'mkv', 'webm', 'mp3'], help='Specify output format for merged files.')

    args = parser.parse_args()

    # Display welcome message if no URL is provided
    if not args.url:
        display_welcome_message()
        return

    # Create downloads directory if it doesn't exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    if args.audio:
        quality = 'bestaudio'
    elif args.video:
        quality = f'bestvideo[height<={args.quality}]' if args.quality.isdigit() else args.quality
    else:
        quality = f'best[height<={args.quality}]' if args.quality.isdigit() else 'best'

    if args.playlist:
        print("Downloading playlist...")
        download_video(args.url, quality, args.output_format)
    else:
        print("Downloading video/audio...")
        download_video(args.url, quality, args.output_format)

if __name__ == '__main__':
    main()
