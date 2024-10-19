import unittest

# Example function to be tested
def add(a, b):
    return a + b

# Test case using unittest
class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

# Running the tests
if __name__ == '__main__':
    unittest.main()
