import unittest
from image_lib.morphology import dilation, erosion, opening, closing, gradient

class TestMorphology(unittest.TestCase):
	def setUp(self):
		self.img = [
			[0, 0, 0, 0, 0],
			[0, 255, 255, 0, 0],
			[0, 255, 255, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
		]
		self.struct_elem = [
			[1, 1, 1],
			[1, 1, 1],
			[1, 1, 1],
		]

	def test_dilation(self):
		result = dilation(self.img, self.struct_elem)
		self.assertEqual(result[1][1], 255)
		self.assertEqual(result[0][0], 0)

	def test_erosion(self):
		result = erosion(self.img, self.struct_elem)
		self.assertEqual(result[2][2], 255)
		self.assertEqual(result[0][0], 0)

	def test_opening(self):
		result = opening(self.img, self.struct_elem)
		self.assertEqual(result[2][2], 255)

	def test_closing(self):
		result = closing(self.img, self.struct_elem)
		self.assertEqual(result[1][1], 255)

	def test_gradient(self):
		result = gradient(self.img, self.struct_elem)
		self.assertTrue(all(0 <= v <= 255 for row in result for v in row))

if __name__ == "__main__":
	unittest.main()
# Add tests for morphology operations
# Add tests for morphology operations
