from parse_money_tracker_data import *
from aggregated_money_tracker import *
import operator
from operator import itemgetter
class MoneyTracker:
    def __init__(self,AggregatedObject):
        self.AggregatedObject=AggregatedObject
    def list_user_data(self):
        for keys, values in self.AggregatedObject.all_user_data.items():
            print ("key: ",  keys)
            #print ("values: " , values)
            for keys1, values1 in self.AggregatedObject.all_user_data[keys].items():
                print ("key1: " , keys1)
                print ("values1: ", values1)
    def add_income(self,inc):
       self.AggregatedObject.incomes.append(inc) 
    def add_expense(self,exp):
       self.AggregatedObject.expenses.append(exp) 
    def show_user_data_per_date(self,date):
        for el in self.AggregatedObject.incomes:
            if el.date==date:
                print(el)
        for el in self.AggregatedObject.expenses:
            if el.date==date:
                print(el)
    def show_user_expenses(self,all_user_data):
        expense_array=[]
        for keys, values in self.AggregatedObject.all_user_data.items():
            for keys1, values1 in all_user_data[keys].items():
                if keys1=='New Expense' or keys1=='expense':               
                    for i in range(len(values1)):
                        expense_array.append(values1[i])
        return expense_array
    def list_user_expenses_ordered_by_categories(self):
        expense_list=self.show_user_expenses(self.AggregatedObject.all_user_data)
        #print(expense_list)
        expense_list.sort(key = operator.itemgetter(1))
        return expense_list




def main():
    a=AggregatedObject()
    #arr={'22-03-2019': {'New Income': [(760.0, 'Salary')], 'New Expense': [(5.5, 'Eating Out'), (34.0, 'Clothes'), (41.79, 'Food'), (12.0, 'Eating Out'), (7.0, 'House'), (14.0, 'Pets'), (112.4, 'Bills'), (21.5, 'Transport')]}, '23-03-2019': {'New Income': [(50.0, 'Savings'), (200.0, 'Deposit')], 'New Expense': [(15.0, 'Food'), (5.0, 'Sports')]}}
    arr=['=== 22-03-2019 ===\n', '760, Salary, New Income\n', '5.5, Eating Out, New Expense\n', '34, Clothes, New Expense\n', '41.79, Food, New Expense\n', '12, Eating Out, New Expense\n', '7, House, New Expense\n', '14, Pets, New Expense\n', '112.40, Bills, New Expense\n', '21.5, Transport, New Expense\n', '=== 23-03-2019 ===\n', '50, Savings, New Income\n', '15, Food, New Expense\n', '200, Deposit, New Income\n', '5, Sports, New Expense']
    my_dict=process_dict(arr)
    a.process(my_dict)
    mt=MoneyTracker(a)
    for el in mt.AggregatedObject.incomes:
        print(el)
    inc=Income(100,'lottery','22-03-2019')
    mt.add_income(inc)
    print('INCOMES')
    for el in mt.AggregatedObject.incomes:
        print(el)

    #     print(el)
    # print('INCOMES')
    # for el in a.incomes:
    #     print(el)
    # print('EXPENSES:')
    # for el in a.expenses:
    #     print(el)
    # inc=Income(100,'lottery','22-03-2019')
    # a.add_income(inc)
    # print('INCOMES')
    # for el in a.incomes:
    #     print(el)
    # print('---------show_user_data_per_date---------')
    # a.show_user_data_per_date('23-03-2019')
if __name__=='__main__':
    main()