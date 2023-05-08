import hashlib
import os

def create_account():
    username = input("Enter username: ")
    password = input("Enter password: ")
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    with open("accounts.txt", "a") as f:
        f.write(f"{username}:{password_hash}\n")
    os.makedirs("home/"+username)
    return True # = "Account created successfully!"

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    with open("accounts.txt", "r") as f:
        for line in f:
            if line.strip().startswith(username):
                if line.strip().split(":")[1] == password_hash:
                    os.chdir("home/"+username)
                    return (True,username) # = "Login successful!"
                else:
                    return False # = Incorrect password!
        return False # = "Username not found!"
    
    
