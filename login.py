import os.path

def main():
    create_userfile()
    if input("(1) Login (2) Create User: ") == "1":
        user = input("Username:")
        password = input ("Password:")
        if login(user, password) == True:
             print('success')
        else:
            print('fail')
    else:
        user = input("Username:")
        password = input ("Password:")
        create_user(user, password)
        main()

def create_userfile():
    if not os.path.exists(r'Program Data\Users.txt'):
        with open(r'Program Data\Users.txt', 'w') as fout:
            fout.write('')

def create_user(username, password):
    found= False
    with open(r'Program Data\Users.txt','r') as f:
        content = f.readlines()
        for line in content:
            if str(line.split("|")[0]) == username:
                found = True
    if found == False:
        with open(r'Program Data\Users.txt','w+') as f:
            f.write(username+"|"+encrypt(password))
    return

def login(username, password):
    success = False
    with open(r'Program Data\Users.txt','r') as f:
        content = f.readlines()
        for line in content:
            if line.split("|")[0] == username:
                if encrypt(password) == line.split("|")[1]:
                    success = True
    return success
    
def encrypt(text):
    chunk = ""
    for char in text:
        block = 255 - ord(char)
        chunk = chunk + str(block)
    return chunk 
        
main()
