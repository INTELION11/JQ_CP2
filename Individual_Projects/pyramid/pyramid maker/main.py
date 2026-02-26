import turtle as t
option = int(input("how mny times?"))
t.penup()
t.goto(-300,-300)
t.pendown()
for i in range(0,option):
    distance = 600
    t.forward(distance)
    t.left(120)
    t.forward(distance)
    t.left(120)
    t.forward(distance)
    t.left(120)
    distance = distance/2




t.done()