
def is_number_balanced(number):
    num=str(number)
    l=len(num)
    sum1=0
    sum2=0
    if l==1:
        return True
    if l%2==0:
        half=l//2
        for i in range(half):
            sum1+=int(num[i])
        for i in range(half,l):
            sum2+=int(num[i])
        return sum1==sum2
    elif l%2!=0:
        half=l//2
        for i in range(half):
            sum1+=int(num[i])
        for i in range(half+1,l):
            sum2+=int(num[i])
        return sum1==sum2

    #another way
def is_number_balanced(number):
    num=str(number)
    n=len(num)
    mid=n//2
    l=0
    r=n-1
    sl=0
    sr=0
    while l<r:
        sl+=int(num[l])
        sr+=int(num[r])
        l+=1
        r-=1
    return sl==sr

    
    


def main():
    print(is_number_balanced(9))
    print(is_number_balanced(4518))
    print(is_number_balanced(28471))
    print(is_number_balanced(1238033))

if __name__=='__main__':
    main()
