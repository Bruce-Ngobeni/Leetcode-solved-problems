import unittest
from three_sum import three_sum

class Test_Three_Sum(unittest.TestCase):

    def test_three_sum(self):
        self.assertEqual(three_sum([-1,0,1,2,-1,-4]),[[-1,-1,2],[-1,0,1]])
        self.assertEqual(three_sum([0,1,1]),[])
        self.assertEqual(three_sum([0,0,0]),[[0,0,0]])