import pytube
import os

from pytube import YouTube

def download_youtube_video(url, output_folder='Assets'):
    try:
        # Create YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Set the output file path
        output_path = f"{output_folder}/{yt.title}.mp4"

        # Download the video
        print(f"Downloading {yt.title}...")
        video_stream.download(output_folder)

        print(f"Download complete! Video saved at {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
youtube_url = "https://www.youtube.com/watch?v=D5R-TaU9cZU"
download_youtube_video(youtube_url)