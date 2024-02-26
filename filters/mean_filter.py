from image_lib.core.utils import convolution

def mean_filter(pixels, size=3):
    """
    Applies a mean filter (average blur) to a grayscale image.
    size: odd integer (3, 5, 7, etc.)
    """
    if size % 2 == 0:
        raise ValueError("Kernel size must be odd.")
    
    kernel = [[1 / (size * size) for _ in range(size)] for _ in range(size)]
    return convolution(pixels, kernel)
# Add mean and median filters for noise reduction
