# filepath: src/pipeline/extract_frames.py
import ffmpeg
import os

def extract_frames(video_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    ffmpeg.input(video_path).output(f"{output_dir}/frame_%04d.png").run()

if __name__ == "__main__":
    extract_frames("data/input_video.mp4", "src/frames")