def chain(iterable_one, iterable_two):
    l=[]
    for el in iterable_one:
        l.append(el)
    for el in iterable_two:
        l.append(el)

    for val in l:
        yield val



def chain2(iterable_one, iterable_two):
    l=[]
    for el in iterable_one:
        l.append(el)
    for el in iterable_two:
        l.append(el)

    class L:
         def __init__(self,lst):
            self.lst=lst
           

         def __iter__(self):
            self.index=0
            return self

         def __next__(self):
            index=self.index
            self.index+=1
            try:
                return self.lst[index]
            except IndexError:
                raise StopIteration

    obj=L(l)
    # i=iter(obj)
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # for el in obj:
    #     print(el)
    return L(l)


def compress(iterable, mask):
    for ind,el in enumerate(iterable):
        if mask[ind]==True:
            yield el


def cycle(iterable):
    s=""
    i=0
    while i<4:
        for el in iterable:
            s+=str(el)
        i+=1
        yield s
    
def remove_newline(str):
    n=len(str)
    str=str[:n-1]
    return str
def book_reader():
    f = open("001.txt", "r")
    array=f.readlines()
    i=0
    is_space=True
    #while is_space:
    while i<len(array):
        # s=input()
        # is s='':
        array[i]=remove_newline(array[i])
        print(array[i][0])
        # while(array[i][0]!='#')
        #     yield array[i]
        #
        i=i+1
    f.close()

def main():
    
    print(chain(range(0, 4), range(4, 8)))
    print(list(chain(range(0, 4), range(4, 8))))
    #chain2(range(0, 4), range(4, 8))

    print(chain2(range(0, 4), range(4, 8)))
    print(list(chain2(range(0, 4), range(4, 8))))

    print(compress(["Ivo", "Rado", "Panda"], [False, False, True]))
    print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))

    print(cycle(range(0,10)))
    print(list(cycle(range(0,10))))
    endless = cycle(range(0,10))
    for item in endless:
        print(item)

    print('================')
    lines=list(book_reader())
    for item in lines:
        print(item)
    #book_reader()
if __name__=='__main__':
    main()



