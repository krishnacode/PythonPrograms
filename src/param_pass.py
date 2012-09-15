#!C:/ProgramFiles/Python
#Copyright Codus

import sys
def function(arr):
    arr[0]=2

def main():
    arr=[1,2,4];
    function(arr);
    for i in arr:print(i);
    

if __name__ == '__main__':
    main()
