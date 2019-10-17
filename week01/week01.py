# from functions import sum_3,a,A
# print(sum_3(1,2,3))#6 6

# print(a,A)# 1 2 

# b=[1,2,3]
# x=4
# b=b+[x]
# print(b)#[1, 2, 3, 4]

# b.append(5)
# print(b)#[1, 2, 3, 4,5]



# def build_index_list(n):
#     result=[]
#     index=0
#     while index < n:
#         result.append(index)
#         index+=1
#     return result



# items=['a','b','c']
# n=len(items)
# indexes=range(n)
# for index in indexes:
#     item=items[index]
#     print(item)
import math  

# l=[x for x in [1,2,3,4,5,6] if x%2==0]
# print(l)#[2, 4, 6]
# new_range  = [i * i          for i in range(5)   if i % 2 == 0]#[0, 4, 16]
# print(new_range)
# fh = open("test.txt", "r")
# print([i for i in fh if "line3" in i])

#1 Sum of all digits of a number

def sum_of_digits(n):
    sum=0
    if n <0:
        n=n*(-1)
    while n > 0:
        digit=n%10
        n=n//10
        sum=sum+digit
    return sum

#print(sum_of_digits(-4820))



# 2 Turn a number into a list of digits

def to_digits(n):
    list=[]
    while n >0:
        list.append(n%10)
        n=n//10
    list.reverse()
    return list

#print(to_digits(123))

def to_digits2(n):
    n = abs(n)

    return [int(ch) for ch in str(n)]#The str() method returns the "informal" or nicely printable representation of a given object.
print(to_digits2(123))


def sum_of_digits2(n):
    return sum(to_digits2(n))
print(sum_of_digits2(-4820))


#3 Turn a list of digits into a number

def to_number(digits):
    n=len(digits)
    index=0
    num=0
    digits.reverse()
    while index < n:
        digit=digits[index]
        num=num + digit*(10**index)
        index=index+1
    return num
#print(to_number([1,2,3,0,2,3]))

#for-cycle
def to_num(digits):
    n=len(digits)
    index=0
    num=0
    digits.reverse()
    for index in range(n):
        digit=digits[index]
        num=num + digit*(10**index)
    return num

#print(to_num([1,2,3,0,2,3]))


def join(items, delimiter):
    result = ''
    n = len(items)

    for index in range(n):
        item = items[index]

        result = result + item

        if index != n - 1:
            result += delimiter

    return result


print(join(['a','b','C','D'],';'))
#print([str(digit) for digit in [1,2,3,0,2,3]]) #['1', '2', '3', '0', '2', '3']
def to_number2(digits):
    chars = [str(digit) for digit in digits]# purvo pravim spisuka ot integeri v spisuk ot charove

    return int(join(chars, ''))#prevrushtame stringa koito se vrushta ot join v chislo
print(to_number2([1,2,3,0,2,3]))

#Factorial Digits

def fact(n):
    if n in [0, 1]:
        return 1

    result = 1

    for x in range(n):
        result *= x + 1

    return result
#or
def fact(n):
    if n in [0, 1]:
        return 1

    result = 1

    for x in range(2,n+1):
        result *= x 

    return result

#or recursive
def fact(n):
    if n in [0, 1]:
        return 1

    return n*fact(n-1)

print(fact(4))

def fact_digits(n):
    sum=0
    while n > 0:
        digit=n%10
        sum=sum+(fact(digit))
        n=n//10
    return sum

#print(fact_digits(999))


def fact_digits2(n):
   return sum([fact(digit) for digit in to_digits2(n)])
print(fact_digits2(999))



#Palindrome
def palindrome(n):
    isPalindrome=True
    if isinstance(n, str)==False: 
        n=str(n)
    len_of_n=len(n)
    l=0
    r=len_of_n-1
    while l < r:
        if n[l]==n[r]:
            l=l+1
            r=r-1
        else:
            isPalindrome=False
            break
    return isPalindrome

def reverse_string(string):
    result = ''
    n = len(string)

    for i in range(n):
        result += string[n - i - 1]

    return result

def palindrome2(obj):
    string_repr_of_obj = str(obj)
    return string_repr_of_obj == reverse_string(string_repr_of_obj)
print(palindrome2(134431))

#print(isinstance("abab", str) )


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

print( count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))


def count_consonants(str):
    consonants={'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z'}
    count=0
    n=len(str)
    if str.islower()==False:
        str=str.lower()
    for i in range(0,n):
       if str[i] in consonants:
        count=count+1
    return count

print( count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
print( count_consonants("Python"))


#Char Histogram
def char_histogram(string):
    out = {}
    for c in string:
        out[c] = out.get(c, 0) + 1#out.get(c, 0) namira kolko chesto se sreshta 'c' v set-a out
        print(c,out[c])
    return out
#print(char_histogram("Python!"))
print('Histogram: ',char_histogram("AAAAaaabb!!!"))

#another way
def char_histogram(string):
    d=dict()
    for el in string:
        if el not in d.keys():
            d[el]=1
        else:
            val=d[el]
            d[el]=val+1
    return d


#Sum Numbers in Matrix
def sum_matrix(m):
    n=len(m)
    sum=0
    for i in range(n):
        for j in range(len(m[i])):
            sum=sum+m[i][j]
    return sum
print('sum matrix')
print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])) # 55
# ???
def sum_matrix2(m):
    n=len(m)
    l=[]
    sum=0
    for i in range(n):
        l=l+[x for x in m[i]]
    print(l)
    Sum = sum(l) 
    return Sum 

#print(sum_matrix2([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])) # 55

# NaN Expand
def  nan_expand(times):
    s=""
    for i in range(times):
        s=s+"Not a "
    if s != "":
        s=s+"NaN"
    return s

