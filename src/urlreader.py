#!C:/ProgramFiles/Python
#Copyright Codus

import sys

import urllib
import urllib.request
def urlreader(url):
    ufile=urllib.request.urlopen(url)
    print("Url Information")
    for key in ufile.info():
        print(ufile.info()[key],"\n")
    print(ufile.geturl())

def main():
    if len(sys.argv)<1:
        print("Usage filename url1 [url2 ]")
        sys.exit(1)
    else:
        for i in sys.argv[1:]:
            urlreader(i)
    print("i am done")

if __name__ == '__main__':
    main()
