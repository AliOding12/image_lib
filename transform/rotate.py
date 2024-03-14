# my_image_lib/transform/rotate.py
import math

def rotate(pixels, angle):
    """
    Rotates the image by 'angle' degrees using nearest-neighbor interpolation.
    Works for grayscale (2D) or RGB (3D) images.
    """
    height = len(pixels)
    width = len(pixels[0])

    # Check if RGB or grayscale
    is_rgb = isinstance(pixels[0][0], list)

    # Convert angle to radians
    rad = math.radians(angle)

    # Center of image
    cx, cy = width / 2, height / 2

    # Create output image (same size)
    output = [[([0,0,0] if is_rgb else 0) for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            # Coordinates relative to center
            xt = x - cx
            yt = y - cy

            # Apply inverse rotation
            src_x =  xt * math.cos(rad) + yt * math.sin(rad) + cx
            src_y = -xt * math.sin(rad) + yt * math.cos(rad) + cy

            # Nearest neighbor
            src_x = int(round(src_x))
            src_y = int(round(src_y))

            if 0 <= src_x < width and 0 <= src_y < height:
                output[y][x] = pixels[src_y][src_x]

    return output
# Add image flipping and rotation
# Add image flipping and rotation
# Add image flipping and rotation
