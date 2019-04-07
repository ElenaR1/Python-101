import operator

class CustomError(Exception):
    pass

def gcd(nom, denom):
        while denom != 0:
            t = denom
            denom = nom%denom
            nom = t
        return nom


def simplify_fraction(fraction):
        if not isinstance(fraction,tuple):#the same way for zero
            raise Exception('not a tuple')
        #print(fraction,fraction[1],type(fraction[1]))
        if fraction[1] in [0]:
            raise CustomError('you should use another denominator')
        x=fraction[0]
        y=fraction[1]

        if x==y:
            return (1,1)
        if y == 1:
            return (x,1)
        else:
            g=gcd(x,y)
            x=x/g
            y=y/g
            return(x,y)   

def collect_fractions(fractions):
    #print(fractions[0][1])
    nom1=fractions[0][0]
    nom2=fractions[1][0]
    denom1=fractions[0][1]
    denom2=fractions[1][1]
    g = gcd(denom1, denom2);
    lcm=(denom1*denom2)/g
    new_nom=(nom1*(lcm/denom1)+nom2*(lcm/denom2))
    (new_nom,lcm)=simplify_fraction((new_nom,lcm))
    return (new_nom,lcm)



def bubblesort(list):

# Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp


# list = [19,2,31,45,6,11,121,27]
# bubblesort(list)
# print(list)


def sort_fractions(fractions):
    #print(fractions)
    division_arr=[]
    n=len(fractions)
    for i in range(n):
        res=fractions[i][0]/fractions[i][1]
        #print(fractions[i], res)
        division_arr.append(res)

    for iter_num in range(n-1,0,-1):
        for idx in range(iter_num):
            if division_arr[idx]>division_arr[idx+1]:
                temp = fractions[idx]
                fractions[idx] = fractions[idx+1]
                fractions[idx+1] = temp

                temp = division_arr[idx]
                division_arr[idx] = division_arr[idx+1]
                division_arr[idx+1] = temp
    #print(division_arr)
    return fractions
                          
#print(simplify_fraction((54,0)))
print(simplify_fraction((54,24)))
print(simplify_fraction((3,9)))
print(simplify_fraction((1,7)))
print(simplify_fraction((4,10)))
print(simplify_fraction((63,462)))
print('-------------')
print(collect_fractions([(1,7),(2,6)]))#(10,21)
print(collect_fractions([(1, 4), (1, 2)]))#(3, 4)
print(collect_fractions([(1, 10), (2, 20)]))#(1.0, 5.0)

print('-------------')
print(sort_fractions([(2, 3), (1, 2)]))
print(sort_fractions([(2, 3), (1, 2), (1, 3)]))#[(1, 3), (1, 2), (2, 3)]
print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))