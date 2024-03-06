# my_image_lib/morphology/closing.py

from .erosion import erosion
from .dilation import dilation

def closing(pixels, struct_elem):
    """
    Performs closing: dilation followed by erosion.
    """
    dilated = dilation(pixels, struct_elem)
    closed = erosion(dilated, struct_elem)
    return closed
# Add morphological opening and closing
