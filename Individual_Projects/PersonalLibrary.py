# JQ 2nd Personal library  
  
# make per_lib dictionary to store books and authors  
per_lib = {}  
  
# show all items in the library  
def display():  
    # if per_lib empty, say so  
    if not per_lib:  
        print("Library is empty.")  
    else:  
        # for each book, print book and author  
        for i, (book, author) in enumerate(per_lib.items(), 1):  
            print(f"{i}. {book} by {author}")  
  
# add new book to per_lib  
def add(per_lib):  
    # ask for book title  
    book = input("What book do you want to add?\n")  
    # ask for author name  
    author = input("What author wrote this book?\n")  
    # add to per_lib  
    per_lib[book] = author  
    print(f"You have added\n{book} by {author}")  
    return per_lib  
  
# remove book from per_lib by title  
def Delete(per_lib):  
    # if no books, print message  
    if not per_lib:  
        print("Library is empty. Nothing to delete.")  
        return per_lib  
    # show all books with numbers  
    for i, (book, author) in enumerate(per_lib.items(), 1):  
        print(f"{i}. {book} by {author}")  
    # ask which to delete  
    num = input("Enter the number of the item you would like to remove: ")  
    try:  
        num = int(num)  
        # get key by index  
        key = list(per_lib.keys())[num - 1]  
        print(f"You have removed {key} by {per_lib[key]}")  
        del per_lib[key]  
    except (IndexError, ValueError):  
        print("Invalid selection.")  
    return per_lib  
  
# search for book by title or author  
def search():  
    # ask search type  
    kind = input("What would you like to search by?\n1. Title\n2. Author\n")  
    if kind == "1":  
        # ask for title  
        title = input("What is the title? ").lower()  
        found = False  
        for book, author in per_lib.items():  
            if title in book.lower():  
                print(f"{book} by {author}")  
                found = True  
        if not found:  
            print("No matching books found.")  
    elif kind == "2":  
        # ask for author  
        author_search = input("What is the author's name? ").lower()  
        found = False  
        for book, author in per_lib.items():  
            if author_search in author.lower():  
                print(f"{book} by {author}")  
                found = True  
        if not found:  
            print("No matching books found.")  
    else:  
        print("Invalid choice.")  
  
# main menu loop  
running = True  
while running:  
    # print main menu  
    print("\nType the number for the action you would like to do \n1. View \n2. Add \n3. Remove \n4. Search \n 5. Exit")  
    action = input("")  
    # view library  
    if action == "1":  
        display()  
    # add book  
    elif action == "2":  
        add(per_lib)  
    # remove book  
    elif action == "3":  
        Delete(per_lib)  
    # search  
    elif action == "4":  
        search()  
    # exit program  
    elif action == "5":  
        print("Goodbye!")  
        running = False  
    # wrong input  
    else:  
        print("Please try again")  

