import sys
import operator


def remove_newline(str):
    n=len(str)
    str=str[:n-1]
    return str

def cat(arguments):
    f=open(arguments)
    i=0;
    #print(f.readlines())
    array=f.readlines()
    #print(array)
    while i<len(array)-1:
        array[i]=remove_newline(array[i])
        print(array[i])
        i=i+1
    print(array[i])
    f.close()

def create_dict(arguments):
    d=dict()
    subdict=dict()
    f=open(arguments)
    i=1;
    #print(f.readlines())
    array=f.readlines()
    #print(array)
    array[0]=remove_newline(array[0])
    k=array[0].replace('=','')
    key=k[1:len(k)-1]
    while i<len(array)-1:
        array[i]=remove_newline(array[i])
        spl=array[i].split(',')
        #print(spl)
        el=spl[0]
        #print(el)
        if(el[0]=='='):
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


def list_user_data(all_user_data):
    for keys, values in all_user_data.items():
        print ("key: ",  keys)
        #print ("values: " , values)
        for keys1, values1 in all_user_data[keys].items():
            print ("key1: " , keys1)
            print ("values1: ", values1)


def show_user_incomes(all_user_data):
    income_array=[]
    for keys, values in all_user_data.items():
        for keys1, values1 in all_user_data[keys].items():
            if keys1=='New Income' or keys1=='income':               
                for i in range(len(values1)):
                    income_array.append(values1[i])
    return income_array

def show_user_savings(all_user_data):
    pass


def show_user_deposits(all_user_data):
    pass


def show_user_expenses(all_user_data):
    expense_array=[]
    for keys, values in all_user_data.items():
        for keys1, values1 in all_user_data[keys].items():
            if keys1=='New Expense' or keys1=='expense':               
                for i in range(len(values1)):
                    expense_array.append(values1[i])
    return expense_array


def list_user_expenses_ordered_by_categories(all_user_data):
    expense_list=show_user_expenses(all_user_data)
    expense_list.sort(key = operator.itemgetter(1))
    return expense_list


def show_user_data_per_date(date, all_user_data):
   info_array=[]
   for keys, values in all_user_data.items():
        if keys==date:
            #print(values)
            for keys1, values1 in all_user_data[keys].items():
                    for i in range(len(values1)):
                        l=list(values1[i])
                        l.append(keys1)
                        tpl=tuple(l)
                        #print(tpl)
                        info_array.append(tpl)                       
   return info_array
   


def list_income_categories(all_user_data):
    income_list=show_user_incomes(all_user_data)
    income_categories=[]
    for i in range(len(income_list)):
        #print(income_list[i])
        income_categories.append(income_list[i][1])
    income_categories.sort()
    return income_categories


def list_expense_categories(all_user_data):
    pass


def add_income(income_category, money, date, all_user_data):
    pass


def add_expense(expense_category, money, date, all_user_data):
    pass


def main():
    my_dict=create_dict(sys.argv[1])
    print(my_dict)
    print("Choose one of the following options to continue:")
    print("1 - show all data")
    print("2 - show data for specific date")
    print("3 - show expenses, ordered by categories")
    print("4 - add new income")
    print("{5 - add new expense")
    print("6 - exit")
    #print(show_user_incomes(my_dict))
    # list_user_data(all_user_data)

    #print(show_user_incomes(my_dict))
    #print(show_user_data_per_date('23-03-2019',my_dict))
    #print(show_user_expenses(my_dict))
    #print(list_user_expenses_ordered_by_categories(my_dict))
    print(list_income_categories(my_dict))

    # choice=input()
    # if choice =='1':
    #      list_user_data(my_dict)
    # if choice =='2':
    #     date=input()
    #     show_user_data_per_date(date,sys.argv[1])



if __name__=='__main__':
    main()
    
