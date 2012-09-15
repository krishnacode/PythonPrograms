#!C:/ProgramFiles/Python
#Copyright Codus

import sys
def merge(arr,low,mid,high):
    i=low
    j=mid+1
    while(i<=mid and j<=high):
        if(arr[i]>arr[j]):
            (arr[i],arr[j])=(arr[j],arr[i])
            i=i+1
        else:
            j=j+1
        

def main():
    arr=[1,2,4,0,3,9]
    merge(arr,0,2,4)
    for i in arr:print(i)

if __name__ == '__main__':
    main()
