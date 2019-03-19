import csv



def filter(file_name,**kwargs):
    #with open('example_data.csv') as csv_file:
    import re
    result_array=list()
    f=open(file_name)
    array=f.readlines()
    # print(re.findall(r'"([^"]*)"', str(array)))
    # print('-------')
    #print(array)
    for i in range(len(array)):
        array[i]=array[i].split(',')
        #print(array[i][2])
        # if array[i][2][0]=='"':
        #     k=len(array[i][2])
            # print(array[i][2])
            # print()
    #print(array)
    #if args[0]=='full_name':
    if len(kwargs)==1:
        for key,val in kwargs.items():
            if key=='full_name':
                for i in range(len(array)):
                    if array[i][0]==val:
                        result_array[len(result_array):]=[array[i]]
            if key=='full_name__starswith':
                for i in range(len(array)):
                    k=len(val)
                    if array[i][0][:k]==val:
                       # print(' '.join(array[i]))
                        result_array[len(result_array):]=[array[i]]
            if key=='email__contains':
                for i in range(len(array)):
                    if val in ' '.join(array[i]):
                        result_array[len(result_array):]=[array[i]]
    #for more than 2 elements in kwargs ? the dictionary is unordered, so how will a ckeck it
    if len(kwargs)==2:
        n1=int(kwargs['salary__gt'])
        n2=int(kwargs['salary__lt'])
        for i in range(1,len(array)):
            n=len(array[i])
            if int(array[i][n-1])> n1 and  int(array[i][n-1]) <n2:
                #print(array[i][n-1])
                result_array[len(result_array):]=[array[i]]

        # j=0
        # for key,val in kwargs.items():
        #     if key=='full_name':
        #         for i in range(len(array)):
        #             if array[i][0]==val:
        #                 result_array[len(result_array):]=[array[i]]
    


        
    #with args
    #     for i in range(len(array)):
    #         if array[i][0]==args[0]:
    #             print("one arg",array[i])
    #             result_array[len(result_array):]=[array[i]]
    # if len(args)==2:
    #     for i in range(len(array)):
    #         if array[i][0]==args[0] and array[i][1]==args[1]:
    #             print("two arg",array[i])
    #             result_array[len(result_array):]=[array[i]]
    #print(len(result_array))
    return result_array




#print(filter('example_data.csv',full_name="Diana Harris"))
# print('----------------------')
print(filter('example_data.csv',full_name__starswith="Michael"))
# print('---------------------')
#print(filter('example_data.csv',email__contains="@gmail"))
# print('---------------------')
# #print(filter('example_data.csv',salary__gt=1000, salary__lt=3000))


def count_filter(file_name,**kwargs):
    #with open('example_data.csv') as csv_file:
    result_array=list()
    f=open(file_name)
    array=f.readlines()
    for i in range(len(array)):
        array[i]=array[i].split(',')
    #print(array)
    #if args[0]=='full_name':
    if len(kwargs)==1:
        for key,val in kwargs.items():
            if key=='full_name':
                for i in range(len(array)):
                    if array[i][0]==val:
                        result_array[len(result_array):]=[array[i]]
            if key=='full_name__starswith':
                for i in range(len(array)):
                    k=len(val)
                    if array[i][0][:k]==val:
                       # print(' '.join(array[i]))
                        result_array[len(result_array):]=[array[i]]
            if key=='email__contains':
                for i in range(len(array)):
                    if val in ' '.join(array[i]):
                        result_array[len(result_array):]=[array[i]]
    #for more than 2 elements in kwargs ? the dictionary is unordered, so how will a ckeck it
    if len(kwargs)==2:
        n1=int(kwargs['salary__gt'])
        n2=int(kwargs['salary__lt'])
        print(n1,n2)
        for i in range(1,len(array)):
            n=len(array[i])
            if int(array[i][n-1])> n1 and  int(array[i][n-1]) <n2:
                #print(array[i][n-1])
                result_array[len(result_array):]=[array[i]]

        # j=0
        # for key,val in kwargs.items():
        #     if key=='full_name':
        #         for i in range(len(array)):
        #             if array[i][0]==val:
        #                 result_array[len(result_array):]=[array[i]]
    


        
    #with args
    #     for i in range(len(array)):
    #         if array[i][0]==args[0]:
    #             print("one arg",array[i])
    #             result_array[len(result_array):]=[array[i]]
    # if len(args)==2:
    #     for i in range(len(array)):
    #         if array[i][0]==args[0] and array[i][1]==args[1]:
    #             print("two arg",array[i])
    #             result_array[len(result_array):]=[array[i]]
    return len(result_array)



#first
#return result_array[0]

#last
#return result_array[len(result_array)-1]
