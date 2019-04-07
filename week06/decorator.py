import datetime
import functools
import time

class TypeError(Exception):
    pass

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")


@my_decorator
def say_whee():
    print("Whee!")

def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    return "Hello "+name





def accepts(*args):
    list_of_types=[type for type in args]
    #print(list_of_types)
    def wrapper(func):
        @functools.wraps(func)
        def decorated_func(*args1):
            for ind,el in enumerate(args1):
                if type(el) != list_of_types[ind]:
                  raise Exception(' Argument 1 of say_hello is not str!')
            #res=func(args1)
            return func(*args1)
        return decorated_func
    return wrapper

@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)
@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True


def log(file_name):
    def wrapper(func):
        @functools.wraps(func)#decorator, which will preserve information about the original function.
        def decorated_func():
            msg=""
            currentDT = datetime.datetime.now()
            msg+=func.__name__+" was called at "+str(currentDT)+'\n'
           #print(msg)# 
            f = open(file_name, "a")
            f.write(msg)
            f.close()
        return decorated_func
    return wrapper


def performance(file_name):
    def wrapper(func):
        @functools.wraps(func)#decorator, which will preserve information about the original function.
        def decorated_func():
            msg=""
            #currentDT = datetime.datetime.now()
            start = time.time()
            res=func()
            end = time.time()
            x = round(end-start, 2)
            msg+=func.__name__+" was called and it took "+str(x)+' seconds to comlete \n'
            print(msg)
            f = open(file_name, "a")
            f.write(msg)
            f.close()
            return res
        return decorated_func
    return wrapper

def encrypt(shift):
    def wrapper(func):
        print('A')
        @functools.wraps(func)
        def decorated_func():
            print('B')
            msg=func()
            encrypted_ms=''
            for ch in msg:
                if ch.isalpha():
                    num=ord(ch)
                    #print(ch,num)
                    num+=shift

                    if ch.isupper():
                        if num > ord('Z'):
                            num-=26
                        elif num < ord('A'):
                            num+=26
                    elif ch.islower():
                        if num > ord('z'):
                            num-=26
                        elif num < ord('a'):
                            num+=26
                    encrypted_ms+=chr(num)
                else:
                    encrypted_ms+=ch
            #return encrypted_ms
            print(encrypted_ms)
        return decorated_func
    return wrapper

@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"
    #return "ATTACKATONCEa/"

@performance('log2.txt')
def something_heavy():
    time.sleep(2)
    return "I am done!"

def main():
    #print(say_hello(4))
    # print(say_hello("Polly"))
    # print(deposit("Roza", 10))

    get_low()   

    #something_heavy()
    # say_whee()
    # greet("World")

if __name__=='__main__':
    main()