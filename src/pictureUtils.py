import os
from PIL import Image

def process_image(input_path, output_path, mode):
    if not os.path.isfile(input_path):
        print(f"Error: The file {input_path} does not exist.")
        return

    image = Image.open(input_path).convert("RGBA")
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            if a != 0:
                if mode == 1:
                    pixels[x, y] = (255, 255, 255, a)
                elif mode == 2:
                    pixels[x, y] = (0, 0, 0, a)
                elif mode == 3:
                    threshold = 60
                    color_distance = ((r - 0) ** 2 + (g - 0) ** 2 + (b - 0) ** 2) ** 0.5
                    if color_distance > threshold:
                        pixels[x, y] = (0, 0, 0, 0)
    image.save(output_path)
    print(f"Processed image saved to {output_path}")
def main():
    input_image_path = "input/input.png"
    output_image_path = "output/output.png"

    print("Select processing mode:")
    print("1 - Change non-transparent pixels to white")
    print("2 - Change non-transparent pixels to black")
    print("3 - Make every pixel that isn't black or related to black transparent")
    mode = input("Enter the mode number (1, 2, or 3): ")
    if mode not in {'1', '2', '3'}:
        print("Invalid mode selected. Please choose 1, 2, or 3.")
        return
    mode = int(mode)
    process_image(input_image_path, output_image_path, mode)

if __name__ == "__main__":
    main()
