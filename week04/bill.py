class ValueError(Exception):
    pass
class TypeEror(Exception):
    pass

class Bill:
    def __init__(self,amount):#moje vmesto self da e rosi, prosto nadolu pak shte trqbva da e rosi;self e nashata instanciq, taka se zakacha
        self.validate_init_params(amount)
        self.amount=amount

    def validate_init_params(self,amount):#self pokazva che e zakachen kum nashataa instannciq
        if isinstance(amount,int)==False:
           raise ValueError('not int')
        if amount < 0:
            raise TypeEror('negative number')

    def __str__(self):
        s='A '+str(self.amount)+"$ bill"
        return s
    def __repr__(self):
        return self.__str__()# ako e __str__(self) otiva na vgradeniq str (default-niq)

    def __int__(self):
        return int(self.amount)

    def __eq__(self,other):
        return self.amount==other.amount

    def __hash__(self):
        return hash(self.amount)

class BatchBill:
     def __init__(self,bills):#moje vmesto self da e rosi, prosto nadolu pak shte trqbva da e rosi;self e nashata instanciq, taka se zakacha
        #self.validate_init_params(bills)
        self.bills=bills

     def __len__(self):
        n=len(self.bills)
        return n

     def total(self):
        n=len(self)
        s=0
        for i in range(n):
            s+=self.bills[i].amount
        return s
     def __getitem__(self, index):
        return self.bills[index]

class CashDesk:
     total_money=0
     bills=[]
     def __init__(self):
        pass
     def take_money(self,money):
            if isinstance(money,Bill):
                self.total_money+=money.amount
                self.bills.append(money)
            if isinstance(money,BatchBill):
                self.total_money+=money.total()
                for bill in money:
                    self.bills.append(bill)
            
     def total(self):
        return self.total_money
     def inspect(self):
        print("We have the following count of bills, sorted in ascending order:")
        unique_bills=[]
        for bill in self.bills:
            if bill not in unique_bills:
                unique_bills.append(bill)
        for bill in unique_bills:
            s=str(int(bill))+'$ bills '+str(self.bills.count(bill))
            print(s)



def main():
    # b2=Bill(100)
    # print(b2.amount)
    # print(str(b2))
    # print(repr(b2))
    # print(int(b2))
    # b4=Bill(100)
    # print(b2==b4)
    # print(hash(b2))


    # a = Bill(10)
    # b = Bill(5)
    # c = Bill(10)

    # money_holder = {}

    # money_holder[a] = 1 # We have one 10% bill
    # print(money_holder)
    # if c in money_holder:# c is the same as a
    #     print('yes')
    #     money_holder[c] += 1

    # print(money_holder) # { "A 10$ bill": 2 }

    # bill1=Bill('ko')
    # b3=Bill(-10)
    # print('-----------------')


    # a = Bill(10)
    # b = Bill(5)
    # c = Bill(10)
    # bb=BatchBill([a,b,c])
    # print(len(bb))
    # print(bb.total())
    # values = [10, 20, 50, 100]
    # bills = [Bill(value) for value in values]

    # batch = BatchBill(bills)

    # for bill in batch:
    #     print(bill)

# A 10$ bill
# A 20$ bill
# A 50$ bill
# A 100$ bill


    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BatchBill(bills)
    desk = CashDesk()
    desk.take_money(batch)
    desk.take_money(Bill(10))
    print(desk.total())#390
    print(CashDesk.total_money)#0
    desk.inspect()


if __name__=='__main__':
    main()
    

