# cat.py
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
    while i<len(array)-1:
        array[i]=remove_newline(array[i])
        print(array[i])
        i=i+1
    print(array[i])
    f.close()



def main():
    cat(sys.argv[1])

if __name__ == '__main__':
    main()