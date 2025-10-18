import numpy as np
from PIL import Image
import random

def generate_random_walk_image(width=800, height=800, num_steps=1000000000):
    """
    Generate an image using a random walk algorithm.

    Parameters:
    - width: Canvas width in pixels
    - height: Canvas height in pixels
    - num_steps: Number of random walk steps to perform (default 1 billion)
    """
    # Initialize canvas with black background
    canvas = np.zeros((height, width, 3), dtype=np.uint8)

    # Start from the center
    x = width // 2
    y = height // 2

    # Initial color (start with middle gray)
    color = np.array([128, 128, 128], dtype=np.int16)

    print(f"Generating walk: {width}x{height} with {num_steps} steps")

    for step in range(num_steps):
        # Set current pixel to current color
        canvas[y, x] = np.clip(color, 0, 255).astype(np.uint8)

        # Randomly choose to move in x or y direction (50-50 probability)
        if random.random() < 0.5:
            # Move in x direction
            dx = random.choice([-1, 1])
            x = np.clip(x + dx, 0, width - 1)
        else:
            # Move in y direction
            dy = random.choice([-1, 1])
            y = np.clip(y + dy, 0, height - 1)

        # Update color
        color[0] += random.choice([-1, 1])  # Red
        color[1] += random.choice([-1, 1])  # Green
        color[2] += random.choice([-1, 1])  # Blue

        # Clip color values to valid RGB range [0, 255]
        color = np.clip(color, 0, 255)

        # Progress
        if (step + 1) % 100000 == 0:
            print(f"Progress: {step + 1}/{num_steps} steps completed")

    print("Random walk complete! Creating image...")
    return canvas

def main():
    # Generate image
    canvas = generate_random_walk_image(width=800, height=800, num_steps=1000000000)

    # Convert to PIL Image,save
    img = Image.fromarray(canvas, 'RGB')
    img.save('random_walk_output.png')
    print("Image saved as 'random_walk_output.png'")

if __name__ == "__main__":
    main()
