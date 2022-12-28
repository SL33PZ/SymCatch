import shutil
import os
import sys

files =  []


def lll(dirname):
    for name in os.listdir(dirname):
        if name not in (os.curdir, os.pardir):
            full = os.path.join(dirname, name)
            if os.path.isdir(full) and not os.path.islink(full):
                lll(full)
            elif os.path.islink(full):
                files.append(name)

def main(args):
    os.mkdir("SYMLINKS")
    if not args: args = [os.curdir]
    first = 1
    for arg in args:
        if len(args) > 1:
            if not first: print()
            first = 0
            print(arg + ':')
        lll(arg)
        
    for i in files:
        shutil.move(i, "SYMLINKS")
        
    

if __name__ == '__main__':
    main(sys.argv[1:])