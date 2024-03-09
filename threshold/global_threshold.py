# my_image_lib/threshold/global_threshold.py

def global_threshold(pixels, thresh):
    """
    Applies a global threshold to a grayscale image.
    Pixels >= thresh become 255, else 0.
    """
    height = len(pixels)
    width = len(pixels[0])

    output = [[0] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            output[y][x] = 255 if pixels[y][x] >= thresh else 0

    return output
# Add threshold module with global thresholding
# Add threshold module with global thresholding
