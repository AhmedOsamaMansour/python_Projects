from turtle import *
title('France Flag')
hideturtle()
penup()
goto(-250,0)
pendown()

# rectangle blue
begin_fill()
color('#0F1042')
lt(90)
fd(240)
lt(90)
fd(100)
lt(90)
fd(240)
lt(90)
fd(100)
end_fill()

# rectangle white
color("white")
fd(100)
#rectangle red
begin_fill()
color('red')
fd(100)
lt(90)
fd(240)
lt(90)
fd(100)
lt(90)
fd(240)
end_fill()

mainloop()