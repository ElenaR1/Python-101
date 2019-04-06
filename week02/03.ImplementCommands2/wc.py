# generate_numbers.py
import sys

def count_newline(s):
    pattern = '\n'
    count =0
    flag=True
    start=0
    while flag:
        a = nStr.find(pattern,start)  # find() returns -1 if the word is not found, 
                                      #start i the starting index from the search starts(default value is 0)
        if a==-1:          #if pattern not found set flag to False
            flag=False
        else:               # if word is found increase count and set starting index to a+1
            count+=1        
            start=a+1
    print(count)

def join(items, delimiter):
    result = ''
    n = len(items)

    for index in range(n):
        item = items[index]

        result = result + item

        if index != n - 1:
            result += delimiter

    return result

def wc(command,filename,):
    f=open(filename)
    array=f.readlines()
    #s=str(array)
    #print(s)
    #print(array)
    n=len(array)
    if command=="lines":
         return n
    if command=='chars':
        count_chars=0
        for i in range(n):
           count_chars=count_chars+len(array[i])
        return count_chars
    if command=='words':
        count_words=0
        for item in array:
            if item=="\n":
                array.remove(item)       
        x=join(array,'')
        return(len(x.split()))
       


def main():
    print(wc(sys.argv[1],sys.argv[2]))

if __name__ == '__main__':
    main()