def histogram_equalization(pixels):
    """
    Performs histogram equalization to improve image contrast.
    Only works on grayscale images (2D list).
    """
    height = len(pixels)
    width = len(pixels[0])

    # Flatten the pixel list
    flat = [p for row in pixels for p in row]

    # Calculate histogram
    hist = [0] * 256
    for val in flat:
        hist[val] += 1

    # Compute cumulative distribution function (CDF)
    cdf = [0] * 256
    cdf[0] = hist[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + hist[i]

    # Normalize the CDF
    cdf_min = min([c for c in cdf if c > 0])
    total_pixels = height * width
    mapping = [0] * 256
    for i in range(256):
        mapping[i] = int((cdf[i] - cdf_min) / (total_pixels - cdf_min) * 255)

    # Map original pixels
    equalized = [
        [mapping[pixels[y][x]] for x in range(width)]
        for y in range(height)
    ]

    return equalized
# Add histogram equalization and image inversion
