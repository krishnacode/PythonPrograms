#!C:/ProgramFiles/Python
#Copyright Codus

import sys
def gcd(m,n):
    while(n!=0):
        rem=m%n
        m=n
        n=rem
    return m

def main():
    m=4
    n=8
    print("GCD of ",m,n,"is",gcd(m,n),sep=' ')
    m=1
    n=8
    print("GCD of ",m,n,"is",gcd(m,n),sep=' ')
    m=40
    n=84
    print("GCD of ",m,n,"is",gcd(m,n),sep=' ')

if __name__ == '__main__':
    main()
