# YouTube Downloader

A simple and user-friendly YouTube downloader with GUI interface built using Python. This application allows users to download YouTube content in various formats including video (MP4), audio (MP3), and subtitles.

## Features

- **Multiple Download Options:**
  - Video download (MP4 format)
  - Audio download (MP3 format)
  - Subtitle download (TXT format)

- **Video Quality Selection:**
  - Supports multiple resolutions: 2160p, 1440p, 1080p, 720p, 480p, 360p
  - Automatic format conversion to MP4

- **Subtitle Options:**
  - Multiple language support (English, Chinese, Japanese, Korean)
  - Auto-generated subtitles support

- **User-Friendly Interface:**
  - Simple and intuitive GUI
  - Download progress indication
  - Error handling with user notifications

## Prerequisites

Before running the application, make sure you have the following installed:

1. Python 3.6 or higher
2. Required Python packages:   ```
   pip install yt-dlp tkinter   ```
3. FFmpeg:
   - Download FFmpeg from https://github.com/BtbN/FFmpeg-Builds/releases
   - Download the latest "ffmpeg-master-latest-win64-gpl.zip" release
   - Extract the zip file
   - Rename the extracted folder to "ffmpeg"
   - Move the "ffmpeg" folder to C:\ drive (final path should be C:\ffmpeg)
   - Verify that C:\ffmpeg\bin\ffmpeg.exe exists and is accessible
   - (Optional) Add C:\ffmpeg\bin to system PATH environment variable for command line usage

## Installation

1. Clone this repository:   ```bash
   git clone https://github.com/song2li/youtube-downloader.git   ```

2. Navigate to the project directory:   ```bash
   cd youtube-downloader   ```

3. Run the application:   ```bash
   python "youtube download.py"   ```

## Usage

1. Launch the application
2. Enter a YouTube URL in the input field
3. Select the desired download type (Video/Audio/Subtitle)
4. Choose quality settings if applicable
5. Click the "Download" button
6. Wait for the download to complete

## Note

- The downloaded files will be saved in the same directory as the script
- Video downloads are automatically converted to MP4 format if necessary
- Make sure you have a stable internet connection for better download experience

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for the YouTube download functionality
- [FFmpeg](https://ffmpeg.org/) for media processing capabilities

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 
