# my_image_lib/transform/scale.py

def scale(pixels, new_width, new_height):
    """
    Resizes the image to (new_width, new_height) using nearest-neighbor interpolation.
    Works for grayscale (2D) or RGB (3D) images.
    """
    height = len(pixels)
    width = len(pixels[0])
    is_rgb = isinstance(pixels[0][0], list)

    output = [[([0,0,0] if is_rgb else 0) for _ in range(new_width)] for _ in range(new_height)]

    for y in range(new_height):
        for x in range(new_width):
            src_x = int(x * width / new_width)
            src_y = int(y * height / new_height)
            output[y][x] = pixels[src_y][src_x]

    return output
# Add transform module with scaling and translation
# Add transform module with scaling and translation
# Add transform module with scaling and translation
