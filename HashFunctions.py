#!/usr/bin/env python

# 2/8/15
# Functions that handle hashing a file, searching a folder for all files of
# that folder and it's subdirectories, and a utility function to combine the
# file list into a dictionary with each file's hash.

import hashlib, os, re

# Global Variable
BUFFER = 65536

# INPUT: Path of a file
# OUTPUT: Hash of input file
# This function takes the path of a file and returns that files hash.
def fileHasher(path):
    ourHash = hashlib.md5()
    file = open(path, 'rb')
    while True:
        text = file.read(BUFFER)
        if not text: # text is empty
            break
        ourHash.update(text)
    file.close()
    return ourHash.hexdigest() 

# INPUT: Path of a folder
# OUTPUT: List of file paths
# Input a folder path and return all files of that folder and its possible
# subdirectories.
def loadFolderContent(folderPath):
    folderList = os.listdir(folderPath)
    returnList = []
    for i in folderList:
        path = folderPath + '\\' + i
        # if it is a file, add to list for hashing
        if os.path.isfile(path):
            returnList.append(path)
        # if it is a subfolder, find its file paths
        elif os.path.isdir(path):
            returnList += loadFolderContent(path)
    return returnList
    

# INPUT: Folder path
# OUTPUT: Dictionary of file paths and their hashes
# Function to find all files of a folder and subdirectories and to hash all of
# these files and return the dictionary containing this information.
def hashCollector(folderPath):
    hashFileDict = {}
    fileList = loadFolderContent(folderPath)
    for i in fileList:
        ourHash = fileHasher(i)
        hashFileDict[i] = ourHash
    return hashFileDict

# INPUT: 2 dictionaries with hashes
# OUTPUT: list of file names that have changed
# Compares the hashes of two dictionaries and 
def compareHashes(newHashDict, oldHashDict):
    unmatchedHashList = []
    for i in newHashDict.keys():
        # check if file has been hashed before
        if oldHashDict[i] != None:
            # hashes match?
            if oldHashDict[i] != newHashDict[i]:
                unmatchedHashList.append(i)
    return unmatchedHashList
                
##def main():
##    a = hashCollector(r"C:\Users\Jarid\HashFolder")
##    b = {'C:\\Users\\Jarid\\HashFolder\\HashSubFolder\\b.txt': '81dc9bdb52d04dc20036dbd8313ed055', 'C:\\Users\\Jarid\\HashFolder\\a.txt': '912ec803b2ce49e4a541068d495ab570'}
##    print(a,b)
##    print(compareHashes(a, b))
##
##if __name__ == "__main__":
##    main()
