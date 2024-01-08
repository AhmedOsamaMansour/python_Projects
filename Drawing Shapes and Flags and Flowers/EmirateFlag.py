from turtle import *

title("Dubai Flag")
hideturtle()

penup()
goto(-250,0)
pendown()

# red rectangle 
color('red')
begin_fill()
lt(90)
fd(200)
rt(90)
fd(100)
rt(90)
fd(200)
rt(90)
fd(100)
end_fill()
#return point
rt(180)
fd(100)

# black rectangle
color('black')
begin_fill()
fd(320)
lt(90)
fd(67)
lt(90)
fd(320)
rt(90)
end_fill()

#white rectangle
color('white')
fd(66)

# green rectangle
color('green')
begin_fill()
fd(67)
rt(90)
fd(320)
rt(90)
fd(67)
rt(90)
fd(320)
end_fill()
penup()
goto(-250,0)
pendown()

# border of flag
color('black')
rt(90)
fd(200)
rt(90)
fd(420)
rt(90)
fd(200)
rt(90)
fd(420)



mainloop()