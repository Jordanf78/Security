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

# INPUT: path of the folder
# OUTPUT: List of files
# Get a list of files to be hashed.
def loadFolderContent(folderPath):
    folderList = os.listdir(folderPath)
    returnList = []
    for i in folderList:
        path = folderPath + i
        # if it is a file, add to list for hashing
        if os.path.isfile(path):
            returnList.append(path)
        # if it is a subfolder, find its file paths
        elif os.path.isdir(path):
            subfolderList = []
            subfolderList = loadFolderContent(path)
            returnList += subfolderList
    return returnList
    

# INPUT: Folder path
# OUTPUT: Dictionary with paths and their hashes
# Helps to simplify
def hashCollector(folderPath):
    hashFileDict = {}
    fileList = loadFolderContent(folderPath)
    for i in fileList:
        ourHash = fileHasher(folderPath + i)
        hashFileDict[folderPath+i] = ourHash
    return hashFileDict

# for specifying drive
# http://stackoverflow.com/questions/827371/is-there-a-way-to-list-all-the-available-drive-letters-in-python
##
##def main():
##    #these files need to be either raw strings or contain \\ instead
##
##if __name__ == "__main__":
##    main()
