"""import turtle as t
option = 3
t.speed(.5)
t.penup()
t.goto(-300,-300)
t.pendown()
distance = 1400
true_distance = 700
for i in  range(0,option):
    distance = distance/2
    t.forward(distance)
    t.left(120)
    t.forward(distance)
    t.left(120)
    t.forward(distance)
    t.left(120)
    distance = distance/2
    t.forward(distance)
    t.left(60)
    t.forward(distance)
    t.left(120)
    t.forward(distance)
    t.left(120)
    t.forward(distance)
    t.left(60)
distance2 = distance
t.forward(distance)
distance = distance*2
distance = distance*2
distance = distance/2
t.forward(distance)
t.left(120)
t.forward(distance)
t.left(120)
t.forward(distance)
t.left(120)
distance = distance/2
t.forward(distance)
t.left(60)
t.forward(distance)
t.left(120)
t.forward(distance)
t.left(120)
t.forward(distance)
t.left(60)
distance2 = distance

t.forward(distance)
distance = distance*16
distance = distance/2
t.forward(distance)
t.left(120)
t.forward(distance)
t.left(120)
t.forward(distance)
t.left(120)
distance = distance/2
t.forward(distance)
t.left(60)
t.forward(distance)
t.left(120)
t.forward(distance)
t.left(120)
t.forward(distance)
t.left(60)
distance2 = distance"""
"""
import turtle

def drawTriangle(points,myTurtle):
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):

    drawTriangle(points,myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()

main()"""

import turtle as t

def draw(point):
    