class Zoo:
    def __init__(self):
        # self.index=0
        self.animals=[]

    def add_animal(self,animal_name):
        self.animals.append(animal_name)

    #get_item e drg nachin po koito da obikalqme, no tezi otdolu  sa s po-visok prioritet
    def __iter__(self):
        self.index=0
        return self

    def __next__(self):
        index=self.index
        self.index+=1
        # try:
        return self.animals[index]
        # except IndexError:
        #     raise StopIteration

def odd_nums():
    start=1
    while start < 20:
        yield start
        start+=2
        print('==========')
        yield 1




z=Zoo()
z.add_animal('zebra')
z.add_animal('lion')
z.add_animal('tiger')
z.add_animal('elephant')


i=iter(z)
print(next(i))
print(next(i))

gen=odd_nums()
for el in gen:
    print('between el')# kolkoto yield-a imame tolkova puti cikli
    print(el)