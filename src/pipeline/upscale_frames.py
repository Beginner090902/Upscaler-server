# filepath: src/pipeline/upscale_frames.py
import os
from realesrgan import RealESRGAN
from PIL import Image

def upscale_frames(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    model = RealESRGAN('cuda', scale=4)
    model.load_weights('weights/RealESRGAN_x4plus_anime_6B.pth')  # Anime-optimiertes Modell

    for frame in os.listdir(input_dir):
        input_path = os.path.join(input_dir, frame)
        output_path = os.path.join(output_dir, frame)

        # Öffne das Bild, um die Auflösung zu überprüfen
        with Image.open(input_path) as img:
            width, height = img.size

            # Dynamische Anpassung der Auflösung
            if width <= 1920 and height <= 1920:
                # Bild hochskalieren, um die maximale Breite oder Höhe von 1920 zu erreichen
                scale_factor = min(1920 / width, 1920 / height)
                new_width = int(width * scale_factor)
                new_height = int(height * scale_factor)
                img = img.resize((new_width, new_height), Image.LANCZOS)
                img.save(input_path)  # Temporär speichern, um den Upscaler zu verwenden

            # Kosmetische Verbesserung durch den Upscaler
            model.predict(input_path, output_path)

        # Lösche das ursprüngliche Bild nach dem Upscaling
        os.remove(input_path)

if __name__ == "__main__":
    upscale_frames("src/frames", "src/upscaled_frames")