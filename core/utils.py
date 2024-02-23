# my_image_lib/core/utils.py

def pad_image(pixels, pad_size, pad_value=0):
    """
    Pads the image with a constant value (default 0) on all sides.
    """
    height = len(pixels)
    width = len(pixels[0])
    padded = [[pad_value] * (width + 2 * pad_size) for _ in range(height + 2 * pad_size)]

    for y in range(height):
        for x in range(width):
            padded[y + pad_size][x + pad_size] = pixels[y][x]

    return padded


def convolution(pixels, kernel):
    """
    Applies convolution on a grayscale image using a given kernel (2D list).
    Assumes kernel is square and has odd dimensions.
    """
    height = len(pixels)
    width = len(pixels[0])
    k_size = len(kernel)
    pad_size = k_size // 2

    padded = pad_image(pixels, pad_size)
    output = [[0] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            total = 0
            for ky in range(k_size):
                for kx in range(k_size):
                    total += padded[y + ky][x + kx] * kernel[ky][kx]
            output[y][x] = max(0, min(255, int(total)))

    return output
# Add utility functions in core
