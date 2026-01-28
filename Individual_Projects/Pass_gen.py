# JQ 2nd Password Generator  
import random as r  
  
def pass_gen():  
    def pas_add(case, password, num1, num2):  
        if case == "y":  
            password.append(r.randint(num1, num2))  
  
    leng = int(input("How long does the password need to be:\n"))  
    lower = input("Does the password need lowercase letters (Y/N):\n").strip().lower()  
    upper = input("Does the password need uppercase letters (Y/N):\n").strip().lower()  
    num = input("Does the password need numbers (Y/N):\n").strip().lower()  
    char = input("Does the password need special characters (Y/N):\n").strip().lower()  
    for i in range(1,4):
        password = []  
        while len(password) <= leng:  
            pas_add(lower, password, 97, 122)    
            if len(password) == leng: break  
            pas_add(upper, password, 65, 90)      
            if len(password) == leng: break  
            pas_add(num, password, 48, 57)       
            if len(password) == leng: break  
            if char == "y":  
                spec = list('!@#\$%^&*()_+-=[]{}|;:,.&lt;&gt;?/~`')  
                password.append(ord(r.choice(spec)))  
            if len(password) == leng: break  
    
        print("".join([chr(i) for i in password]))  
    
world = True  
while world:  
    action = input("\n1. Generate Passwords \n2. Exit\n").strip().lower()  
    match action:  
        case "1":  
            pass_gen()  
        case "2":  
            world = False  
        case _:  
            print("please try again")  
