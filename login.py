from simplecrypt import encrypt, decrypt

def main():
    if input("(1) Login (2) Create User: ") == 1:
        user = input("Username:")
        password = input ("Password:")
        if login(user, password) == True:
             print('success')
        else:
            print('fail')
    else:
        user = input("Username:")
        password = input ("Password:")
        create_user(username, password)
        main()

def create_user(username, password):
    with open(r'Program Data\Users.txt','w+') as f:
        f.write(username+"|"+password)
    return 

def login(username, password):
    success = False
    with open(r'Program Data\Users.txt','r') as f:
        content = f.readlines()
        for line in content:
            if line.split("|")(0) == username:
                if decrypt(line.split("|")(1),ciphertext) == password:
                    success = True
    return success
            

login()
