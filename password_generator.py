import random

chars_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?%$&€/*-()[]="

def generate_password(length, chars):
    password = ""
    for i in range(length):
        password_char = random.choice(chars)
        password+=password_char
    return password

password_count = int(input("Number of password : "))
password_length = int(input("Length of password : "))
password_list = ""

for j in range(password_count):
    password = generate_password(password_length, chars_list)
    print(f"password {j+1} : {password}")
    password_list += password + "\n"

save_password = input("Do you want to save the passwords ? Y/N : ")

if save_password.lower() == "y":
    with open("password_log.txt", "a") as psw:
        psw.write("---New round---\n")
        psw.write(password_list)
    print("passwords has been succesfully saved !")
