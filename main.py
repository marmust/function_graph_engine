#--- function graph engine ---
#type your function between the two comments "this is the function"
#change the resolution between the two cmments "graph res" (the higher the value the worse the resolution)
#examples:
#y = x + 100
#y = x * x * 0.01
import turtle
import math
turtle.bgcolor("black")
x = -500
y = 0
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-1000, 0)
turtle.pendown()
turtle.pencolor("gray")
turtle.goto(1000, 0)
turtle.penup()
turtle.goto(0, -1000)
turtle.pendown()
turtle.goto(0, 1000)
turtle.penup()
while True:
    turtle.pencolor("white")
    turtle.speed(0)
    #--- graph res ---
    x = x+10
    #--- graph res ---
    #--- this is the function ---
    y = x*x*x*0.00001
    #--- this is the function ---
    turtle.goto(x, y)
    turtle.pendown()
    if x>499:
        break
turtle.mainloop()