# sum_numbers.py - test it with numbers.txt
import sys
from random import randint



def sum_numbers(filename):
    f=open(filename)
    array=f.readlines()
    print(array)
    s=array[0]
    print(s)
    n=len(s)
    #print(n)
    local_sum=0
    global_sum=0
    i=0
    temp_str=""
    while i < n:
        if s[i]==' ':
            i=i+1
            num=int(temp_str)
            global_sum=global_sum+num
            temp_str=""
        else:
            temp_str=temp_str+s[i]
            i=i+1
    return global_sum+int(temp_str)



def main():
    print(sum_numbers(sys.argv[1]))

if __name__ == '__main__':
    main()