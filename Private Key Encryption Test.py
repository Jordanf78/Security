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

# INPUT: Vector for encryption and encrypted key
# OUTPUT: N/A
# Stores encrypted private key and vector in a file.
def storeInFile(vector, encrypted):
    makeSecurityFolder()
    file = open('C:\SecurityFolder\CryptoFile', 'w+b')
    file.write(vector)
    file.write(b'|||||')
    file.write(encrypted)
    

# INPUT: N/A
# OUTPUT: Encrypted Private Key and Vector or "FILEDNE" if no file exists
# Extracts the private key and vector from the file for decryption.
def removeFromFile():
    if os.path.exists(r'C:\SecurityFolder\CryptoFile'):
        file = open('C:\SecurityFolder\CryptoFile', 'rb')
        data = str(file.read())
        return data.partition('|||||')[::2]
    else:
        return "FILEDNE"

# INPUT: N/A
# OUTPUT: N/A
# Makes a folder for the program to store files in, if one doesn't exist.
def makeSecurityFolder():
    if not os.path.exists(r'C:\SecurityFolder'):
        os.makedirs(r'C:\SecurityFolder')

def main():
    message, vector = encryptKey(b'passwordpassword', b'PRIVATEKEY')
    print(vector, message)
    privateKey = decryptKey(b'passwordpassword', vector, message)
    print(privateKey)
    storeInFile(vector, message)
    a,b = removeFromFile()
    print(a,b)

if __name__ == "__main__":
    main()
