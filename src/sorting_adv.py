#!C:/ProgramFiles/Python
#Copyright Codus

import sys


def compare(v):
    if type(v) is int:
        return v
    else:
        sum=ord(v[:1])
        return 10000+sum  #say 10000 is infinty


       

def main():
    a=[1,1,5,0,8,"aaaa","bbbb","c"]
    a=sorted(a,key=compare)
    for s in a:
        print(s)


    

if __name__ == '__main__':
    main()

