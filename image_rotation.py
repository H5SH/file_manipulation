from PIL import Image
import os


def rotate_and_save(img, save_path_prefix, number):
    for angle in [0, 90, 180, 270]:
        rotated_img = img.rotate(angle, expand=True)
        save_path = f"{save_path_prefix}_rotated_{angle}_{number}Image.png"
        rotated_img.save(save_path)


def open_images_in_directory(directory):
    files = os.listdir(directory)

    image_files = [file for file in files if file.lower().endswith(('.jpg', 'jpeg', '.png'))]
    count = 0

    for image_file in image_files:
        image_path = os.path.join(directory, image_file)
        img = Image.open(image_path)
        rotate_and_save(img, 'C:/H5SH/Other_Projects/image_rotation/rotated_img/', count)
        count += 1

open_images_in_directory('C:\H5SH\Other_Projects\image_rotation\Images')