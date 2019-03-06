#HOW TO WORK WITH ARGUMENTS. WHAT WE WRITE IN THE CONSOLE:  python snd.py one two three snd.py is the 0 arg one the first two-2nd and 3-third

import sys

def do_something(x, y, z='ZAZAZAZA'):
    print ('x:', x)
    print ('y:', y)
    print ('z:', z)

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    do_something(*sys.argv[1:])

def printt(x,y):
    print("----",x)
    print ("----",y)

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    printt(*sys.argv[2:])# if there are 3 args otherwise ->error


# Let's run this with three arguments:

# $ python dosomething.py one twoo three
# x: one
# y: twoo
# z: three
# Run it with two arguments and Python will assign a default value for the third:

# $ python dosomething.py one twoo
# x: one
# y: twoo
# z: ZAZAZAZA
