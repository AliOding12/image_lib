def adjust_contrast(pixels, factor):
    """
    Adjusts contrast by scaling pixel values around 128.
    factor > 1 increases contrast, 0 < factor < 1 decreases contrast.
    """
    if isinstance(pixels[0][0], list):  # RGB
        return [
            [[max(0, min(255, int((c - 128) * factor + 128))) for c in pixel]
             for pixel in row]
            for row in pixels
        ]
    else:  # Grayscale
        return [
            [max(0, min(255, int((pixel - 128) * factor + 128)))
             for pixel in row]
            for row in pixels
        ]
# Add manipulation module with brightness and contrast adjustments
# Add manipulation module with brightness and contrast adjustments
