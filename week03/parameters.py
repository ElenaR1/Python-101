def simple_addition(num1,num2):
    answer=num1+num2
    print('num1 is',num1)
    print(answer)

print(simple_addition(5,3))
print(simple_addition(num2=4,num1=6))


def simple(num1,num2=2):
    answer=num1+num2
    print('num2 is',num2)
    print(answer)

print(simple(5))
print(simple(3,5))

print('----------------------')


def f(farg, *args):
    print("formal arg:{}".format(farg))
    for arg in args:
        print("another arg:{}".format(arg))


f(1, "two", 3)
# formal arg: 1
# another arg: two
# another arg: 3

def ff(arg,*args):
    sum=0
    for i in range(len(args)):
        sum+=args[i]
    sum+=arg
    print(sum)

ff(20,1,2,3)

print('-----------')
def test_var_kwargs(farg, **kwargs):
    print("formal arg:{}".format(farg))
    for key in kwargs:
        print ("another keyword arg: {}={}".format(key, kwargs[key]))

test_var_kwargs(farg=1, myarg2="two", myarg3=3)

# formal arg:1
# another keyword arg: myarg3=3
# another keyword arg: myarg2=two

def cheeseshop(kind, *args, **kwargs):
    print("-- Do you have any {}".format(kind))

    for arg in args:
        print('arg',arg)

    print("-"*40)

    for key in kwargs:
        print("kwarg {}:{}".format(key, kwargs[key]))


cheeseshop("Limburger", "It's very runny, sir.", "It's really VERY runny")
cheeseshop("Limburger", shopkeeper="Michael", client="John", sketch="Cheese Shop Sketch")
