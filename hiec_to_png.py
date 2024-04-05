from PIL import Image
import os
# import pyheif

def convert_heic_to_png(heic_path, png_path):
    try:
        # heic_file = pyheif.read(heic_path)
        heic_img = Image.open(heic_path)
        image = Image.frombytes(
            heic_img.mode, 
            heic_img.size, 
            heic_img.data,
            "raw",
            heic_img.mode,
            heic_img.stride,
        )
        heic_img.save(image, "PNG")
    except Exception as e:
        print(e)

heic_directory = "C:\H5SH\Other_Projects\image_rotation\data_set"

png_directory = "C:\H5SH\Other_Projects\image_rotation\pngImages"

for file in os.listdir('C:\H5SH\Other_Projects\image_rotation\data_set'):
    if file.endswith('.HEIC') or file.endswith('.heic'):
        heic_path = os.path.join(heic_directory, file)
        png_path = os.path.join(png_directory, os.path.splitext(file)[0] + ".png")
        convert_heic_to_png(heic_path, png_path) 


