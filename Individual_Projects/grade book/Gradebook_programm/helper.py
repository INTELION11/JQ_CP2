# helpers.py  
  
def get_int(prompt):  
    while True:  
        try:  
            value = int(input(prompt))  
            return value  
        except:  
            print("Whoops, that's not a number. Try again.")  
  
#definition get_int(prompt)  
# ask user for a number until they type a real int  
# return the number when it's good  
  
def get_grade(prompt):  
    while True:  
        try:  
            value = float(input(prompt))  
            if 0 <= value <= 100:  
                return value  
            else:  
                print("Grade needs to be between 0 and 100. Try again.")  
        except:  
            print("Come on, enter a number for the grade.")  
  
#definition get_grade(prompt)  
# ask user for a number between 0 and 100 (can be decimal)  
# if not a number or not in range, keep asking  
# return the grade when it's good  
