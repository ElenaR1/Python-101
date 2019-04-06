# def f(a):
#     return a+2

# my_dict = {f(1):'fst',f(2):'snd'}
# print(my_dict)

# my_dict = {'fst': f(1), 'snd': f(2)}

#Are two words anagrams?
# def do_something(x, y, z='ZAZAZAZA'):
#     print ('x:', x)
#     print ('y:', y)
#     print ('z:', z)

# if __name__ == '__main__':
#     # Map command line arguments to function arguments.
#     do_something(*sys.argv[1:])

# def printt(x,y):
#     print("----",x)
#     print ("----",y)

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

print('Anagrams')
#print(anagrams())


#Credit card validation
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


print('Credit card validation')
print(is_credit_card_valid(14283))
print('79927398713',is_credit_card_valid(79927398713))
print('79927398715',is_credit_card_valid(79927398715))# def f(a):


#Goldbach Conjecture
print('Goldbach Conjecture')
def goldbach(n):
    primes=[x for x in range(n) if prime(x)==True]
    l=list()
    #print(primes)
    primes_len=len(primes)
    for i in range(n):
        for j in range(i,primes_len):
            if primes[i]+primes[j]==n:
                # print(primes[i],primes[j])
                l.append((primes[i],primes[j]))
    print(l)
def prime(num):
    if num > 2 and num%2==0:
        return False
    if num > 1: 
       for i in range(2, num//2): 
           if (num % i) == 0: 
               return False
       else: 
           return True
      
    else: 
       return False

goldbach(4)
goldbach(6)
goldbach(8)
goldbach(10)
goldbach(14)
goldbach(44)
goldbach(50)
goldbach(100)