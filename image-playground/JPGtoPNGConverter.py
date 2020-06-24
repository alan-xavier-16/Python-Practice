import os
import sys
from PIL import Image, ImageFilter

img_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file in os.listdir(img_folder):
    filename, extension = os.path.splitext(file)
    try:
        input_folder_path = os.path.join(img_folder, filename)
        output_folder_path = os.path.join(output_folder, filename)
        with Image.open(f"{input_folder_path}{extension}") as img:
            img.save(f"{output_folder_path}.png", "png")
            print(f"{filename} converted from {extension} to PNG")
    except IOError:
        print(f"Cannot convert {filename}")
print("All Done!")