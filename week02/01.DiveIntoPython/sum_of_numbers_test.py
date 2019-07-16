from sum_of_numbers import *
import unittest


class TestSumOfNumbers(unittest.TestCase):
    def test_when_no_numbers_then_Exception(self):
        with self.assertRaises(CustomError) as exc:
            sum_of_numbers("ab")
        self.assertTrue("no numbers" in str(exc.exception))

if __name__=='__main__':
    unittest.main()
