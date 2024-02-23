# my_image_lib/core/io.py

def read_pgm(filename):
    """
    Reads a PGM (Portable Gray Map) image and returns a 2D list of pixel values.
    Only supports ASCII (P2) format.
    """
    with open(filename, 'r') as f:
        # Read magic number
        magic_number = f.readline().strip()
        if magic_number != 'P2':
            raise ValueError("Only ASCII PGM (P2) format is supported.")

        # Skip comments
        line = f.readline().strip()
        while line.startswith('#'):
            line = f.readline().strip()

        # Read width and height
        width, height = map(int, line.split())

        # Read max grayscale value
        max_val = int(f.readline().strip())
        if max_val > 255:
            raise ValueError("Only 8-bit PGM files are supported.")

        # Read pixel data
        pixels = []
        for _ in range(height):
            row = list(map(int, f.readline().strip().split()))
            pixels.append(row)

        return pixels


def write_pgm(filename, pixels):
 
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'w') as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write("255\n")
        for row in pixels:
            f.write(" ".join(map(str, row)) + "\n")
# Add core module with init and IO operations
