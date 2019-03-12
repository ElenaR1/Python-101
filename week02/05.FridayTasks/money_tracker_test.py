from money_tracker import *

import unittest

class TestMoneyTracker(unittest.TestCase):
    def test_show_user_incomes(self):
        all_user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result=[(10, 'Deposit'), (700, 'Salary'), (50, 'Savings')]
        self.assertEqual(show_user_incomes(all_user_data),expected_result)
    def test_show_user_expenses(self):
        all_user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result=[(10, 'Deposit'), (700, 'Salary'), (50, 'Savings')]
        self.assertEqual(show_user_incomes(all_user_data),expected_result)
    def test_show_user_data_per_date(self):
        all_user_data = {'22-03-2019': {'New Income': [(760.0, 'Salary')], 'New Expense': [(5.5, 'Eating Out'), (34.0, 'Clothes'), (41.79, 'Food'), (12.0, 'Eating Out'), (7.0, 'House'), (14.0, 'Pets'), (112.4, 'Bills'), (21.5, 'Transport')]}, '23-03-2019': {'New Income': [(50.0, 'Savings'), (200.0, 'Deposit')], 'New Expense': [(15.0, 'Food'), (5.0, 'Sports')]}}
        expected_result=[(5.5, 'Eating Out'), (34.0, 'Clothes'), (41.79, 'Food'), (12.0, 'Eating Out'), (7.0, 'House'), (14.0, 'Pets'), (112.4, 'Bills'), (21.5, 'Transport'), (15.0, 'Food'), (5.0, 'Sports')]
        self.assertEqual(show_user_expenses(all_user_data),expected_result)
    def test_list_user_expenses_ordered_by_categories(self):
        all_user_data = {'22-03-2019': {'New Income': [(760.0, 'Salary')], 'New Expense': [(5.5, 'Eating Out'), (34.0, 'Clothes'), (41.79, 'Food'), (12.0, 'Eating Out'), (7.0, 'House'), (14.0, 'Pets'), (112.4, 'Bills'), (21.5, 'Transport')]}, '23-03-2019': {'New Income': [(50.0, 'Savings'), (200.0, 'Deposit')], 'New Expense': [(15.0, 'Food'), (5.0, 'Sports')]}}
        expected_result=[(112.4, 'Bills'), (34.0, 'Clothes'), (5.5, 'Eating Out'), (12.0, 'Eating Out'), (41.79, 'Food'), (15.0, 'Food'), (7.0, 'House'), (14.0, 'Pets'), (5.0, 'Sports'), (21.5, 'Transport')]

        self.assertEqual(list_user_expenses_ordered_by_categories(all_user_data),expected_result)
    def test_list_income_categories(self):
        all_user_data = {'22-03-2019': {'New Income': [(760.0, 'Salary')], 'New Expense': [(5.5, 'Eating Out'), (34.0, 'Clothes'), (41.79, 'Food'), (12.0, 'Eating Out'), (7.0, 'House'), (14.0, 'Pets'), (112.4, 'Bills'), (21.5, 'Transport')]}, '23-03-2019': {'New Income': [(50.0, 'Savings'), (200.0, 'Deposit')], 'New Expense': [(15.0, 'Food'), (5.0, 'Sports')]}}
        expected_result=['Deposit', 'Salary', 'Savings']
        self.assertEqual(list_income_categories(all_user_data),expected_result)

    

if __name__=='__main__':
     unittest.main()