# JQ 2nd
import turtle as t
def triangleism(recursion,turt):
    
    def drawTriangle(points,turt):
        turt.up()
        turt.goto(points[0][0],points[0][1])
        turt.down()
        turt.goto(points[1][0],points[1][1])
        turt.goto(points[2][0],points[2][1])
        turt.goto(points[0][0],points[0][1])

    def getMid(p1,p2):
        return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

    def sirpin(points,degree,turt):

        drawTriangle(points,turt)
        if degree > 0:
            sirpin([points[0],
                            getMid(points[0], points[1]),
                            getMid(points[0], points[2])],
                    degree-1, turt)
            sirpin([points[1],
                            getMid(points[0], points[1]),
                            getMid(points[1], points[2])],
                    degree-1, turt)
            sirpin([points[2],
                            getMid(points[2], points[1]),
                            getMid(points[0], points[2])],
                    degree-1, turt)

    def main(recursion,turt):

        myWin = t.Screen()
        myPoints = [[-100,-50],[0,100],[100,-50]]
        sirpin(myPoints,recursion,turt)
        myWin.exitonclick()

    main(recursion,turt)

turt = t.Turtle()
# define triangleism with recursion, turt  
#     define drawTriangle with points, turt  
#         turt lift pen  
#         turt move to first point  
#         turt lower pen  
#         turt move to second point  
#         turt move to third point  
#         turt move back to first point  
#  
#     define getMid with p1, p2  
#         return midpoint between p1 and p2  
#  
#     define sirpin with points, degree, turt  
#         call drawTriangle with points, turt  
#         if degree greater than 0  
#             call sirpin with [points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree-1, turt  
#             call sirpin with [points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree-1, turt  
#             call sirpin with [points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree-1, turt  
#  
#     define main with recursion, turt  
#         myWin equal to screen  
#         myPoints equal to [[-100, -50], [0, 100], [100, -50]]  
#         call sirpin with myPoints, recursion, turt  
#         myWin wait for exit click  
#  
#     call main with recursion, turt  
#  
# turt equal to new Turtle  
