from turtle import *
speed(0)
bgcolor('black')
hideturtle()
def curve():
    for i in range(200):
        rt(1)
        fd(1)
def heart():
    fillcolor("red")
    begin_fill()
    lt(140)
    fd(113)
    curve()
    lt(120)
    curve()
    fd(112)
    end_fill()
heart()
mainloop()