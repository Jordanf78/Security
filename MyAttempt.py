#!/usr/bin/env python

# 2/8/15
# Create a function that accepts a file's path, hashes the file,
# and returns its hash.

import hashlib, os

# Global Variable(s) 
BUFFER = 65536

# INPUT: filepath 
# OUTPUT: hash
# Gives a hash for a given file
def fileHasher(path):
    hash = hashlib.md5()
    file = open(path.encode('unicode-escape'), 'rb')
    while True:
        text = file.read(BUFFER)
        if not text:
            break
        hash.update(text)
    file.close()
    return hash.digest() 

# INPUT: 2 hashes
# OUTPUT: True/False
# Gives truth value to hash value comparison
def compareHashes(hash1, hash2):
    return hash1 == hash2

# INPUT: N/A
# OUTPUT: List of directories
# Get a list of the directories for files to be hashed.
def loadDirectories():
    

# INPUT
# OUTPUT:
# 

def main():
    #these files need to be either raw strings or contain \\ instead
    testFile = FileHasher('c:\Users\Jarid\a.txt')
    print(randomFile.digest())

if __name__ == "__main__":
    main()
