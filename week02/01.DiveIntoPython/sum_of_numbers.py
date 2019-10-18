
class CustomError(Exception):
    pass

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def sum_of_numbers(input_string):
    temp=''
    sum=0
    if hasNumbers(input_string)==False:
        raise CustomError("no numbers")
    for index,ch in enumerate(input_string):
        if ch.isdigit():
            #print(ch,temp)
            temp=temp+ch
        if ch.isdigit()==False:
            #print(ch)
            if(temp.isdigit()):
                #print(ch,temp)
                temp_num=int(temp)# int('x') ValueError: invalid literal for int() with base 10: 'x'
                sum=sum+temp_num
                temp=''
        if(ch.isdigit and index==len(input_string)-1 and temp.isdigit()):
             #print("end" ,temp)
             sum= sum+int(temp)
    return sum


#another way
def sum_of_numbers(input_string):
    temp=''
    s=0
    for ch in input_string:
        if ch.isdigit():
            temp+=ch
        else:
            if temp.isdigit():
                s+=int(temp)
                temp=''
    if temp.isdigit():
        s+=int(temp)
    return s



def main():
    print(sum_of_numbers("ab125cd3"))
    print(sum_of_numbers("ab"))
    
if __name__=='__main__':
    main()
