import os
import sys
from pytube import YouTube
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-l', '--link', metavar='link', help='link to the YouTube video', required=True)
parser.add_argument('-n', '--name', metavar='name', help='name of the file', required=True)
parser.add_argument('-p', '--path', metavar='path', help='path for the pdf files', required=False)
parser.add_argument('-a', '--audio', metavar='audio', help='option arg to just download the audio', required=False)


def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")


if __name__ == "__main__":
    args = parser.parse_args()
    link = args.link
    name = args.name
    path = args.path

    if not path:
        path = os.getcwd()
    else:
        path = os.path.expanduser(path)

    yt = YouTube(link, on_progress_callback=on_progress)
    filesize = yt.streams.first().filesize
    if args.audio:
        file = yt.streams.get_audio_only()
        suffix = '.mp3'
    else:
        file = yt.streams.get_highest_resolution()
        suffix = '.mp4'
    file.download(output_path=path, filename=name+suffix)