print(nan_expand(3))

#Integer prime factorization
print('prime_factorization')
def prime_factorization(n):
    l=[]
    newl=[]
    while n % 2 == 0: 
        print (2) 
        l=l+[2]
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
        print("i: ",i,"int(math.sqrt(n))+1 ", int(math.sqrt(n))+1," n: ",n)
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            print (i) 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        l=l+[n]
        print (n) 
    print(l)
    for i in range(len(l)):
        print(l[i],l.count(l[i]))
        item=l[i]
        newl[item]=l.count(l[i])
    print(newl)



print(prime_factorization(80))

#another way
def prime(num):
    if num>1:
        for i in range(2,num):#for i in range(2, num//2):
            if num%i==0:
                return False
        return True
    else:
        return False

def prime_factorization(n):
    l=[]
    for i in range(2,n+1):
        if n%i==0 and prime(i):
            count=0
            while n%i==0:
                count+=1
                n=n//i
            l.append((i,count))
    return l


#The group function
print('The group function')
def group(lst):
    n=len(lst)
    newl=[]
    if lst==[]:
        return []
    else:
        for i in range(n):
            if i == 0:
                sub_arr=[]
                sub_arr.append(lst[i])
                newl.append(sub_arr)
            elif i != 0 and i != n-1 :
                if lst[i]==lst[i-1]:
                    newl[-1].append(lst[i])
                if lst[i] != lst[i-1]:
                    sub_arr=[]
                    sub_arr.append(lst[i])
                    newl.append(sub_arr)
            elif i==n-1:
                if lst[i]==lst[i-1]:
                    newl[-1].append(lst[i])
                if lst[i] != lst[i-1]:
                    sub_arr=[]
                    sub_arr.append(lst[i])
                    newl.append(sub_arr)
    return newl

print(group([1, 1, 1, 2, 3, 1, 1]))
print(group([1, 2, 1, 2, 3, 3]))
print(group([1, 2, 1, 2, 2, 2,2,4,4]))

#another way
def group(lst):
    sub_lst=[]
    newl=[]
    sub_lst+=[lst[0]]
    for i in range(1,len(lst)):
        #print('sub_lst outer: ',sub_lst,i,lst[i],lst[i]==sub_lst[-1])
        if lst[i]==sub_lst[-1]:
            sub_lst.append(lst[i])
        else:
            newl.append(sub_lst)
            sub_lst=[]
            sub_lst.append(lst[i])
            #print('sub_lst: ',sub_lst)
    newl.append(sub_lst)
    return newl

#Longest subsequence of equal consecutive elements
print('Longest subsequence of equal consecutive elements')
def max_consecutive(items):
    lst=group(items)
    count_lst=[]
    for el in lst:
        n=len(el)
        count_lst.append(n)
    return max(count_lst)

print(max_consecutive([1, 1, 1, 2, 3, 1, 1]))
print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))


#Word counter
print('Word counter')

def transpose(matrix):
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed_matrix

def contains(word,row):
    count=0
    s=''.join(row)
    #print(s)
    count+= s.count(word)
    reversed_word=word[::-1]
    count+= s.count(reversed_word)
    return count

def get_diagonal(mat, bltr = True):
      dim = len(mat)
      #assert dim == len(mat[0])
      lst = [[] for total in range(2 * len(mat) - 1)] 
      print('lst',lst)
      for row in range(len(mat)):
        for col in range(len(mat[row])):
          if bltr: 
            # print(lst[row + col],mat[row][col])
            lst[row + col].append(mat[col][row])
            # print(lst[row + col])
          else:    lst[col - row + (dim - 1)].append(mat[row][col])
      return lst

def check_diagonals(word,rows,cols,matrix):
    print('in check_diagonals')
    reversed_word=word[::-1]
    left_to_right=get_diagonal(matrix,True)
    right_to_left=get_diagonal(matrix,False)
    count=0
    for el in left_to_right:
        str_el=''.join(el)
        #print(str_el)
        if word in str_el:
            count+=str_el.count(word)
        if reversed_word in str_el:
            count+=str_el.count(reversed_word)
      
    for el in right_to_left:
        #print(str_el)
        str_el=''.join(el)
        if word in str_el:
            count+=str_el.count(word)
        if reversed_word in str_el:
            count+=str_el.count(reversed_word)
    return count


def check_rows(word,rows,cols,matrix):
    print('in check_rows')
    count=0
    for i in range(rows):
        count+=contains(word,matrix[i])
    return count

def check_cols(word,rows,cols,matrix):
    print('in check_cols')
    transposed_matrix=transpose(matrix)
    #print('transposed_matrix',transposed_matrix)
    count=0
    for i in range(cols):
        count+=contains(word,transposed_matrix[i])
    return count 


def word_counter(word,rows,cols,mat):
    n=len(word)
    if n>rows or n > cols:
        msg="not a valid input"
        return msg
    count=0
    count=check_rows(word,rows,cols,mat)+check_cols(word,rows,cols,mat)+check_diagonals(word,rows,cols,mat)
    print('rows and cols and diagonals',check_rows(word,rows,cols,mat),check_cols(word,rows,cols,mat),check_diagonals(word,rows,cols,mat))
    return count


mat=[['i','v','a','n'],['i','p','o','a'],['t','v','a','v'],['k','o','a','i']]
print(get_diagonal(mat,True))
print(get_diagonal(mat,False))
print(word_counter('iva',4,4,mat))
print('=====================')
mat2=[['i','v','a','n'],
      ['e','v','n','h'],
      ['i','n','a','v'],
      ['m','v','v','n'],
      ['q','r','i','t']]
print(word_counter('ivan',5,4,mat2))


