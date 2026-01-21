# JQ 2nd Personal library

per_lib = {
    
}
def display():
    print(per_lib)

def add(per_lib):
    book = input("what book do you want to add?\n")
    author = input(" What author wrote this book?\n")
    per_lib[book]= author
    return per_lib
def Delete(per_lib):
    what = input("what do you want to delete, please insert title?\n")
    del per_lib[what]
    return per_lib
def search():
    
running = True
while running == True:
    action = input("What do you want to do? 1 view\n 2 add\n 3 delete\n")
    if action == "1":
        display()
    elif action == "2":
        add(per_lib)
    elif action == "3":
        Delete(per_lib)
    elif action == "4":
        Delete(per_lib)
    elif action == "5":
        exit
    else:
        print("please try again")
