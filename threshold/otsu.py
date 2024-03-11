# my_image_lib/threshold/otsu.py

def otsu_threshold(pixels):
    """
    Computes an optimal threshold value using Otsu's method
    and applies binary thresholding.
    Works for grayscale images.
    """
    height = len(pixels)
    width = len(pixels[0])

    # Flatten pixel values
    flat = [p for row in pixels for p in row]

    # Histogram
    hist = [0] * 256
    for val in flat:
        hist[val] += 1

    total = height * width

    sum_total = sum(i * hist[i] for i in range(256))
    sum_bg = 0
    weight_bg = 0
    max_var = 0
    threshold = 0

    for t in range(256):
        weight_bg += hist[t]
        if weight_bg == 0:
            continue
        weight_fg = total - weight_bg
        if weight_fg == 0:
            break

        sum_bg += t * hist[t]
        mean_bg = sum_bg / weight_bg
        mean_fg = (sum_total - sum_bg) / weight_fg

        # Between-class variance
        var_between = weight_bg * weight_fg * (mean_bg - mean_fg) ** 2

        if var_between > max_var:
            max_var = var_between
            threshold = t

    # Apply threshold
    output = [[255 if pixels[y][x] >= threshold else 0 for x in range(width)]
              for y in range(height)]

    return output, threshold
# Add Otsu's automatic thresholding
# Add Otsu's automatic thresholding
