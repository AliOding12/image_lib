
def erosion(pixels, struct_elem):
  
    height = len(pixels)
    width = len(pixels[0])
    k_size = len(struct_elem)
    pad_size = k_size // 2

    padded = [[255] * (width + 2 * pad_size) for _ in range(height + 2 * pad_size)]
    for y in range(height):
        for x in range(width):
            padded[y + pad_size][x + pad_size] = pixels[y][x]

    output = [[0] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            min_val = 255
            for ky in range(k_size):
                for kx in range(k_size):
                    if struct_elem[ky][kx] == 1:
                        val = padded[y + ky][x + kx]
                        if val < min_val:
                            min_val = val
            output[y][x] = min_val

    return output
# Add morphology module with dilation and erosion
# Add morphology module with dilation and erosion
