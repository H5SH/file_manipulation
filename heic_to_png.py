from PIL import Image
import os
from pillow_heif import register_heif_opener

def convert_heic_to_png(heic_path, png_path):
    register_heif_opener()
    try:
        with Image.open(heic_path) as heic_img:
            heic_img.convert('RGB').save(png_path, formate='PNG')
        # heic_img = HEIC2PNG(heic_path, quality=90)
        # heic_img.save(png_path, "PNG")
    except Exception as e:
        print(e)

heic_directory = "C:\H5SH\Other_Projects\image_rotation\heicImages"

png_directory = "C:\H5SH\Other_Projects\image_rotation\pngImages"

for file in os.listdir('C:\H5SH\Other_Projects\image_rotation\Images'):
    if file.endswith('.HEIC') or file.endswith('.heic'):
        heic_path = os.path.join(heic_directory, file)
        png_path = os.path.join(png_directory, os.path.splitext(file)[0] + ".png")
        convert_heic_to_png(heic_path, png_path) 


