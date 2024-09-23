# YouTube Downloader CLI

A simple command-line application for downloading audio, video, or entire playlists from YouTube using `yt-dlp`.

## Features

- Download audio only
- Download video only
- Download entire playlists
- Specify video quality (e.g., 720p, best)
- Choose output format (mp4, mkv, webm, mp3)

## Requirements

- Python 3.6 or higher
- `yt-dlp` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/youtube-downloader-cli.git
   cd youtube-downloader-cli

2. Install the required dependencies:

   ```bash
   pip install yt-dlp

## usauge
  Run the application using the following command:
  
  ```bash
  python download.py [VIDEO_URL] [OPTIONS]
  ```
```
Options
--audio: Download audio only.
--video: Download video only (default).
--playlist: Download the entire playlist.
--quality QUALITY: Specify the quality (e.g., best, worst, 720).
--output-format FORMAT: Specify output format (options: mp4, mkv, webm, mp3).
```

## Examples
Download a video at 720p:

  ```bash
  python download.py https://www.youtube.com/watch?v=example --video --quality 720
```
Download audio only:

  ```bash
  python download.py https://www.youtube.com/watch?v=example --audio
```
Download an entire playlist:
  ```bash
python download.py https://www.youtube.com/playlist?list=example --playlist
