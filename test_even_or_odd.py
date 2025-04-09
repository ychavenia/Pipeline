

import unittest
from even_or_odd import is_even


class TestEvenOrOdd(unittest.TestCase):

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(-1))
        self.assertTrue(is_even(-2))


if __name__ == '__main__':
    unittest.main()
