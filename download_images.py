import csv
import requests
import os

# Define the CSV file path and the directory to save images
csv_file_path = '/Users/imac/Desktop/scrap_design_methods/scraped_data.csv'
images_dir = '/Users/imac/Desktop/scrap_design_methods/images'

# Create the images directory if it doesn't exist
os.makedirs(images_dir, exist_ok=True)

# Function to download an image from a URL
def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {save_path}")
    else:
        print(f"Failed to download: {url}")

# Read the CSV file and download each image
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    for row in csv_reader:
        image_url = row['Image Path']
        image_name = os.path.basename(image_url)
        save_path = os.path.join(images_dir, image_name)
        download_image(image_url, save_path)
