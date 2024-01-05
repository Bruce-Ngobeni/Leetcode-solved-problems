import unittest 
from max_area import maxArea

class TestMaxArea(unittest.TestCase):

    def test_max_area(self):

        self.assertEqual(maxArea([1,8,6,2,5,4,8,3,7]),49)
        self.assertEqual(maxArea([1,1]),1)


if __name__ == "__main__":
    unittest.main()