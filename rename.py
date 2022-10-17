import os
from glob import glob
import argparse

def main():
    parser = argparse.ArgumentParser(prog="rename.py", description="Rename srt's to match video files")
    parser.add_argument('--ext', '--e', type=str, help="Specify video extension", required=True)
    
    args = parser.parse_args()

    video_ext = args.ext.replace('.', '')

    videos = glob(f"*.{video_ext}")
    if not videos:
        print(f"{video_ext} files not found.")
        return

    srts = glob("*.srt")
    if not srts:
        print(f".srt files not found.")
        return

    for i, vid in enumerate(videos):
        os.rename(srts[i], vid.replace(f".{video_ext}", ".srt"))

    print("Succesfully renamed srt's")

if __name__=="__main__":
    main()