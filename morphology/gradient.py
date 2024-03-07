# my_image_lib/morphology/gradient.py

from .erosion import erosion
from .dilation import dilation

def gradient(pixels, struct_elem):
    """
    Morphological gradient: difference between dilation and erosion.
    Works for grayscale/binary images represented as 2D lists (0-255).
    
    Returns a new 2D list where each pixel = dilation(pixels) - erosion(pixels),
    clamped to [0, 255].
    """
    dilated = dilation(pixels, struct_elem)
    eroded = erosion(pixels, struct_elem)

    height = len(pixels)
    width = len(pixels[0])
    output = [[0] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            val = dilated[y][x] - eroded[y][x]
            # clamp to valid range
            if val < 0:
                val = 0
            elif val > 255:
                val = 255
            output[y][x] = val

    return output
# Add morphological gradient
# Add morphological gradient
# Add morphological gradient
