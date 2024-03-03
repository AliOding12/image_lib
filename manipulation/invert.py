def invert(pixels):
    """
    Creates a negative of the image by inverting pixel values.
    Works for grayscale (0-255) or RGB images.
    """
    if isinstance(pixels[0][0], list):  # RGB image
        return [[[255 - c for c in pixel] for pixel in row] for row in pixels]
    else:  # Grayscale image
        return [[255 - pixel for pixel in row] for row in pixels]
# Add histogram equalization and image inversion
