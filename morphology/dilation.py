# my_image_lib/morphology/dilation.py

def dilation(pixels, struct_elem):
    """
    Performs binary/grayscale dilation on an image using the given structuring element.
    pixels: 2D list of integers (0–255)
    struct_elem: 2D list with 1s where the structure applies
    """
    height = len(pixels)
    width = len(pixels[0])
    k_size = len(struct_elem)
    pad_size = k_size // 2

    # Pad image with low values for dilation
    padded = [[0] * (width + 2 * pad_size) for _ in range(height + 2 * pad_size)]
    for y in range(height):
        for x in range(width):
            padded[y + pad_size][x + pad_size] = pixels[y][x]

    output = [[0] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            max_val = 0
            for ky in range(k_size):
                for kx in range(k_size):
                    if struct_elem[ky][kx] == 1:
                        val = padded[y + ky][x + kx]
                        if val > max_val:
                            max_val = val
            output[y][x] = max_val

    return output
# Add morphology module with dilation and erosion
# Add morphology module with dilation and erosion
# Add morphology module with dilation and erosion
