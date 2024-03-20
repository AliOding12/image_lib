import unittest
from image_lib.transform import flip_horizontal, flip_vertical, rotate, scale, translate

class TestTransform(unittest.TestCase):
	def setUp(self):
		self.img = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9],
		]

	def test_flip_horizontal(self):
		result = flip_horizontal(self.img)
		self.assertEqual(result[0], [3, 2, 1])

	def test_flip_vertical(self):
		result = flip_vertical(self.img)
		self.assertEqual(result[0], [7, 8, 9])

	def test_rotate(self):
		result = rotate(self.img, 90)
		self.assertEqual(result[0][2], 1)

	def test_scale(self):
		result = scale(self.img, 2, 2)
		self.assertEqual(len(result), 2)
		self.assertEqual(len(result[0]), 2)

	def test_translate(self):
		result = translate(self.img, 1, 1)
		self.assertEqual(result[1][1], 1)

if __name__ == "__main__":
	unittest.main()
# Add tests for transform functions
# Add tests for transform functions
