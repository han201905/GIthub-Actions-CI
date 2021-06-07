import unittest
import example


class TestCase(unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_sub_1(self):
        self.assertEqual(example.subtract(1, 1), 0)

    def test_mul_1(self):
        self.assertEqual(example.multiply(2, 5), 10)

    def test_div_1(self):
        self.assertEqual(example.divide(5, 2), 2)


if __name__ == '__main__':
    unittest.main()
