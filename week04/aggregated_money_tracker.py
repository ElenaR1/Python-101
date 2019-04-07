from category import *

def remove_newline(str):
        n=len(str)
        str=str[:n-1]
        return str

def process_dict(array):
    d=dict()
    subdict=dict()
    array[0]=remove_newline(array[0])
    i=1;
    k=array[0].replace('=','')
    key=k[1:len(k)-1]
    while i<len(array)-1:
        array[i]=remove_newline(array[i])
        spl=array[i].split(',')
        #print(spl)
        el=spl[0]
        #print(el)
        if el[0]=='=':
            #print('a')
            d[key]=subdict
            #print("d:",d)
            subdict={}
            k=array[i].replace('=','')
            key=k[1:len(k)-1]
            i=i+1
            continue
        if spl[2][1:] in subdict.keys():
            tpl=(float(spl[0]),spl[1][1:])#spl[1][1:] we write [1:] so that the white space before the word is removed
            subdict[spl[2][1:]].append(tpl)
            #print(subdict)
        if spl[2][1:] not in subdict.keys():       
            sub_key=spl[2][1:]
            tpl=(float(spl[0]),spl[1][1:])
            sub_val=[tpl]
            subdict[sub_key]=sub_val
            #print(subdict)
        i=i+1
    #for the last one we don't need to remove the new line because it dooesn't have one
    if '\n' in array[i]:
        array[i]=remove_newline(array[i])
        spl=array[i].split(',')
        if spl[2][1:] in subdict.keys():
                tpl=(float(spl[0]),spl[1][1:])
                subdict[spl[2][1:]].append(tpl)
        if spl[2][1:] not in subdict.keys():       
                sub_key=spl[2][1:]
                tpl=(spl[0],spl[1])
                sub_val=[tpl]
                subdict[sub_key]=sub_val

    else:
        spl=array[i].split(',')
        if spl[2][1:] in subdict.keys():
                tpl=(float(spl[0]),spl[1][1:])
                subdict[spl[2][1:]].append(tpl)
        if spl[2][1:] not in subdict.keys():       
                sub_key=spl[2][1:]
                tpl=(spl[0],spl[1])
                sub_val=[tpl]
                subdict[sub_key]=sub_val

    d[key]=subdict
    #print(d)
    return d

class AggregatedObject:
    incomes=[]
    expenses=[]
    def __init__(self,all_user_data):
        self.all_user_data=all_user_data

    def process(self):
       #print(all_user_data)
       for keys, values in self.all_user_data.items():
            #print ("key: ",  keys)
            date=keys
        #print ("values: " , values)
            for keys1, values1 in self.all_user_data[keys].items():
                # print ("key1: " , keys1)
                # print ("values1: ", values1)
                if keys1=='New Income':
                    for val in values1:      
                        #print(val)                  
                        category_type=val[1]
                        amount=val[0]
                        obj=Income(amount,category_type,date)
                        self.incomes.append(obj) #[len(self.incomes):]
                if keys1=='New Expense':
                    for val in values1:      
                        #print(val)                  
                        category_type=val[1]
                        amount=val[0]
                        obj=Expense(amount,category_type,date)
                        self.expenses.append(obj) #[len(self.incomes):]
    # def add_income(self,inc):
    #    self.incomes.append(inc)  
    # def show_user_data_per_date(self,date):
    #     for el in self.incomes:
    #         if el.date==date:
    #             print(el)
    #     for el in self.expenses:
    #         if el.date==date:
    #             print(el)





def main():
    # a=AggregatedObject()
    # #arr={'22-03-2019': {'New Income': [(760.0, 'Salary')], 'New Expense': [(5.5, 'Eating Out'), (34.0, 'Clothes'), (41.79, 'Food'), (12.0, 'Eating Out'), (7.0, 'House'), (14.0, 'Pets'), (112.4, 'Bills'), (21.5, 'Transport')]}, '23-03-2019': {'New Income': [(50.0, 'Savings'), (200.0, 'Deposit')], 'New Expense': [(15.0, 'Food'), (5.0, 'Sports')]}}
    # arr=['=== 22-03-2019 ===\n', '760, Salary, New Income\n', '5.5, Eating Out, New Expense\n', '34, Clothes, New Expense\n', '41.79, Food, New Expense\n', '12, Eating Out, New Expense\n', '7, House, New Expense\n', '14, Pets, New Expense\n', '112.40, Bills, New Expense\n', '21.5, Transport, New Expense\n', '=== 23-03-2019 ===\n', '50, Savings, New Income\n', '15, Food, New Expense\n', '200, Deposit, New Income\n', '5, Sports, New Expense']
    # my_dict=process_dict(arr)
    # a.process(my_dict)
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
    pass

if __name__=='__main__':
    main()