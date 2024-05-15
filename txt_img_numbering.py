import os
import glob

def rename_img_files(directory):
    # Change to the specified directory
    os.chdir(directory)
    
    # Find all .png files in the directory
    png_files = glob.glob('*.png')
    
    # Sort files to ensure consistent renaming order
    png_files.sort()
    
    # Rename each file
    for index, filename in enumerate(png_files):
        new_name = f"{index + 1}.png"
        os.rename(filename, new_name)
        print(f"Renamed {filename} to {new_name}")



def rename_txt_files(directory):
    # Change to the specified directory
    os.chdir(directory)
    
    # Find all .png files in the directory
    png_files = glob.glob('*.txt')
    
    # Sort files to ensure consistent renaming order
    png_files.sort()
    
    # Rename each file
    for index, filename in enumerate(png_files):
        new_name = f"{index + 1}.txt"
        os.rename(filename, new_name)
        print(f"Renamed {filename} to {new_name}")

# Specify the directory containing the .png files
img_directory_path = 'C:/H5SH/Other_Projects/Ai-Attendance-System/train/images'
txt_directory_path = 'C:/H5SH/Other_Projects/Ai-Attendance-System/train/labels'
# rename_txt_files(txt_directory_path)
rename_img_files(img_directory_path)


