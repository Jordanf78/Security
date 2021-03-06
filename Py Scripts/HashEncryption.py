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

# INPUT: drive for data storage, hash dict file (absolute path w/ drive letter)
# OUTPUT: private key or "FILEDNE" if file doesn't exist
# The hash dict file is encrypted for transfer to the google drive.
def encryptFile(hashFile):
    if os.path.exists(hashFile):
        privateKey = RSA.generate(1024)
        key = privateKey.publickey()
        cipher = PKCS1_OAEP.new(key)
        file = open(hashFile, 'rb')
        outputFile = open("..\Program Data\EncryptedHash", 'wb')
        message = file.read(64)
        while message != b'':
            # use public key to encrypt 64 char messages from hashFile
            outputFile.write(cipher.encrypt(message))
            message = file.read(64)
        outputFile.close()
        file.close()
        os.remove(hashFile)
        # for decryption
        return privateKey
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

def main():
    encryptFile()
    return

main()
