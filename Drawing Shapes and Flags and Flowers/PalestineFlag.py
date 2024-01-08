from turtle import *
title('Palestine Flag')
# to hide arrow
hideturtle()

# Set starting position at the middle of the window

#to remove draw lines(garbage) when go to position (penup-pendown)
penup()
goto(-250, 0)
pendown()
#######################################################################################################################
# triangle
color('red')
# to start drawing
begin_fill() #to fill closed shape with color
# left(angle) turtle (Turn the turtle left or right (in degrees).)
lt(90) #angle
# forward(distance) turtle
fd(200) #steps
# right(angle) turtle (Turn the turtle left or right (in degrees).)
rt(135)
fd(150)
rt(90)
fd(150)
# to end drawing
end_fill()
#######################################################################################################################
# turn arrow to draw black rectangle

#to remove draw lines(garbage) when go to position (penup-pendown)
penup()
rt(135)#angle
fd(212)#steps
pendown()
rt(90)
color('black')
begin_fill()
fd(300)
rt(90)
fd(70)
rt(90)
fd(229)
rt(45)
fd(100)
end_fill()
#######################################################################################################################
# white rectangle

#to remove draw lines(garbage) when go to position (penup-pendown)
penup()
lt(180)
fd(100)
pendown()
color('white')
lt(45)
fd(227)
rt(90)
fd(70)
#######################################################################################################################
# green rectangle
color('green')
begin_fill()
rt(90)
fd(225)
lt(45)
fd(100)
lt(135)
fd(300)
lt(90)
fd(72)
end_fill()
#########################################################################################################################
# word
color('red')
write("#Save_Palestine",font=('verdina',15,'bold'))

mainloop()