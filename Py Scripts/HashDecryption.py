#!/usr/bin/env python

# 3/28/2015
# Handles the dictionary produced from the file hashing functions and
# handles the encryption of this file to be sent to the drive.

import os, hashlib, re
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA



# INPUT: drive for data storage, dictionary (dict[filename] = hash)
# OUTPUT: N/A
# The filenames and hashes are stored in a file line by line.
def storeHashes(DRIVE, hashDict):
    while(not os.path.exists(DRIVE + r'SecurityFolder')):
        os.makedirs(DRIVE + r'SecurityFolder')
    file = open(DRIVE + r'SecurityFolder\HashFile.txt', 'w')
    for i in hashDict.keys():
        # filename - hash
        string = i + ' - ' + str(hashDict[i] + '\n')
        file.write(string)
    file.close()

# INPUT: DRIVE
# OUTPUT: hashDict or FILEDNE if path is not found
# return the hashDict we stored in the file previously
def readHashes(DRIVE):
    if(os.path.exists(DRIVE + r'SecurityFolder\HashFile.txt')):
        file = open(DRIVE + r'SecurityFolder\HashFile.txt', 'r')
        hashDict = {}
        for line in file:
            file, spacer, hashValue = line.partition(" - ")
            hashDict[file] = hashValue
        return hashDict
    else:
        return "FILEDNE"


# INPUT: drive for data storage, file, private key
# OUTPUT: "FILEDNE" if file does not exist
# Decrypts the file when retrieved from the google drive.
def decryptFile(DRIVE, encryptedFile, key):
    path = DRIVE + encryptedFile
    if os.path.exists(path):
        cipher = PKCS1_OAEP.new(key)
        file = open(path, 'rb')
        outputFile = open(DRIVE + r'SecurityFolder\Decrypted.txt', 'wb')
        # 128 because 2 encrypted char = 1 unencrypted char
        message = file.read(128)
        while message != b'':
            outputFile.write(cipher.decrypt(message))
            message = file.read(128)
        file.close()
        outputFile.close()
    else:
        return "FILEDNE"

##def main():
##    d = {'C:\\Users\\Jarid\\HashFolder\\HashSubFolder\\b.txt': '81dc9bdb52d04dc20036dbd8313ed055', 'C:\\Users\\Jarid\\HashFolder\\a.txt': '912ec803b2ce49e4a541068d495ab570'}
##    storeHashes('C:\\', d)
##    print(readHashes('C:\\'))
##    key = encryptFile('C:\\', r'C:\SecurityFolder\HashFile.txt')
##    decryptFile('C:\\', r'SecurityFolder\Encrypted.txt', key)
##
##if __name__ == "__main__":
##    main()
