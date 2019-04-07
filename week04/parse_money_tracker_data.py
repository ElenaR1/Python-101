import sys

def remove_newline(str):
    n=len(str)
    str=str[:n-1]
    return str


def create_arr(arguments):
    d=dict()
    subdict=dict()
    f=open(arguments)
    i=1;
    #print(f.readlines())
    array=f.readlines()
    # new_array=[]
    # for el in array:
    #     print(remove_newline(el))
    #     el=remove_newline(el)
    #     new_array.append(el)
    # return new_array
    return array




def main():
    pass

if __name__=='__main__':
    main()