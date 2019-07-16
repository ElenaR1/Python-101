from is_number_balanced import *
import unittest


class TestIsNumberBalanced(unittest.TestCase):
    def test_if_number_has_one_digit_then_return_True(self):
        num=1
        expected_result=True 
        self.assertEqual(is_number_balanced(num),expected_result)
    def test_if_number_has_odd_number_of_digits_and_two_sums_are_equal(self):
        num=13522
        expected_result=True 
        self.assertEqual(is_number_balanced(num),expected_result)
    def test_if_number_has_odd_number_of_digits_and_two_sums_are_not_equal(self):
        num=13521
        expected_result=False 
        self.assertEqual(is_number_balanced(num),expected_result)

if __name__=='__main__':
    unittest.main()
