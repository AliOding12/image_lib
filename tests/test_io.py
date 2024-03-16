# tests/test_io.py
import os
from image_lib.core.io import write_pgm, read_pgm

def test_pgm_read_write():
    img = [
        [0, 128, 255],
        [255, 128, 0],
        [50, 100, 150]
    ]
    write_pgm("test.pgm", img)
    read_img = read_pgm("test.pgm")
    assert img == read_img, "PGM read/write mismatch"
    os.remove("test.pgm")
# Start tests module with IO tests
# Start tests module with IO tests
