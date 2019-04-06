# cat2.py
import sys
def remove_newline(str):
    n=len(str)
    str=str[:n-1]
    return str

def cat(arguments):
    f=open(arguments)
    i=0;
    #print(f.readlines())
    array=f.readlines()
    #print(array)
    while i<len(array):
        array[i]=remove_newline(array[i])
        print(array[i])
        i=i+1
    f.close()

def cat2(arguments):
    n=len(arguments)
    # print(arguments)
    # print(n)
    for i in range(1,n):
        cat(arguments[i])
        print('\n')


def main():
    cat2(sys.argv)

if __name__ == '__main__':
    main()