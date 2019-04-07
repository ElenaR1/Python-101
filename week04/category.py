class Category:
    def __init__(self,amount,category_type,date):
        self.date=date
        self.amount=amount
        self.category_type=category_type

    def __str__(self):
        s=self.category_type+' '+str(self.amount)+' '+self.date
        return s
    def __eq__(self,other):
        return self.amount==other.amount and self.category_type==other.category_type and self.date==other.date
    def __repr__(self):
        return self.__str__


class Income(Category):
    def __init__(self,amount,category_type,date):
        super().__init__(amount,category_type,date)
class Expense(Category):
    def __init__(self,amount,category_type,date):
        super().__init__(amount,category_type,date)


def main():
    a=Income(100,"Savings","22-03-2019")
    print(a)

if __name__=='__main__':
    main()