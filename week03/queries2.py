def filter(file_name,**kwargs):
    #with open('example_data.csv') as csv_file:
    import re
    result_array=list()
    f=open(file_name)
    array=f.readlines()
    for i in range(len(array)):
        array[i]=array[i].split(',')
    for i in range(len(array)):
        n=len(array[i])
        if n > 6:
            num_of_additional_cols= n -6        
            array[i][2:2+num_of_additional_cols+1] = [''.join(array[i][2:2+num_of_additional_cols+1])]
    add_element=True
    array=array[1:]
    for el in array:
        #print(el[0])
        for key, value in kwargs.items():
            #print('key:',key,"val:",value)
            if key=='full_name':
                if el[0]==value:
                    #print(el[0],value)
                    #result_array[len(result_array):]=[el]
                    continue
                else:
                    add_element=False
            if key=='full_name__starswith':
                k=len(value)
                if el[0][:k]==value:
                    #result_array[len(result_array):]=[el]
                    continue
                else:
                    add_element=False
            if key=='favourite_color':
                if el[1]==value:
                    continue
                else:
                    add_element=False
            if key=='company_name':
                if el[2]==value:
                    continue
                else:
                    add_element=False
            if key=='email__contains':
                if value in el[3]:
                    continue
                else:
                    add_element=False
            if key=='email':
                if el[3]==value:
                    continue
                else:
                    add_element=False
            if key=='phone_number':
                if value == el[4]:
                    continue
                else:
                    add_element=False
            if key=='salary':
                if value == int(el[5]):
                    continue
                else:
                    add_element=False
            if key=='salary__gt':
                print(el[5],value)
                if int(el[5])>value:
                    continue
                else:
                    add_element=False
            if key=='salary__lt':
                if int(el[5])<value:
                    continue
                else:
                    add_element=False

        if add_element==True:
            result_array[len(result_array):]=[el]
        else:
            add_element=True
    if 'order_by' in kwargs.keys():
        if kwargs['order_by']=='full_name':
            result_array = sorted(result_array, key=lambda k: k[0])
        if kwargs['order_by']=='favourite_color':
            result_array = sorted(result_array, key=lambda k: k[1])
        if kwargs['order_by']=='company_name':
            result_array = sorted(result_array, key=lambda k: k[2])
        if kwargs['order_by']=='email':
            result_array = sorted(result_array, key=lambda k: k[3])
        if kwargs['order_by']=='phone_number':
            result_array = sorted(result_array, key=lambda k: k[4])
        if kwargs['order_by']=='salary':
            result_array = sorted(result_array, key=lambda k: k[5])

    print(len(result_array))
    return result_array




def filter_count(file_name,**kwargs):
    #with open('example_data.csv') as csv_file:
    import re
    result_array=list()
    f=open(file_name)
    array=f.readlines()
    for i in range(len(array)):
        array[i]=array[i].split(',')
    for i in range(len(array)):
        n=len(array[i])
        if n > 6:
            num_of_additional_cols= n -6        
            array[i][2:2+num_of_additional_cols+1] = [''.join(array[i][2:2+num_of_additional_cols+1])]
    add_element=True
    array=array[1:]
    for el in array:
        #print(el[0])
        for key, value in kwargs.items():
            #print('key:',key,"val:",value)
            if key=='full_name':
                if el[0]==value:
                    #print(el[0],value)
                    #result_array[len(result_array):]=[el]
                    continue
                else:
                    add_element=False
            if key=='full_name__starswith':
                k=len(value)
                if el[0][:k]==value:
                    #result_array[len(result_array):]=[el]
                    continue
                else:
                    add_element=False
            if key=='favourite_color':
                if el[1]==value:
                    continue
                else:
                    add_element=False
            if key=='company_name':
                if el[2]==value:
                    continue
                else:
                    add_element=False
            if key=='email__contains':
                if value in el[3]:
                    continue
                else:
                    add_element=False
            if key=='email':
                if el[3]==value:
                    continue
                else:
                    add_element=False
            if key=='phone_number':
                if value == el[4]:
                    continue
                else:
                    add_element=False
            if key=='salary':
                if value == int(el[5]):
                    continue
                else:
                    add_element=False
            if key=='salary__gt':
                print(el[5],value)
                if int(el[5])>value:
                    continue
                else:
                    add_element=False
            if key=='salary__lt':
                if int(el[5])<value:
                    continue
                else:
                    add_element=False

        if add_element==True:
            result_array[len(result_array):]=[el]
        else:
            add_element=True
    if 'order_by' in kwargs.keys():
        if kwargs['order_by']=='full_name':
            result_array = sorted(result_array, key=lambda k: k[0])
        if kwargs['order_by']=='favourite_color':
            result_array = sorted(result_array, key=lambda k: k[1])
        if kwargs['order_by']=='company_name':
            result_array = sorted(result_array, key=lambda k: k[2])
        if kwargs['order_by']=='email':
            result_array = sorted(result_array, key=lambda k: k[3])
        if kwargs['order_by']=='phone_number':
            result_array = sorted(result_array, key=lambda k: k[4])
        if kwargs['order_by']=='salary':
            result_array = sorted(result_array, key=lambda k: k[5])

    return len(result_array)



