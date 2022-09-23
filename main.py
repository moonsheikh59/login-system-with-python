import bcrypt

login = {}
with open("data.txt", "r") as file:
    lines = file.readlines()
    #print(len(lines))
    for i in range(0,len(lines),3):
        username = lines[i][:-1]
        salt = lines[i + 1][:-1] 
        hashed = lines[i+2][:-1] 
        login[username] = (salt,hashed)
#print(login)

have_an_account = input("Do you have an account (Y/N) please select one option:-")

if have_an_account.lower() == "y":

    print("LOGIN")
    user_name = input("enter your username:-")
    pass_word = input("enter your password:-").encode()
    if user_name in login:
        hashed = login[user_name][1]
        hashed = str(hashed).encode() 
        if bcrypt.checkpw(pass_word, hashed):
            print("Login success!")
            print(f"Hi{user_name}")
        else:
             print("wrong password")
    else:
        print("please register first")
elif have_an_account.lower() == "n":
    print("Please register")
    user_name = input("enter username:-")
    pass_word = input("enter password:-").encode()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pass_word, salt)
    salt = salt.decode()
    hashed = hashed.decode()
    if user_name not in login:
        with open("data.txt",'a') as read:
            read.write(f"Username :- {user_name}\nSalt:-{salt}\nHashed :-{hashed}\n")
        print("Your account is successfully created")
    else:
         print("user already exists")
else:
     print("Invalid Key")