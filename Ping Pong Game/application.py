#turtle used as gui for shapes moving and gameing
import turtle
from tkinter import messagebox
import winsound

window = turtle.Screen()
window.title('Ping Pong Game')
window.bgcolor(.1,.1,.1)
# set size of window
window.setup(width=800,height=600)
#speed of update window automatically (speed of game)
window.tracer(0)

############################################################################################################################################
# first player
player1 = turtle.Turtle()
#speed of drawing shape on the screen when moveing
player1.speed(1)
player1.shape('square')
#set size of player default 20px -> newWidth= 20*7 = 140px
player1.shapesize(stretch_wid=7,stretch_len=1)
player1.color('blue')
# not drawing any lines when moveing (اثر مكانه)
player1.penup()
# location of player on window
player1.goto(-370,0)

############################################################################################################################################
# second player
player2 = turtle.Turtle()
player2.speed(0)
player2.shape('square')
player2.shapesize(stretch_wid=7,stretch_len=1)
player2.color('red')
player2.penup()
player2.goto(365,0)
############################################################################################################################################
# ball (20px - 20px)
ball = turtle.Turtle()
ball.speed(0)
ball.color('white')
ball.shape('circle')
ball.penup()
ball.goto(0,0)
# d-> delta (rate of change) (speed of moveing ball)
ball.dx= 0.35
ball.dy= 0.35
############################################################################################################################################
centerLine = turtle.Turtle()
centerLine.speed(0)
centerLine.shape("square")
centerLine.color("white")
centerLine.shapesize(stretch_wid=27,stretch_len=0.1)
centerLine.penup()
centerLine.goto(0,0)
############################################################################################################################################
# score 
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed()
score.color("white")
score.penup()
# To hide shape of score and show text only
score.hideturtle()
# To set position of Text
score.goto(0,270)
score.write("Player 1: {}            Player 2: {}".format(score1,score2),align="center",font=("Courier",24,"normal"))
############################################################################################################################################

#functions
def player1_MoveingUp():
    # get y cordinate for player1
    y = player1.ycor()
    y+=20
    # set y cordinate for player1
    player1.sety(y)

def player1_MoveingDown():
    y = player1.ycor()
    y-=20
    player1.sety(y)

def player2_MoveingUp():
    y = player2.ycor()
    y+=20
    player2.sety(y)

def player2_MoveingDown():
    y = player2.ycor()
    y-=20
    player2.sety(y)

#keyboard binding:
# tell window to wait keyboard pressing
window.listen()
# when press w call function move up to player1
window.onkeypress(player1_MoveingUp,"w")
window.onkeypress(player1_MoveingDown,"s")
window.onkeypress(player2_MoveingUp,"Up")  # Arrow Up
window.onkeypress(player2_MoveingDown,"Down") # Arrow Down

# Game loop for game to
while True:
    # screen update 
    window.update()

    # moveing ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # check border (up and down)

    # border top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # reverse direction of y
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    # border bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # reverse direction of y
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    # border right
    if ball.xcor() > 390:
        ball.goto(0,0) # return ball in center 
        ball.dx *=-1 # reverse direction of x
        score1+=1
        # remove old text and write new text (avoid write old score on new score)
        score.clear()
        score.write("Player 1: {}            Player 2: {}".format(score1,score2),align="center",font=("Courier",24,"normal"))

    # border left
    if ball.xcor() < -390:
        ball.goto(0,0)  # return ball in center 
        ball.dx *=-1  # reverse direction of x
        score2+=1
        # remove old text and write new text (avoid write old score on new score)
        score.clear()
        score.write("Player 1: {}            Player 2: {}".format(score1,score2),align="center",font=("Courier",24,"normal"))

    # collision of ball with player 1
    if ball.xcor() > 348 and ball.xcor() < 365 and ball.ycor() < player2.ycor() + 70 and ball.ycor() > player2.ycor() - 70:
        ball.setx(348)
        ball.dx *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.xcor() < -358 and ball.xcor() > -370 and ball.ycor() < player1.ycor() + 70 and ball.ycor() > player1.ycor() - 70:
        ball.setx(-358)
        ball.dx *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if score1 >= 7:
        messagebox.showinfo("Game Over", "Player 1 wins!")
        window.bye()
    elif score2 >= 7:
        messagebox.showinfo("Game Over", "Player 2 wins!")
        window.bye()