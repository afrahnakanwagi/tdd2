# test_factorial.py

import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)
        # self.assertEqual is used to check whether the method's output matches the expected result.
        self.assertEqual(factorial(3), 6)

# below the negative number number will raise an error since the negative for the factorial is not defined.
    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-5)

if __name__ == '__main__':
    # the statement below runs the tests when the code is executed.
    unittest.main()
