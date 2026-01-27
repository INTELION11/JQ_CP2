# JQ 2nd Password Generator
import random as r
def pass_gen():
    def pas_add(case,password,num1,num2):
        match case:
            case "y":
                password.append(r.randint(num1,num2))
                return password
            case "n":
                return
    leng = int(input("How long does the password need to be:\n"))
    lower = input("Does the password need lowercase letters (Y/N):\n").strip().lower()
    upper = input("Does the password need uppercase letters (Y/N):\n").strip().lower()
    num = input("Does the password need numbers letters (Y/N):").strip().lower()
    char = input("Does the password need special characters letters (Y/N):\n").strip().lower()
    password = []
    for i in range(1,4):
        for i in range(1,leng):
            pas_add(upper,password,97,122); exit if len(password) == leng else print()

            pas_add(lower,password,65,90); exit if len(password) == leng else print()

            pas_add(num,password,0,127); exit if len(password) == leng else print()

            pas_add(char,password,97,122); exit if len(password) == leng else print()

        new_password = []
        for i in password:
            new_password.append(chr(i))
        print(*new_password,sep="")

        #underscore if its under none of the above


world = True
while world == True:
    action = input("\n1. Generate Passwords \n2. Exit\n").strip().lower()
    match action:
        case "1":
            pass_gen()
        case "2":
            world = False
        case _:
            print("please try again")
    
