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

# INPUT: Path of a folder
# OUTPUT: List of directories
# Get a list of the files in a directory to be hashed.
def loadFolderContent(folderPath):
    folderList = os.listdir(folderPath)

# can use this instead to search subdirectories, depends on
# how we want to setup hashable files and subdirectories
# root = pathlib.Path('some/path/here')
# non_empty_dirs = {str(p.parent) for p in root.rglob('*') if p.is_file()}
    

# INPUT: Folder path
# OUTPUT: Dictionary with paths and their hashes
# Helps to simplify
def hashCollector(folderPath):
    hashFileDict = {}
    fileList = loadFolderContent(folderPath)
    for i in fileList:
        # combines folder path with file name
        ourHash = fileHasher(folderPath + r'\\' + i)
        hashFileDict[folderPath+i] = ourHash
    return hashFileDict

def main():
    #these files need to be either raw strings or contain \\ instead
    testFile = FileHasher('c:\Users\Jarid\a.txt')
    print(randomFile.digest())

if __name__ == "__main__":
    main()
