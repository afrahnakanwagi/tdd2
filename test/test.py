import unittest

# Example function to be tested
def multiply(a, b):
    return a * b

# Test case using unittest
class TestMultiply(unittest.TestCase):
    def test_multiply_numbers(self):
        self.assertEqual(multiply(1, 1), 1)
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(3, 3), 9)
        self.assertEqual(multiply(4, 4), 16)    
        self.assertEqual(multiply(23, 25), 23*45)

# Running the tests
if __name__ == '__main__':
    unittest.main()
