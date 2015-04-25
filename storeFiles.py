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
        outputFile = open(str(randNum) + '.txt', 'wb')
        message = file.read(64)
        while message != b'':
            # use public key to encrypt 64 char messages from hashFile
            outputFile.write(cipher.encrypt(message))
            message = file.read(64)
        file.close()
        outputFile.close()
        indexFile = open(DRIVE + r'SecurityFolder\index.txt', 'w')
        indexFile.write(encryptFile + ' - ' + str(randNum))
        indexFile.close()
    else:
        return "FILEDNE"


def main():
    exist = encryptFileForDrive("C:\\", 'C:\\Users\\Jarid\\HashFolder\\a.txt')
    print(exist)

if __name__ == "__main__":
    main()

