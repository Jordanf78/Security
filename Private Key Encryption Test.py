#!/usr/bin/env python

# 3/7/2015
# Function that will handle storing the private key on a system.

from Crypto.Cipher import AES
from Crypto import Random

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

# INPUT:
# OUTPUT:
# Handles the storage of the private key, password hash...

# INPUT:
# OUTPUT:
# Turns the password into a hashed value

def main():
    message, vector = encryptKey(b'passwordpassword', b'PRIVATEKEY')
    privateKey = decryptKey(b'passwordpassword', 

if __name__ == "__main__":
    main()
