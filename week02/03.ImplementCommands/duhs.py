# duhs.py
import os
from cat import cat


def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

# generates the file names in a directory tree by walking the tree either top-down or bottom-up.
def walk():
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))

def main():
    #duhs(sys.argv)
    #walk()
    print(sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)))#os.path.getsize - Gives the size in bytes




if __name__ == '__main__':
    main()