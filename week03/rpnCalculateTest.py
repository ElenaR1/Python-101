#from unitTest import TestCase
# import unittest
# from message_to_numbers import message_to_numbers

# class TestMessageToNumbers(unittest.TaseCase):
#     def test_when_capital_letter_is_passed_then_return_one_and_its_numbers(self):
#         self.assertEquals(message_to_numbers('P'),[1,7])
#     def test_if_space_is_passed_then_zero_is_returned(self):
#         self.assertTrue(0 in message_to_numbers('I am'))
#     def test_when_two_consequitive_letters_on_one_key_then_minus_one_is_returned(self):
#         self.assertTrue(-1 in message_to_numbers('aa'))

# if __name__=='__main__':
#     unittest.main()

from rpnCalculate import rpn_calculate

import unittest

class TestRevrsePolishNotation(unittest.TestCase):
    def test_when_single_digit_is_passed_then_return_same_digit(self):
        number='45'
        expected_result=45
        self.assertEqual(rpn_calculate(number),expected_result)
    def test_when_two_numbers_Are_passed_then_Return_sum_of_them(self):
        expr='4 8 +'
        expected_result=12
        self.assertEqual(rpn_calculate(expr),expected_result)
    def test_when_substraction_of_two_numbers_then_return_differance(self):
        expr='7 3 -'
        expected_result=4
        self.assertEqual(rpn_calculate(expr),expected_result)
    def test_when_division_of_two_numbers_then_return_quotient(self):
        expr='24 4 /'
        expected_result=6
        self.assertEqual(rpn_calculate(expr),expected_result)
    def test_when_multiplication_of_two_numbers_then_return_product(self):
        expr='7 4 *'
        expected_result=28
        self.assertEqual(rpn_calculate(expr),expected_result)
    def test_when_sqrt_of_two_numbers_then_return_square_root(self):
        expr='144 SQRT'
        expected_result=12
        self.assertEqual(rpn_calculate(expr),expected_result)
    def test_a_more_complex_Expression(self):
        expr="3 20 4 6 + / *"
        expected_result=6
        self.assertEqual(rpn_calculate(expr),expected_result)


if __name__=='__main__':
     unittest.main()
