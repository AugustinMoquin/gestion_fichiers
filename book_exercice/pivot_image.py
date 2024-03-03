from PIL import Image

def rotate_image(input_path, output_path, angle):
    try:
        with Image.open(input_path) as img:
            rotated_img = img.rotate(angle, expand=True)
            
            rotated_img.save(output_path)
            
            print(f"Image rotated successfully and saved at {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main_rotate():
    input_image_path = "./img/image_1.jpg"
    output_image_path = "./img/rotated_image1.jpg"
    rotation_angle = 30

    rotate_image(input_image_path, output_image_path, rotation_angle)