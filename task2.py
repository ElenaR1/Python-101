import string
def filter(file_name,**kwargs):
    #with open('example_data.csv') as csv_file:
    exclude = set(string.punctuation)
    numbers={'0':'zero','1':'one', '2':'two', '3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    import re
    result_array=list()
    f=open(file_name)
    array=f.readlines()
    f.close()
    #print(array)
    for i in range(len(array)):
        array[i]=array[i].split(',')
    #print('-------------')
    #print(array)

    # for i in range(len(array)):
    #     n=len(array[i])
    #     if n > 6:
    #         num_of_additional_cols= n -6        
    #         array[i][2:2+num_of_additional_cols+1] = [''.join(array[i][2:2+num_of_additional_cols+1])]
    add_element=True
    array=array[1:]

    for el in array:
        #print(el[1],el[4],el[5])
        #print(el[0])
        for key, value in kwargs.items():
            #print('key:',key,"val:",value)
            if key=='Language':
                if el[4]==value:
                    #print(el[0],value)
                    #result_array[len(result_array):]=[el]
                    continue
                else:
                    add_element=False           

        if add_element==True:
            el[0] = ''.join(ch for ch in el[0] if ch not in exclude)
            el[7] = ''.join(ch for ch in el[7] if ch not in exclude)
            for ch in el[0]:
                if ch in numbers.keys():
                    el[0]=el[0].replace(ch,numbers[ch])
            for ch in el[7]:
                if ch in numbers.keys():
                    el[7]=el[7].replace(ch,numbers[ch])
                    
            result_array[len(result_array):]=[[el[0],el[7]]]
        else:
            add_element=True
    # if 'order_by' in kwargs.keys():
    #     if kwargs['order_by']=='full_name':
    #         result_array = sorted(result_array, key=lambda k: k[0])
    #     if kwargs['order_by']=='favourite_color':
    #         result_array = sorted(result_array, key=lambda k: k[1])
    #     if kwargs['order_by']=='company_name':
    #         result_array = sorted(result_array, key=lambda k: k[2])
    #     if kwargs['order_by']=='email':
    #         result_array = sorted(result_array, key=lambda k: k[3])
    #     if kwargs['order_by']=='phone_number':
    #         result_array = sorted(result_array, key=lambda k: k[4])
    #     if kwargs['order_by']=='salary':
    #         result_array = sorted(result_array, key=lambda k: k[5])

    l=len(result_array)
    print(l)
    for i in range(0,4):
        print(result_array[i])
    return result_array[0:4]


def main():
    print('filter')
    s = "ab1k0"
    numbers={'0':'zero','1':'one', 2:'two', 3:'three'}
    print('0' in numbers.keys(),numbers['0'])
    for el in s:
        if el in numbers.keys():
            s=s.replace(el,numbers[el])
            print(s)

    (filter('records.csv',Language='English'))
   

if __name__=='__main__':
    main()