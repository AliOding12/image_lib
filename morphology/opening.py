# my_image_lib/morphology/opening.py

from .erosion import erosion
from .dilation import dilation

def opening(pixels, struct_elem):
    """
    Performs opening: erosion followed by dilation.
    """
    eroded = erosion(pixels, struct_elem)
    opened = dilation(eroded, struct_elem)
    return opened
# Add morphological opening and closing
# Add morphological opening and closing
# Add morphological opening and closing
