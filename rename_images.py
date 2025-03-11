import os
import re

def rename_images(directory):
    for filename in os.listdir(directory):
        # Match filenames with query strings
        new_filename = re.sub(r'\?.*$', '', filename)
        if new_filename != filename:
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f'Renamed: {filename} to {new_filename}')

# Specify the directory containing the images
image_directory = './images'
rename_images(image_directory)
