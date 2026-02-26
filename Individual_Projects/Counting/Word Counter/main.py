from view import view_document
from update_doc import update_document
from adding import add_content

def main():  
    filename = input("Enter the exact file path for your document: ")  
    while True:  
        choice = input("1. Update document info\n 2. View document\n 3. Add content to document\n 4. Exit\n")  
        if choice == "1":  
            update_document(filename)  
        elif choice == "2":  
            view_document(filename)  
        elif choice == "3":  
            add_content(filename)  
        elif choice == "4":  
            break  
        else:  
            print("Invalid choice. Try again.")  
  

main()  
#define  main()
# prompt user for filename
# loop forever
# show the menu and get choice
# if choice is "1"
# update document
# if choice is "2"
# view document
# if choice is "3"
# add content
# if choice is "4"
# exit 
# else
# display invalid choice 