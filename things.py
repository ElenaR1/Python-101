#Vowels in a string
	def count_vowels(str):
	    vowels={'a','e','i','o','u','y'}
	    count=0
	    n=len(str)
	    if str.islower()==False:#islower proverqva dali vsichki elementi v string-a sa mali bukvi
	        str=str.lower()
	    for i in range(0,n):
	       if str[i] in vowels:
	        count=count+1
	    return count

#Week 2 DiveIntoPython

def get_largest_palindrome(num):
	    numstr = str(num)
	    for i in reversed(range(num)):#sys.min; negative numbers
	        #print(str(i),str(i)[::-1])
	        if str(i) == str(i)[::-1]:
	            return i
      
      
#Sum all numbers in a given string
print('======Sum all numbers in a given string======')
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def sum_of_numbers(input_string):
    temp=''
    sum=0
    if hasNumbers(input_string)==False:
        return 0
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
   
   
   
#Birthday Ranges
print('======Birthday Ranges======')
def birthday_ranges(birthdays, ranges):
    count_lst=[]
    count=0
    for item in ranges:
        for birthday in birthdays:
            if birthday>=item[0] and birthday<=item[1]:
                count=count+1
        count_lst=count_lst+[count]
        count=0
    return count_lst
    
#ADDITIONAL TASKS
def anagrams():
     output=""
     str1 = input()
     str2 = input()
     if str1.islower()==False:
        str1=str1.lower()
     if str2.islower()==False:
        str2=str2.lower()
     n_str1=len(str1)
     n_str2=len(str2)
     if n_str1!=n_str2:
        output="NOT ANAGRAMS"
        return output
     else:
        l1=sorted(str1)
        l2=sorted(str2)
        for i in range(n_str1):
            if l1[i]!=l2[i]:
                output="NOT ANAGRAMS"
                return output
        output="ANAGRAMS"               
        return output
def is_credit_card_valid(number):
    str_num=str(number)
    n=len(str_num)
    l=[]
    for i in reversed(range(n)):
         if i%2!=0:
             #print("odd",str_num[i])
             el=int(str_num[i])*2
             #print(el)
             l=l+[el]
         else:
             #print("even",str_num[i])
             el=int(str_num[i])
             l=l+[el]
    l.reverse()
    #print(l)
    str_num=""
    sum_digits=0
    for el in l:
        str_num+=str(el)
    #print(str_num)
    for el in str_num:
        sum_digits+=int(el)

    #print(sum_digits)
    if sum_digits%10==0:
        return True
    else:
        return False

#2nd version
def is_credit_card_valid2(number):
    l=len(str(number))
    str_num=str(number)
    new_num=''
    str_num=str_num[::-1]
    for ind,el in enumerate(str_num):
        if ind%2==0:
            new_num+=el
        else:
            transformed_dig=int(el)*2
            new_num+=str(transformed_dig)[::-1]
    new_num=new_num[::-1]
    sum=0
    for el in new_num:
        sum+=int(el)
    if sum%10==0:
        return True
    else:
        return False
#WEEK 03
def rpn_calculate(expr):
    ops = {'+','-','*','/','SQRT'}
    split_expr=expr.split(' ') 
    if len(split_expr)==1:
        return int(split_expr[0])
    st=[]
    num=int(split_expr[0])
    st.append(num)
    for tk in split_expr[1:]:
      #print(st)
      if tk in ops:
        #print("if",tk)
        if tk == '+':
            y,x = st.pop(),st.pop()
            z=x+y    
        if tk == '-':
            y,x = st.pop(),st.pop()
            z=x-y   
        if tk == '/':
            y,x = st.pop(),st.pop()
            z=x/y   
        if tk == '*':
            y,x = st.pop(),st.pop()
            z=x*y
        if tk == 'SQRT':
            y=st.pop()
            z=math.sqrt(y)
      else:
        #print("else",tk)
        z = int(tk)
      st.append(z)
    return z

#print(rpn_calculate("4 8 +"))
