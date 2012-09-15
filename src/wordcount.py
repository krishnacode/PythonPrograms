#!C:/ProgramFiles/Python
#Copyright Codus
import re
import sys
def wordcount(filename):
    hashtable={}
    pat=re.compile(r'\s|\:|\(|\)|\,|\'|\"|\'|[@#$!%^&*()\-=+/\\.\|_\[\]\{\}\(\)\;\:]');
    fhandle=open(filename,'rU')
    for line in fhandle:
        for word in pat.split(line):
            if word.lower() in hashtable.keys():
                hashtable[word]=hashtable[word]+1
            else:
                hashtable[word.lower()]=1

    for key,val in hashtable.items():
        if len(key)==0:
            print("Null Count"," ----- ",val)
        else:
            print(key," ----- ",val)
        
        
    

def main():
    for arg in sys.argv:
        wordcount(arg)
        print("")
        
    
    

if __name__ == '__main__':
    main()
