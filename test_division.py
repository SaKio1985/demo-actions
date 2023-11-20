import unittest
from division import division

class TestDivision(unittest.TestCase):

    def test_division(self):
        self.assertEqual(division(3, 2), 1)
        self.assertEqual(division(-1, 1), -1)
        self.assertEqual(division(-1, -1), 1)

    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            division(5, 0)

if __name__ == '__main__':
    unittest.main()