from image_lib.core.utils import convolution
import math

def sobel_filter(pixels):
    """
    Applies Sobel edge detection and returns gradient magnitude.
    """
    Gx = [[-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1]]

    Gy = [[-1, -2, -1],
          [ 0,  0,  0],
          [ 1,  2,  1]]
    
    grad_x = convolution(pixels, Gx)
    grad_y = convolution(pixels, Gy)

    height = len(pixels)
    width = len(pixels[0])
    output = [[0] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            mag = int(math.sqrt(grad_x[y][x]**2 + grad_y[y][x]**2))
            output[y][x] = min(255, mag)
    
    return output
# Add Sobel and Laplacian edge detection filters
# Add Sobel and Laplacian edge detection filters
# Add Sobel and Laplacian edge detection filters
