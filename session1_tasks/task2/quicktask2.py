import secrets
import string
import hashlib
from getpass import getpass
#credentials_file_path = "/home/desoky/My_Files/Embedded Linux Course/1-Python/Python_Tasks/task2/credentials.txt" #Comment if not used
credentials_file_path = "./credentials.txt"
"""**************************************************************************************************************************************************
Function description:   Function used to generate random password
Arguments:  length of the password, default value = 12
Return: the generated password
**************************************************************************************************************************************************"""
def Generate_random_passwd(passwd_length = 12): #defualt length = 12
    PUNCTUATIONS = "%$#@!&"
    rndm_characters = string.ascii_letters + string.digits + PUNCTUATIONS #Total random characters to be used to make the generated password
    #.join to join empty passwd to the characters #secrets to generate the random password every iteration, in a shorthand for
    passwd = ''.join(secrets.choice(rndm_characters) for i in range(passwd_length)) 
    return passwd
"""**************************************************************************************************************************************************
Function description:   Function used to encrypt the password
Arguments:  password
Return: password encrypted
**************************************************************************************************************************************************"""
def Hash_passwd(passwd):
    #encode the password, then encrypt with SHA1 Algorithm in present them in hexdecimal
    hashed_passwd = hashlib.sha1((passwd.encode('utf-8'))).hexdigest()
    return (hashed_passwd)
"""**************************************************************************************************************************************************
Function description:   Function to save user in credentials file
Arguments:  username, password (hashed)
Return: NONE
**************************************************************************************************************************************************"""
def save_user(username,passwd_hashed):
    file = open(credentials_file_path,"a") #"a" for append
    file.write(f"{username} {passwd_hashed}\n")
    file.close()
"""**************************************************************************************************************************************************
Function description:   Function to check wether the user is exists on the system or not
Arguments:  username
Return: if yes return True, if not False
**************************************************************************************************************************************************"""
def check_user_exists(username):
    file = open(credentials_file_path,"r")  #"r" for read only
    for line in file:
        pair = line.split() #split string into list
        if(pair[0] == username):
            file.close()
            return True
    file.close()
    return False
"""**************************************************************************************************************************************************
Function description:   Function to authenicate user login
Arguments:  username
Return: if yes return True, if not False
**************************************************************************************************************************************************"""
def authenicate_user(username,passwd):
    if (not(check_user_exists(username))):
        return False
    file = open(credentials_file_path,"r")  #"r" for read only
    for line in file:
        pair = line.split() #split string into list
        if (pair[0] == username):
            passwd_hashed = pair[1]
            if (passwd_hashed == Hash_passwd(passwd)):
                file.close()
                return True
            else:
                file.close()
                return False
    file.close()
    return False
"""**************************************************************************************************************************************************
Function description:   Function to register user
Arguments:  NONE
Return: NONE
**************************************************************************************************************************************************"""
def register():
    username = input("Enter username: ")
    while(check_user_exists(username)):
        username = input("Username already exists\nEnter username: ")
    choice = input("\nif you want to have random generated password, choose 1\nif you want to enter your own password, choose 2\n")
    if(choice == "1"):
        password = Generate_random_passwd()
        password_hashed = Hash_passwd(password)
        save_user(username,password_hashed)
        print("User created successfully")
        print("Your password is:", password)
    elif(choice == "2"):
        password = getpass("enter password of length [8-16] characters\nPassword:")
        while((len(password) > 16) or (len(password) < 8)):
            password = getpass("Please enter password of length [8-16] characters\nPassword:")
        password_hashed = Hash_passwd(password)
        save_user(username,password_hashed)
        print("User created successfully")
    else:
        print("Not recognized")
"""**************************************************************************************************************************************************
Function description:   Function to login
Arguments:  NONE
Return: NONE
**************************************************************************************************************************************************"""
def login():
    username = input("Enter username: ")
    if (not(check_user_exists(username))):
        print("User does not exist")
        return
    password = getpass("Password: ")
    if(authenicate_user(username,password)):
        print("Login successful")
    else:
        print("Incorrect password")
"""**************************************************************************************************************************************************
Function description:   Function to login
Arguments:  NONE
Return: NONE
**************************************************************************************************************************************************"""       
def change_passwd():
    username = input("Enter username: ")
    if(not(check_user_exists(username))):
        print("User does not exist, try again")
        return
    file = open(credentials_file_path,"r")  #"r" open to read only
    file_iter = open(credentials_file_path,"r")  #"r" open to read only
    for line in file_iter:
        pair = line.split() #split string into list
        if(pair[0] == username):
            old_passwd = getpass("Old password: ")
            old_passwd_hashed = pair[1]
            if(old_passwd_hashed != Hash_passwd(old_passwd)):
                print("Old password is incorrect, try again")
                file.close()
                file_iter.close()
                return
            new_passwd = getpass("New password: ")
            new_passwd_again = getpass("Re-enter the new password: ")
            if(new_passwd != new_passwd_again):
                print("New password entered incorrectly, try again")
                file.close()
                file_iter.close()
                return
            new_passwd_hashed = Hash_passwd(new_passwd)
            file_data = file.read() #it reads empty why!!!
            file_data = file_data.replace(f"{old_passwd_hashed}",f"{new_passwd_hashed}")
            file.close()
            file_iter.close()
            file = open(credentials_file_path,"w") #"w" open to write, data is truncated and over-written
            file.write(file_data)
            file.close()
            print("Password changed sucessfully")
            return
"""**************************************************************************************************************************************************
Function description:   Main function to operate all functions
Arguments:  NONE
Return: NONE
**************************************************************************************************************************************************"""
def main():
    while True:
        print("1-login\n2-register\n3-change password\n4-exit")
        choice = input("Enter your choice: ")
        if(choice == "1"):
            login()
        elif(choice == "2"):
            register()
        elif(choice == "3"):
            change_passwd()
            #this code has a bug, if two users have the same password, changing one of them may affect the other user
        elif(choice == "4"):
            break
        else:
            print("Invalid Choice")

main()
