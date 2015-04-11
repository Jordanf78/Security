#!/usr/bin/env python

# 3/7/2015
# Function that will handle storing the private key on a system.

from Crypto.Cipher import AES
from Crypto import Random
import os

# INPUT: password for cipher, privateKey for asymmetric hash
# OUTPUT: encrypted message and vector used for seed
# Encrypts the private key. All I/O is in bytes object form.
def encryptKey(password, privateKey):
    vector = Random.new().read(AES.block_size)
    cipher = AES.new(password, AES.MODE_CFB, vector)
    message = cipher.encrypt(privateKey)
    return message, vector

# INPUT: password for cipher, vector used in encryption, encrypted text
# OUTPUT: private key
# Decrypts the private key. All I/O in bytes object form.
def decryptKey(password, vector, encrypted):
    cipher = AES.new(password, AES.MODE_CFB, vector)
    privateKey = (cipher.decrypt(encrypted))
    return privateKey

# INPUT: Vector for encryption, encrypted key, and hard drive letter
# OUTPUT: N/A
# Stores encrypted private key and vector in a file.
def storeInFile(vector, encrypted, DRIVE):
    makeSecurityFolder(DRIVE)
    file = open(DRIVE + r'SecurityFolder\CryptoFile.txt', 'w+b')
    file.write(vector)
    file.write(b'|||||')
    file.write(encrypted)
    file.close()
    

# INPUT: hard drive letter
# OUTPUT: Encrypted Private Key and Vector or "FILEDNE" if no file exists
# Extracts the private key and vector from the file for decryption.
def removeFromFile(DRIVE):
    if os.path.exists(DRIVE + r'SecurityFolder\CryptoFile.txt'):
        file = open(DRIVE + r'SecurityFolder\CryptoFile.txt', 'rb')
        data = str(file.read())
        file.close()
        return data.partition('|||||')[::2]
    else:
        return "FILEDNE"

# INPUT: hard drive letter
# OUTPUT: N/A
# Makes a folder for the program to store files in, if one doesn't exist.
def makeSecurityFolder(DRIVE):
    if not os.path.exists(DRIVE + r'SecurityFolder'):
        os.makedirs(DRIVE + r'SecurityFolder')

##def main():
##    message, vector = encryptKey(b'passwordpassword', b'PRIVATEKEY')
##    print(vector, message)
##    privateKey = decryptKey(b'passwordpassword', vector, message)
##    print(privateKey)
##    storeInFile(vector, message, 'C:\\')
##    a,b = removeFromFile('C:\\')
##    print(a,b)
##
##if __name__ == "__main__":
##    main()
