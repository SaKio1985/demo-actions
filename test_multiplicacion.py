import unittest
from multiplicacion import multiplicacion

class TestMultiplicacion(unittest.TestCase):

    def test_multiplicar(self):
        self.assertEqual(multiplicacion(3,2), 6)
        self.assertEqual(multiplicacion(-1, 1), -1)
        self.assertEqual(multiplicacion(-1, -1), 1)

if __name__ == '__main__':
    unittest.main()