# my_image_lib/threshold/adaptive_threshold.py

def adaptive_threshold(pixels, block_size, C):
    """
    Adaptive mean thresholding:
    For each pixel, threshold = mean of surrounding block - C
    If pixel > threshold, set to 255, else 0.
    """
    height = len(pixels)
    width = len(pixels[0])
    pad = block_size // 2

    output = [[0] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            # Compute mean of neighborhood
            total = 0
            count = 0
            for ky in range(-pad, pad + 1):
                for kx in range(-pad, pad + 1):
                    ny, nx = y + ky, x + kx
                    if 0 <= ny < height and 0 <= nx < width:
                        total += pixels[ny][nx]
                        count += 1
            mean = total / count

            output[y][x] = 255 if pixels[y][x] > (mean - C) else 0

    return output
# Add adaptive thresholding
# Add adaptive thresholding
