import unittest
from resta import resta

class TestResta(unittest.TestCase):

    def test_resta(self):
        self.assertEqual(resta(3,2), 1)
        self.assertEqual(resta(-1, 1), -2)
        self.assertEqual(resta(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()