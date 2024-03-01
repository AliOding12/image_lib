
def rgb_to_grayscale(rgb_pixels):
    """
    Converts an RGB image (3D list) to grayscale (2D list).
    Formula: 0.299*R + 0.587*G + 0.114*B
    """
    height = len(rgb_pixels)
    width = len(rgb_pixels[0])
    gray_pixels = [[0] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            r, g, b = rgb_pixels[y][x]
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            gray_pixels[y][x] = gray

    return gray_pixels
# Add color to grayscale conversion
# Add color to grayscale conversion
