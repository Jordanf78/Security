#!/usr/bin/env python

# 2/8/15
# Functions that handle hashing a file, searching a folder for all files of
# that folder and it's subdirectories, and a utility function to combine the
# file list into a dictionary with each file's hash.

import hashlib, os

# Global Variable(s) 
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

# for specifying drive
# http://stackoverflow.com/questions/827371/is-there-a-way-to-list-all-the-available-drive-letters-in-python
##
##def main():
##    print(hashCollector(r"C:\Users\Jarid\HashFolder"))
##
##if __name__ == "__main__":
##    main()
