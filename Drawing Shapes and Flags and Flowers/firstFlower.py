from turtle import *
penup()
goto(0,30)
pendown()

title("Flower")
bgcolor("black")
speed(0)
hideturtle()
Colors = ['yellow','red','yellow','red']
for i in range(120):
    for c in Colors:
        color(c)
        circle(200-i,100)
        lt(90)
        circle(200-i,100)
        rt(60)
        end_fill()
mainloop()