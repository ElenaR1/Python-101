# cat2.py
import sys
from cat import cat


def cat2(arguments):
    n=len(arguments)
    print(arguments)
    print(n)
    for i in range(1,n):
        cat(arguments[i])


def main():
    cat2(sys.argv)

if __name__ == '__main__':
    main()