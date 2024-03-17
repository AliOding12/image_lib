
from image_lib.filters.sobel_filter import sobel

def test_sobel():
    img = [
        [0, 0, 0],
        [0, 255, 0],
        [0, 0, 0]
    ]
    gx, gy = sobel(img)
    assert len(gx) == 3 and len(gy) == 3, "Sobel output size mismatch"
# Add tests for filters
# Add tests for filters
