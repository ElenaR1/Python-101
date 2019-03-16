from fractions import simplify_fraction,collect_fractions,sort_fractions

class CustomError(Exception):
    pass

import unittest

# class ValidationError(Exception):
#     pass

class TestFractions(unittest.TestCase):
    def test_when_nominator_and_denominator_are_equal_then_return_one_one(self):
        tpl=(5,5)
        expected_result=(1,1)
        self.assertEqual(simplify_fraction(tpl),expected_result)
    def test_when_denominator_is_one_then_return__nominator_one(self):
        tpl=(5,1)
        expected_result=(5,1)
        self.assertEqual(simplify_fraction(tpl),expected_result)
    def test_validate_fraction_object_is_a_tuple(self):
        #self.assertRaises(ValidationError,simplify_fraction,(1,2))
        with self.assertRaises(Exception) as exc:
            simplify_fraction([1,2])
        print(str(exc.exception))
        self.assertTrue('not a tuple' in str(exc.exception))
    def test_validate_denominator_is_not_zero(self):
        #self.assertRaises(ValidationError,simplify_fraction,(1,2))
        with self.assertRaises(CustomError) as exc:
            simplify_fraction((1,0))
        print(str(exc.exception))
        self.assertTrue('you should use another denominator' in str(exc.exception))
    def test_sum_of_two_fractions(self):
        tpl1=(1,7)
        tpl2=(2,6)
        expected_result=(10,21)
        self.assertEqual(collect_fractions((tpl1,tpl2)),expected_result)
    def test_sort_of_fractions(self):
        arr=[(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
        expected_result=[(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]
        self.assertEqual(sort_fractions(arr),expected_result)


if __name__=='__main__':
     unittest.main()
