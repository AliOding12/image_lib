# my_image_lib/transform/translate.py

def translate(pixels, dx, dy):
    """
    Translates (shifts) the image by (dx, dy).
    Empty space is filled with black.
    Works for grayscale or RGB.
    """
    height = len(pixels)
    width = len(pixels[0])
    is_rgb = isinstance(pixels[0][0], list)

    output = [[([0,0,0] if is_rgb else 0) for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < width and 0 <= new_y < height:
                output[new_y][new_x] = pixels[y][x]

    return output
# Add transform module with scaling and translation
