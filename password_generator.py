import random

chars_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!%ù$£&€^/*-(`)[]="
other_password = "yes"

while other_password == "yes":
    password_length = int(input("What length do you want for your password ? "))
    password_count = int(input("How many password do you want ? "))
    for i in range(1,password_count+1):
        password = ""
        for j in range(password_length):
            password_chars = random.choice(chars_list)
            password = password + password_chars
        print(f"Password {i} : {password}")
    other_password = input("Do you want to generate other password(s) ? (yes or no) : ")
