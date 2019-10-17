# po-nadolu sa obqsneni
import math

def print_factors(x):
    for i in range(1,x+1):
        if x%i==0:
            print(i)

def prime(num):
    if num>1:
        for i in range(2,num):#for i in range(2, num//2):
            if num%i==0:
                return False
        return True
    else:
        return False

def primeFactors(n):
    while n%2==0:
        print(2)
        n=n//2
    for i in range(3,int(math.sqrt(n))+1):
        while n%i==0:
            print(i)
            n=n//i
    if n>2:
        print(n)
         
 ##########################################################



#Find Factors of Number
# Python Program to find the factors of a number

# define a function
def print_factors(x):
   # This function takes a number and prints the factors

   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

# change this value for a different result.
num = 320

# uncomment the following line to take input from the user
#num = int(input("Enter a number: "))

print_factors(num)

#Check Prime Number
# Python program to check if the input number is prime or not

num = 407

# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
   
 #drug nachin
# Python program to check if  
# given number is prime or not 
  
num = 11
  
# If given number is greater than 1 
if num > 1: 
      
   # Iterate from 2 to n / 2  
   for i in range(2, num//2): 
         
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number") 

   

#Find all prime factors
# A function to print all prime factors of  
# a given number n 
def primeFactors(n): 
      
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        print 2, 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            print i, 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        print n 
