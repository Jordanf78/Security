#!/usr/bin/env python

# 2/8/15
# Create a function that accepts a file's path, hashes the file,
# and returns its hash.

import hashlib

BUFFER = 65536

def FileHasher(path):
    hash = hashlib.md5()
    file = open(path, 'rb')
    while True:
        text = file.read(BUFFER)
        if not text:
            break
        hash.update(text)
    file.close()
    return hash

def main():
    #these files need to be either raw strings or contain \\ instead
    testFile = FileHasher(r'c:\Users\Jarid\a.txt')
    print(randomFile.digest())

if __name__ == "__main__":
    main()
