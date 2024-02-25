from image_lib.core.utils import convolution
import math

def gaussian_kernel(size=3, sigma=1.0):
    """
    Generates a Gaussian kernel.
    """
    kernel = [[0] * size for _ in range(size)]
    center = size // 2
    total = 0.0
    
    for y in range(size):
        for x in range(size):
            exponent = -((x - center)**2 + (y - center)**2) / (2 * sigma**2)
            kernel[y][x] = math.exp(exponent) / (2 * math.pi * sigma**2)
            total += kernel[y][x]
    
    # Normalize
    for y in range(size):
        for x in range(size):
            kernel[y][x] /= total

    return kernel

def gaussian_filter(pixels, size=3, sigma=1.0):
    """
    Applies Gaussian blur to a grayscale image.
    """
    kernel = gaussian_kernel(size, sigma)
    return convolution(pixels, kernel)
# Start filters module with Gaussian blur
# Fix bug in Gaussian filter implementation
# Start filters module with Gaussian blur
# Fix bug in Gaussian filter implementation
# Start filters module with Gaussian blur
