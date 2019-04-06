# generate_numbers.py test it with test.txt
import sys

from random import randint
from cat import cat

def generate_numbers(filename, numbers):
    f= open(filename,"w+")
    for i in range(int(numbers)-1):
        f.write(str(randint(1, 1000))+" ")
    f.write(str(randint(1, 1000)))


def main():
    print(sys.argv[1],sys.argv[2])
    generate_numbers(sys.argv[1],sys.argv[2])
    cat(sys.argv[1])


if __name__ == '__main__':
    main()
    #print(randint(1, 5))