import turtle  
  
def setting(turt):  
    while True:  
        try:  
            color = input("What color do you want your turtle? ")  
            turt.color(color)  
            break  
        except:  
            print("Invalid color, try again.")  
  
    while True:  
        try:  
            size = int(input("What size do you want your turtle? (integer, e.g. 1-10): "))  
            turt.pensize(size)  
            break  
        except:  
            print("Invalid size, try again.")  
  
    while True:  
        try:  
            recursion = int(input("How many recursions? (integer, e.g. 1-6): "))  
            break  
        except:  
            print("Invalid number, try again.")  
  
    return recursion  
# define setting with turt  
#     while true  
#         try  
#             color equals user input ("What color do you want your turtle?")  
#             set turt color to color  
#             break loop  
#         except  
#             display "Invalid color, try again."  
#  
#     while true  
#         try  
#             size equal to user input as integer (What size do you want your turtle?)  
#             set turt pensize to size  
#             break loop  
#         except  
#             display "Invalid size, try again."  
#  
#     while true  
#         try  
#             recursion equal to user input as integer (How many recursions?)  
#             break loop  
#         except  
#             display "Invalid number, try again."  
#  
#     return recursion  
