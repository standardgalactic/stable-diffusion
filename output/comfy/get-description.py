import os
from PIL import Image
from clip_interrogator import Config, Interrogator

image_dir = "."

# Use smaller model for speed
ci = Interrogator(Config(
    clip_model_name="ViT-L-14/openai",       # Or "ViT-B-16/openai" for faster CLIP
    caption_model_name="blip-base"          
))

with open("description.txt", "w") as output_file:

    def process_image(image_path):
        image = Image.open(image_path).convert('RGB')
        result = ci.interrogate(image)
        return result

    for filename in os.listdir(image_dir):
        if filename.lower().endswith(('.jpg', '.png')):
            image_path = os.path.join(image_dir, filename)
            message = f"Processing {filename}..."
            print(message)
            output_file.write(message + "\n")
            output_file.flush()

            result = process_image(image_path)

            message = f"Results for {filename}: {result}"
            print(message)
            output_file.write(message + "\n")
            output_file.flush()