def first(file_name,**kwargs):
    #with open('example_data.csv') as csv_file:
    import re
    result_array=list()
    f=open(file_name)
    array=f.readlines()
    for i in range(len(array)):
        array[i]=array[i].split(',')
    for i in range(len(array)):
        n=len(array[i])
        if n > 6:
            num_of_additional_cols= n -6        
            array[i][2:2+num_of_additional_cols+1] = [''.join(array[i][2:2+num_of_additional_cols+1])]
    add_element=True
    array=array[1:]
    for el in array:
        #print(el[0])
        for key, value in kwargs.items():
            #print('key:',key,"val:",value)
            if key=='full_name':
                if el[0]==value:
                    #print(el[0],value)
                    #result_array[len(result_array):]=[el]
                    continue
                else:
                    add_element=False
            if key=='full_name__starswith':
                k=len(value)
                if el[0][:k]==value:
                    #result_array[len(result_array):]=[el]
                    continue
                else:
                    add_element=False
            if key=='favourite_color':
                if el[1]==value:
                    continue
                else:
                    add_element=False
            if key=='company_name':
                if el[2]==value:
                    continue
                else:
                    add_element=False
            if key=='email__contains':
                if value in el[3]:
                    continue
                else:
                    add_element=False
            if key=='email':
                if el[3]==value:
                    continue
                else:
                    add_element=False
            if key=='phone_number':
                if value == el[4]:
                    continue
                else:
                    add_element=False
            if key=='salary':
                if value == int(el[5]):
                    continue
                else:
                    add_element=False
            if key=='salary__gt':
                print(el[5],value)
                if int(el[5])>value:
                    continue
                else:
                    add_element=False
            if key=='salary__lt':
                if int(el[5])<value:
                    continue
                else:
                    add_element=False

        if add_element==True:
            result_array[len(result_array):]=[el]
        else:
            add_element=True
    if 'order_by' in kwargs.keys():
        if kwargs['order_by']=='full_name':
            result_array = sorted(result_array, key=lambda k: k[0])
        if kwargs['order_by']=='favourite_color':
            result_array = sorted(result_array, key=lambda k: k[1])
        if kwargs['order_by']=='company_name':
            result_array = sorted(result_array, key=lambda k: k[2])
        if kwargs['order_by']=='email':
            result_array = sorted(result_array, key=lambda k: k[3])
        if kwargs['order_by']=='phone_number':
            result_array = sorted(result_array, key=lambda k: k[4])
        if kwargs['order_by']=='salary':
            result_array = sorted(result_array, key=lambda k: k[5])

    return result_array[0]


def last(file_name,**kwargs):
    #with open('example_data.csv') as csv_file:
    import re
    result_array=list()
    f=open(file_name)
    array=f.readlines()
    for i in range(len(array)):
        array[i]=array[i].split(',')
    for i in range(len(array)):
        n=len(array[i])
        if n > 6:
            num_of_additional_cols= n -6        
            array[i][2:2+num_of_additional_cols+1] = [''.join(array[i][2:2+num_of_additional_cols+1])]
    add_element=True
    array=array[1:]
    for el in array:
        #print(el[0])
        for key, value in kwargs.items():
            #print('key:',key,"val:",value)
            if key=='full_name':
                if el[0]==value:
                    #print(el[0],value)
                    #result_array[len(result_array):]=[el]
                    continue
                else:
                    add_element=False
            if key=='full_name__starswith':
                k=len(value)
                if el[0][:k]==value:
                    #result_array[len(result_array):]=[el]
                    continue
                else:
                    add_element=False
            if key=='favourite_color':
                if el[1]==value:
                    continue
                else:
                    add_element=False
            if key=='company_name':
                if el[2]==value:
                    continue
                else:
                    add_element=False
            if key=='email__contains':
                if value in el[3]:
                    continue
                else:
                    add_element=False
            if key=='email':
                if el[3]==value:
                    continue
                else:
                    add_element=False
            if key=='phone_number':
                if value == el[4]:
                    continue
                else:
                    add_element=False
            if key=='salary':
                if value == int(el[5]):
                    continue
                else:
                    add_element=False
            if key=='salary__gt':
                print(el[5],value)
                if int(el[5])>value:
                    continue
                else:
                    add_element=False
            if key=='salary__lt':
                if int(el[5])<value:
                    continue
                else:
                    add_element=False

        if add_element==True:
            result_array[len(result_array):]=[el]
        else:
            add_element=True
    if 'order_by' in kwargs.keys():
        if kwargs['order_by']=='full_name':
            result_array = sorted(result_array, key=lambda k: k[0])
        if kwargs['order_by']=='favourite_color':
            result_array = sorted(result_array, key=lambda k: k[1])
        if kwargs['order_by']=='company_name':
            result_array = sorted(result_array, key=lambda k: k[2])
        if kwargs['order_by']=='email':
            result_array = sorted(result_array, key=lambda k: k[3])
        if kwargs['order_by']=='phone_number':
            result_array = sorted(result_array, key=lambda k: k[4])
        if kwargs['order_by']=='salary':
            result_array = sorted(result_array, key=lambda k: k[5])

    return result_array[len(result_array)-1]



def main():
    print('filter')
    print(filter('example_data.csv',full_name="Diana Harris"))
    print('----------------------')
    print(filter('example_data.csv',full_name__starswith="Michael",favourite_color="teal"))
    print('---------------------')
    #print(filter('example_data.csv',email__contains="@gmail"))
    # print('---------------------')
    #print(filter('example_data.csv',salary__gt=1000, salary__lt=3000))
    print(filter('example_data.csv',full_name__starswith="Michael",order_by='salary'))
    #print(filter('example_data.csv',company_name="Sanchez-Poole"))
    print(filter('example_data.csv',phone_number="(867)299-2717x38504"))
    print(filter('example_data.csv',salary=4881))

    print(filter_count('example_data.csv',full_name__starswith="Michael",order_by='salary'))#8
    print(first('example_data.csv',full_name__starswith="Michael",order_by='salary'))
    print(last('example_data.csv',full_name__starswith="Michael",order_by='salary'))

if __name__=='__main__':
    main()