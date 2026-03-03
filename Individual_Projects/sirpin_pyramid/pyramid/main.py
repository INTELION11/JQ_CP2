import turtle as t
from settings import setting
from drawing import triangleism
def main():  
    while True:  
        turt = t.Turtle()  
        recursions = setting(turt)  
        triangleism(recursions, turt)
        again = input("to draw again insert (y) ").strip().lower()  
        if again != "y":  
            break  
        t.clearscreen()
# define main  
#     while true  
#         turt equals Turtle  
#         recursions equals setting(turt)  
#         call triangleism with recursions, turt  
#         again equal to user input ("to draw again insert (y)")  
#         if again not equal to "y"  
#             break loop  
#         clear screen  