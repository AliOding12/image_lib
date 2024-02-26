from image_lib.core.utils import pad_image

def median_filter(pixels, size=3):
    """
    Applies median filtering to remove salt & pepper noise.
    """
    if size % 2 == 0:
        raise ValueError("Kernel size must be odd.")
    
    height = len(pixels)
    width = len(pixels[0])
    pad_size = size // 2
    padded = pad_image(pixels, pad_size)
    output = [[0] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            window = []
            for ky in range(size):
                for kx in range(size):
                    window.append(padded[y + ky][x + kx])
            output[y][x] = sorted(window)[len(window) // 2]
    
    return output
# Add mean and median filters for noise reduction
