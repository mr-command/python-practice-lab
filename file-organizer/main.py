import os
import shutil

def organize_files(directory):
    DIR = os.listdir(directory)
    for filename in DIR:
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = filename.split('.')[-1]  # Get File Format
            folder_path = os.path.join(directory, file_extension)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))
            print("Your Files Ordered")

path = "D:"  # your directory
organize_files(path)
