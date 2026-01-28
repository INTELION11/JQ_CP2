# JQ 2nd Password Generator    
import random as r    
    
def pass_gen():    
    # inner function: adds char to password if case is 'y'  
    def pas_add(case, password, num1, num2):    
        if case == "y":    
            password.append(r.randint(num1, num2))    
    
    # ask for password length    
    leng = int(input("How long does the password need to be:\n"))    
    # ask if need lowercase    
    lower = input("Does the password need lowercase letters (Y/N):\n").strip().lower()    
    # ask if need uppercase    
    upper = input("Does the password need uppercase letters (Y/N):\n").strip().lower()    
    # ask if need numbers    
    num = input("Does the password need numbers (Y/N):\n").strip().lower()    
    # ask if need special chars    
    char = input("Does the password need special characters (Y/N):\n").strip().lower()    
    # make 3 passwords    
    for i in range(1,4):  
        password = []    
        # build password until right length    
        while len(password) <= leng:    
            # add lowercase if picked    
            pas_add(lower, password, 97, 122)      
            if len(password) == leng: break    
            # add uppercase if picked    
            pas_add(upper, password, 65, 90)        
            if len(password) == leng: break    
            # add number if picked    
            pas_add(num, password, 48, 57)         
            if len(password) == leng: break    
            # add special char if picked    
            if char == "y":    
                spec = list('!@#\\$%^&*()_+-=[]{}|;:,.&lt;&gt;?/~`')    
                password.append(ord(r.choice(spec)))    
            if len(password) == leng: break    
        # turn password list to string and print    
        print("".join([chr(i) for i in password]))    
      
# main loop    
world = True    
while world:    
    # ask user to generate or exit    
    action = input("\n1. Generate Passwords \n2. Exit\n").strip().lower()    
    match action:    
        case "1":    
            pass_gen()    
        case "2":    
            world = False    
        case _:    
            print("please try again")    
