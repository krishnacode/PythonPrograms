#!C:/ProgramFiles/Python
#Copyright Codus

import sys

def main():
    a=2
    b=5
    print("Original",a,b)
    (a,b)=(b,a)   #tuple
    print("Final",a,b)
    

if __name__ == '__main__':
    main()
