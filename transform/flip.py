# my_image_lib/transform/flip.py

def flip_horizontal(pixels):
    """
    Flips the image horizontally (mirror image).
    """
    return [list(reversed(row)) for row in pixels]

def flip_vertical(pixels):
    """
    Flips the image vertically.
    """
    return list(reversed(pixels))
# Add image flipping and rotation
# Add image flipping and rotation
