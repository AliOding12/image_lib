from image_lib.core.utils import convolution

def laplacian_filter(pixels):
    """
    Applies Laplacian filter for edge detection.
    """
    kernel = [[0, -1, 0],
              [-1, 4, -1],
              [0, -1, 0]]
    
    return convolution(pixels, kernel)
# Add Sobel and Laplacian edge detection filters
# Add Sobel and Laplacian edge detection filters
