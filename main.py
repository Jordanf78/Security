###Imports###
import hashlib
import sys
import os

###Universal Variables###
BLOCKSIZE = 65536
hasher = hashlib.md5()

#Loads the text file containing the list of filepaths to be observed
def load_watchlist():
    filelist = []
    configpath = "Program Data\watchlist.txt"
    with open(configpath) as f:
        for line in f:
            filelist.append(line)
    return filelist

#Loads items from the filelist into a recursive call of calc_hash
#Compiles all hashs with corrosponding filepath to a list of list
#[[file1,hash1],[file2,hash2]...]
def compile_hashs(filelist):
    hasharray = []
    i = 0
    while i < len(filelist):
        print (str(filelist[i]))
        hash1 = calc_hash(str(filelist[i]))
        hasharray = hasharray + [filelist[i],hash1]
        i+=1
    file = open("Program Data\hashdb.txt","w")
    x = 0
    while x < len(hasharray):
        tmpstr = str(hasharray[x])+ ","+str(hasharray[x+1]+"\n")
        file.write(tmpstr)
        x+=2
    file.close()
    print (hasharray)
    return hasharray

def read_hashdb():
    oldhasharray = []

#Compares two hashes and returns yes or no
def compare_hash(hash1,hash2):
    if hash1 == hash2:
        print("yes")
    else:
        print ("no")

#calculate the hash for a given filepath
def calc_hash(filepath):
    print (filepath)
    with open(str(filepath[:-1]),'rb') as infile:
        buf = infile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = infile.read(BLOCKSIZE)

    return(hasher.hexdigest())

#The main function contains the calls neccesary to initialize the program
#On start -> load filelist -> generate hashes -> load old hashes -> compare new and old hashes
#If changes are found, notify user. else start timer and wait for refresh. 
def main():
    filelist = load_watchlist()
    #path = r'C:\Users\Jordan\Desktop\Test\Text.txt'
    #filelist = [r'C:\Users\Jordan\Desktop\Test\Text.txt',r'C:\Users\Jordan\Desktop\Test\Image.bmp',r'C:\Users\Jordan\Desktop\Test\ZIP.zip']
    hasharray = compile_hashs(filelist)
    print(hasharray)
    
    



main()
