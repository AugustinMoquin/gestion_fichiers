import requests
from PIL import Image

def download_image(url, save_path):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded successfully and saved at {save_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")



def resize_image(input_path, output_path, new_size):
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Resize the image
            resized_img = img.resize(new_size)
            
            # Save the resized image
            resized_img.save(output_path)
            
            print(f"Image resized successfully and saved at {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main_image():


    image_url = "https://www.gutenberg.org/cache/epub/73079/pg73079.cover.medium.jpg"
    save_path = "./img/Henry_Jones.jpg"

    output_image_path = f"./img/resized_Henry_Jones.jpg"
    new_size = (300, 200)
    
    download_image(image_url, save_path)
    resize_image(save_path, output_image_path, new_size)
    
