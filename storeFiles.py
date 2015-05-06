#!/usr/bin/env python

# 4/24/2015
# Functions to encrypt/decrypt files to store on Google Drive

import os, hashlib, re
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from random import randint
from shutil import move

# INPUT: drive for data storage, file to be encrypted
# OUTPUT: private key or "FILEDNE" if file doesn't exist
# Encrypts the file to be stored on google drive
def encryptFileForDrive(DRIVE, encryptFile):
    if os.path.exists(encryptFile):
        privateKey = RSA.generate(1024)
        key = privateKey.publickey()
        cipher = PKCS1_OAEP.new(key)
        file = open(encryptFile, 'rb')
        randNum = randint(2**16, 2**32)
        randFile = DRIVE + r'SecurityFolder\\' + str(randNum) + '.txt'
        outputFile = open(randFile, 'wb')
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
            if filePath == encryptFile:
                os.remove(DRIVE + 'SecurityFolder\\' + fileNum.strip() + '.txt')
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
        return privateKey#, randFile #testing purposes
    else:
        return "FILEDNE"

# INPUT: drive for data storage, path of randFile, private key
# OUTPUT: "FILEDNE" if file does not exist
# Decrypts the file when retrieved from the google drive.
def decryptFileForDrive(DRIVE, randFile, key):

    # retrieve output file name
    outputFileName = ''
    indexFile = open(DRIVE + r'SecurityFolder\index.txt', 'r')
    tempFile = open(DRIVE + r'SecurityFolder\dump', 'w')
    for line in indexFile:
        filePath, spacer, fileNum = line.partition(' - ')
        fileNum = DRIVE + r'SecurityFolder\\' + fileNum + '.txt'
        if fileNum == randFile:
            outputFileName = filePath
        else:
            # handles removing the selected filepath
            tempFile.write(line)
    tempFile.close()
    indexFile.close()
        
    # decrypt the file
    if os.path.exists(randFile):
        cipher = PKCS1_OAEP.new(key)
        file = open(randFile, 'rb')
        outputFile = open(outputFileName, 'wb')
        # 128 because 2 encrypted char = 1 unencrypted char
        message = file.read(128)
        while message != b'':
            outputFile.write(cipher.decrypt(message))
            message = file.read(128)
        file.close()
        outputFile.close()
    else:
        return "FILEDNE"

    # rename dump file to index
    os.remove(DRIVE + r'SecurityFolder\index.txt')
    move(DRIVE + r'SecurityFolder\dump', DRIVE + r'SecurityFolder\index.txt')
    #remove unnecessary file
    os.remove(randFile)
    

##def main():
##    key, randFile = encryptFileForDrive("C:\\", 'C:\\Users\\Jarid\\HashFolder\\a.txt')
##    decryptFileForDrive("C:\\", randFile, key)
##
##if __name__ == "__main__":
##    main()

