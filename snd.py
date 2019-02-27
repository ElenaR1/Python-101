from functions import sum_3,a,A
print(sum_3(1,2,3))

print(a,A)

b=[1,2,3]
x=4
b=b+[x]
print(b)
b.append(5)
print(b)


def build_index_list(n):
    result=[]
    index=0
    while index < n:
        result.append(index)
        index+=1
    return result



items=['a','b','c']
n=len(items)
indexes=range(n)
for index in indexes:
    item=items[index]
    print(item)



def sum_of_digits(n):
    sum=0
    if n <0:
        n=n*(-1)
    while n > 0:
        digit=n%10
        n=n//10
        sum=sum+digit
    return sum

print(sum_of_digits(-4820))






def to_digits(n):
    list=[]
    while n >0:
        list.append(n%10)
        n=n//10
    list.reverse()
    return list

print(to_digits(123))


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

print(to_number([1,2,3,0,2,3]))

#Factorial Digits

def fact(n):
    factorial = 1
    for i in range(1,n+1): 
        factorial = factorial * i 
    return factorial
print(fact(4))

def fact_digits(n):
    sum=0
    while n > 0:
        digit=n%10
        sum=sum+(fact(digit))
        n=n//10
    return sum

print(fact_digits(999))


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

print(palindrome(134431))

#print(isinstance("abab", str) )


#Vowels in a string
def count_vowels(str):
    vowels={'a','e','i','o','u','y'}
    count=0
    n=len(str)
    if str.islower()==False:
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
#def char_histogram(string):
