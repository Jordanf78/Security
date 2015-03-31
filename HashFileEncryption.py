#!/usr/bin/env python

# 3/28/2015
# Handles the dictionary produced from the file hashing functions and
# handles the encryption of this file to be sent to the drive.

import os, hashlib
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# INPUT: dictionary (dict[filename] = hash)
# OUTPUT: N/A
# The filenames and hashes are stored in a file line by line.
def storeHashes(hashDict):
    while(not os.path.exists(r'C:\SecurityFolder')):
        os.makedirs(r'C:\SecurityFolder')
    file = open('C:\SecurityFolder\HashFile.txt', 'w')
    for i in hashDict.keys():
        # filename - hash
        string = i + ' - ' + str(hashDict[i] + '\n')
        file.write(string)
    file.close()

# INPUT: hash dict file
# OUTPUT: private key or "FILEDNE" if file doesn't exist
# The hash dict file is encrypted for transfer to the google drive.
def encryptFile(hashFile):
    if os.path.exists(hashFile):
        privateKey = RSA.generate(1024)
        key = privateKey.publickey()
        cipher = PKCS1_OAEP.new(key)
        file = open(hashFile, 'r+b')
        outputFile = open('C:\SecurityFolder\Encrypted.txt', 'w+b')
        for line in file:
            outputFile.write(cipher.encrypt(line))
        file.close()
        outputFile.close()
        return privateKey
    else:
        return "FILEDNE"

# INPUT: file, private key
# OUTPUT: N/A
# Decrypts the file when retrieved from the google drive.
def decryptFile(encryptedFile, key):
    if os.path.exists(encryptedFile):
        cipher = PKCS1_OAEP.new(key)
        file = open(encryptedFile, 'r+b')
        outputFile = open('C:\SecurityFolder\Decrypted.txt', 'w+b')
        message = file.read(1024)
        while message != b'':
            outputFile.write(cipher.decrypt(message))
            message = file.read(1024)
        file.close()
        outputFile.close()

def main():
    d = {'C:\\Users\\Jarid\\HashFolder\\HashSubFolder\\b.txt': '81dc9bdb52d04dc20036dbd8313ed055', 'C:\\Users\\Jarid\\HashFolder\\a.txt': '912ec803b2ce49e4a541068d495ab570'}
    storeHashes(d)
    key = encryptFile(r'C:\SecurityFolder\HashFile.txt')
    decryptFile(r'C:\SecurityFolder\Encrypted.txt', key)

if __name__ == "__main__":
    main()
