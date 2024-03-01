
def adjust_brightness(pixels, value):
    """
    Adjusts brightness by adding 'value' to each pixel.
    Positive to increase brightness, negative to decrease.
    Clamps values between 0 and 255.
    """
    if isinstance(pixels[0][0], list):  # RGB
        return [
            [[max(0, min(255, c + value)) for c in pixel] for pixel in row]
            for row in pixels
        ]
    else:  # Grayscale
        return [
            [max(0, min(255, pixel + value)) for pixel in row]
            for row in pixels
        ]
# Add manipulation module with brightness and contrast adjustments
