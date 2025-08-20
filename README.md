# image_lib: Python Image Processing Library

<div align="center">
  
[![Python Version][python-shield]][python-url]
[![License][license-shield]][license-url]
[![Tests][tests-shield]][tests-url]
[![Code Style][black-shield]][black-url]
[![Contributions Welcome][contributions-shield]][contributions-url]

A modular, pure Python library for basic image processing operations including filters, morphology, transforms, thresholding, and more.

[View Usage Examples](#usage) · [Report Bug](https://github.com/AliOding12/image_lib/issues) · [Request Feature](https://github.com/AliOding12/image_lib/issues)

</div>

---

## Table of Contents

- [About The Project](#about-the-project)
  - [What is this project?](#what-is-this-project)
  - [Why use this library?](#why-use-this-library)
  - [How does it work?](#how-does-it-work)
  - [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Basic Examples](#basic-examples)
  - [Available Modules](#available-modules)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

---

## About The Project

### What is this project?

`image_lib` is a modular and educational image processing library written in pure Python. It provides a collection of functions for manipulating and analyzing images, focusing on grayscale and simple RGB operations. The library is designed for learning, prototyping, and small-scale image processing tasks.

### Why use this library?

- **Educational**: Clear, readable code for learning image processing concepts
- **No Dependencies**: Pure Python implementation, no external libraries required
- **Modular**: Organized into logical submodules for easy navigation and use
- **Tested**: Includes comprehensive unit tests for core functionality
- **Well-Documented**: Clean code with detailed documentation
- **Lightweight**: Perfect for prototyping and educational purposes

### How does it work?

You can import and use the provided functions for various image processing tasks. Each submodule exposes its main functions via its `__init__.py`, so you can access them directly from the package.

### Features

#### **Filters**
- Gaussian Filter
- Laplacian Filter  
- Mean Filter
- Median Filter
- Sobel Edge Detection

#### **Morphological Operations**
- Dilation
- Erosion
- Opening
- Closing
- Morphological Gradient

#### **Image Manipulation**
- Brightness Adjustment
- Contrast Enhancement
- Grayscale Conversion
- Histogram Equalization
- Image Inversion

#### **Thresholding**
- Global Thresholding
- Adaptive Thresholding
- Otsu's Method

#### **Geometric Transforms**
- Image Flipping
- Rotation
- Scaling
- Translation

---

## Getting Started

### Prerequisites

- Python 3.6 or higher
- No additional dependencies required!

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AliOding12/image_lib.git
   cd image_lib
   ```

2. **Install the package (development mode)**
   ```bash
   pip install -e .
   ```

3. **Or install from PyPI (when available)**
   ```bash
   pip install image_lib
   ```

---

## Usage

### Basic Examples

```python
# Import the modules you need
from image_lib.filters import gaussian_filter, sobel_filter
from image_lib.morphology import dilation, erosion
from image_lib.transform import rotate, scale
from image_lib.manipulation import brightness, grayscale
from image_lib.threshold import otsu, adaptive_threshold

# Example 1: Apply Gaussian blur
blurred_image = gaussian_filter(image_pixels, size=5, sigma=1.5)

# Example 2: Edge detection with Sobel filter
edges = sobel_filter(grayscale_pixels)

# Example 3: Morphological operations
dilated = dilation(binary_image, kernel_size=3)
eroded = erosion(binary_image, kernel_size=3)

# Example 4: Image transformations
rotated = rotate(image_pixels, angle=45)
scaled = scale(image_pixels, scale_factor=1.5)

# Example 5: Brightness and contrast
brighter = brightness(image_pixels, factor=1.2)
gray = grayscale(rgb_pixels)

# Example 6: Thresholding
threshold_value = otsu(grayscale_pixels)
binary = adaptive_threshold(grayscale_pixels, block_size=11)
```

### Available Modules

| Module | Description | Key Functions |
|--------|-------------|---------------|
| `filters` | Image filtering operations | `gaussian_filter`, `laplacian_filter`, `mean_filter`, `median_filter`, `sobel_filter` |
| `morphology` | Morphological operations | `dilation`, `erosion`, `opening`, `closing`, `gradient` |
| `manipulation` | Basic image adjustments | `brightness`, `contrast`, `grayscale`, `histogram_equalization`, `invert` |
| `threshold` | Thresholding techniques | `global_threshold`, `adaptive_threshold`, `otsu` |
| `transform` | Geometric transformations | `flip`, `rotate`, `scale`, `translate` |
| `core` | Utility functions | I/O operations, helper functions |

---

## Project Structure

```
image_lib/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── io.py              # Image input/output operations
│   └── utils.py           # Utility functions
├── filters/
│   ├── __init__.py
│   ├── gaussian_filter.py # Gaussian blur implementation
│   ├── laplacian_filter.py# Laplacian edge detection
│   ├── mean_filter.py     # Mean/average filter
│   ├── median_filter.py   # Median filter for noise reduction
│   └── sobel_filter.py    # Sobel edge detection
├── manipulation/
│   ├── __init__.py
│   ├── brightness.py      # Brightness adjustment
│   ├── contrast.py        # Contrast enhancement
│   ├── grayscale.py       # Color to grayscale conversion
│   ├── histogram_equalization.py # Histogram equalization
│   └── invert.py          # Image inversion
├── morphology/
│   ├── __init__.py
│   ├── closing.py         # Morphological closing
│   ├── dilation.py        # Morphological dilation
│   ├── erosion.py         # Morphological erosion
│   ├── gradient.py        # Morphological gradient
│   └── opening.py         # Morphological opening
├── threshold/
│   ├── __init__.py
│   ├── adaptive_threshold.py # Adaptive thresholding
│   ├── global_threshold.py   # Global thresholding
│   └── otsu.py            # Otsu's automatic thresholding
├── transform/
│   ├── __init__.py
│   ├── flip.py            # Image flipping
│   ├── rotate.py          # Image rotation
│   ├── scale.py           # Image scaling
│   └── translate.py       # Image translation
├── tests/
│   ├── __init__.py
│   ├── test_filters.py    # Filter function tests
│   ├── test_io.py         # I/O function tests
│   ├── test_morphology.py # Morphology function tests
│   └── test_transform.py  # Transform function tests
├── README.md
├── requirements.txt
└── setup.py
```

---

## Testing

Run the test suite to ensure everything works correctly:

```bash
# Run all tests
python -m pytest tests/

# Run tests with coverage
python -m pytest tests/ --cov=image_lib

# Run specific test module
python -m pytest tests/test_filters.py
```

---

## Roadmap

- [x] Basic filtering operations
- [x] Morphological operations  
- [x] Image transformations
- [x] Thresholding algorithms
- [ ] Color image processing support
- [ ] Advanced filters (bilateral, non-local means)
- [ ] Image I/O for common formats (PNG, JPEG)
- [ ] Performance optimizations
- [ ] Visualization utilities
- [ ] Documentation website

See the [open issues](https://github.com/AliOding12/image_lib/issues) for a full list of proposed features and known issues.

---

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork the Project**
2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/image_lib.git
cd image_lib

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Install development dependencies
pip install pytest pytest-cov black flake8

# Run tests
pytest tests/
```

---

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

---

## Contact

**Abbas Ali** - [abbasali1214313@gmail.com](mailto:abbasali1214313@gmail.com)

**Project Link**: [https://github.com/AliOding12/image_lib](https://github.com/yourusername/image_lib)



---

## Acknowledgments

- Python community for inspiration and support
- [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template) for the README structure
- Open source image processing algorithms and research papers
- Contributors and users of this library

---

<div align="center">

**⭐ Star this repository if you found it helpful! ⭐**

[Report Bug](https://github.com/AliOding12/image_lib/issues) · [Request Feature](https://github.com/AliOding12/image_lib/issues) · [Contribute](#contributing)

</div>

<!-- MARKDOWN LINKS & IMAGES -->
[python-shield]: https://img.shields.io/badge/python-3.6+-blue.svg?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[license-shield]: https://img.shields.io/github/license/AliOding12/image_lib.svg?style=for-the-badge
[license-url]: https://github.com/AliOding12/image_lib/blob/main/LICENSE.txt
[tests-shield]: https://img.shields.io/badge/tests-passing-brightgreen.svg?style=for-the-badge
[tests-url]: https://github.com/AliOding12/image_lib/actions
[black-shield]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
[black-url]: https://github.com/psf/black
[contributions-shield]: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=for-the-badge
[contributions-url]: #contributing<!-- Initial commit: Set up project with README, setup.py, requirements.txt and .gitignore -->
<!-- Update README with usage examples and documentation -->
