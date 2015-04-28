#!/usr/bin/env python

# 4/24/2015
# Functions to encrypt/decrypt files to store on Google Drive

import os, hashlib, re
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from random import randint

# INPUT: drive for data storage, file to be encrypted
# OUTPUT:  "FILEDNE" if file doesn't exist
# 
def encryptFileForDrive(DRIVE, encryptFile):
    if os.path.exists(encryptFile):
        privateKey = RSA.generate(1024)
        key = privateKey.publickey()
        cipher = PKCS1_OAEP.new(key)
        file = open(encryptFile, 'rb')
        randNum = randint(2**16, 2**32)
        outputFile = open(DRIVE + r'SecurityFolder\\' + str(randNum) + '.txt', 'wb')
        message = file.read(64)
        while message != b'':
            # use public key to encrypt 64 char messages from hashFile
            outputFile.write(cipher.encrypt(message))
            message = file.read(64)
        file.close()
        outputFile.close()
        # check for same file name
        indexFile = open(DRIVE + r'SecurityFolder\index.txt', 'r')
        tempFile = open(DRIVE + r'SecurityFolder\dump', 'w')
        for line in indexFile:
            filePath, spacer, fileNum = line.partition(' - ')
            # dont copy old file name
            print(filePath, fileNum)
            if filePath == encryptFile:
                os.remove(DRIVE + r'SecurityFolder\\' + fileNum.strip() + '.txt')
            else:
                tempFile.write(line)
        indexFile.close()
        tempFile.close()
        # now done storing data temporarily, can move back to index file
        indexFile = open(DRIVE + r'SecurityFolder\index.txt', 'w')
        tempFile = open(DRIVE + r'SecurityFolder\dump', 'r')
        for line in tempFile:
            indexFile.write(line + '\n')
        indexFile.write(encryptFile + ' - ' + str(randNum))
        indexFile.close()
        tempFile.close()
        os.remove(DRIVE + r'SecurityFolder\dump')
    else:
        return "FILEDNE"


def main():
    exist = encryptFileForDrive("C:\\", 'C:\\Users\\Jarid\\HashFolder\\a.txt')
    print(exist)

if __name__ == "__main__":
    main()

