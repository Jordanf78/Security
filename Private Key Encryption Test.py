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
    if os.path.exists(r'C:\CryptoFile'):
        return
    else:
        #want to define specific directory here instead of storing locally
        file = open('CryptoFile', 'w+b')
        file.write(vector)
        file.write(b'|||||')
        file.write(encrypted)

# INPUT: N/A
# OUTPUT: Encrypted Private Key and Vector
# Extracts the private key and vector from the file for decryption.
def removeFromFile():
    file = open('CryptoFile', 'rb')
    data = str(file.read())
    return data.partition('|||||')[::2]

def main():
    message, vector = encryptKey(b'passwordpassword', b'PRIVATEKEY')
    print(vector, message)
    privateKey = decryptKey(b'passwordpassword', vector, message)
    print(privateKey)
    storeInFile(vector, message)
    a,b = removeFromFile()
    print(a,b)
# Want to change directories for file

if __name__ == "__main__":
    main()
