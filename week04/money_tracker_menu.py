from money_tracker import MoneyTracker
from category import *
class MoneyTrackerMenu:
    def __init__(self,AggregatedObject):
        self.AggregatedObject=AggregatedObject
    def option(self):
        flag=True
        while flag:
            print("Choose one of the following options to continue:")
            print("1 - show all data")
            print("2 - show data for specific date")
            print("3 - show expenses, ordered by categories")
            print("4 - add new income")
            print("5 - add new expense")
            print("6 - exit")
            choice=input()
            if choice =='1':
                 obj=MoneyTracker(self.AggregatedObject)
                 obj.list_user_data()
            if choice =='2':
                date=input()
                obj=MoneyTracker(self.AggregatedObject)
                obj.show_user_data_per_date(date)
            if choice =='3':
                obj=MoneyTracker(self.AggregatedObject)
                print(obj.list_user_expenses_ordered_by_categories())
            if choice =='4':
                  print("New income amount:")
                  money=input()
                  if int(money) < 0:
                    raise CustomError('enter a valid amount')
                  print("New income type:")
                  income_category=input()
                  print("New income date:")
                  date=input()
                  obj=MoneyTracker(self.AggregatedObject)
                  i=Income(int(money),income_category,date)
                  obj.add_income(i)
                  # for el in obj.AggregatedObject.incomes:
                  #   print(el)
            if choice =='5':
                  print("New expense amount:")
                  money=input()
                  if int(money) < 0:
                    raise CustomError('enter a valid amount')
                  print("New expense type:")
                  expense_category=input()
                  print("New expense date:")
                  date=input()
                  obj=MoneyTracker(self.AggregatedObject)
                  i=Expense(int(money),expense_category,date)
                  obj.add_expense(i)
                  # for el in obj.AggregatedObject.expenses:
                  #   print(el)
            if choice=='6':
                  flag=False
            if choice not in ('1','2','3','4','5','6'):
                raise Exception('Invalid input')
        

def main():
    pass
if __name__=='__main__':
    main()