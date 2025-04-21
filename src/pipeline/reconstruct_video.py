# filepath: src/pipeline/reconstruct_video.py
import ffmpeg

def reconstruct_video(frames_dir, output_video):
    ffmpeg.input(f"{frames_dir}/frame_%04d.png", framerate=30).output(output_video).run()

if __name__ == "__main__":
    reconstruct_video("frames", "output_video.mp4")