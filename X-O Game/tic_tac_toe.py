from tkinter import *
import random as rand
import winsound


# function put X or O in GUI window
def drawAndNextPlayer(row,col):
    global player
    # check Cell is empty and not win status
    if gameBtns[row][col]['text']=="" and checkWin()==False:
        # check player == O (first element in array)
        if player == playersChoice[0]:
            gameBtns[row][col]['text']= player
            if checkWin() == False:
                player = playersChoice[1]
                whosPlayLabel.config(text=(player + " Should Play"))
            elif checkWin() ==True:
                whosPlayLabel.config(text= ("congrats, " + playersChoice[0] + " wins!"))
            elif checkWin() == 'tie':
                whosPlayLabel.config(text= ("Tie, No Winner!"))

        # check player == X (second element in array)
        elif player == playersChoice[1]:
            gameBtns[row][col]['text']=player
            # check if this status is not win then convert player (O) and update label
            if checkWin() ==False:
                player = playersChoice[0]
                whosPlayLabel.config(text=(player + " Should Play"))
            # check win status to update label
            elif checkWin() ==True:
                whosPlayLabel.config(text=("congrats, " + playersChoice[1] + " wins!"))
            # check empty cell (equals no loser)
            elif checkWin() == 'tie':
                whosPlayLabel.config(text= ("Tie, No Winner!"))

# function check win of game
def checkWin():
    # check 3 horizontal line
    for row in range(3):
        if gameBtns[row][0]['text'] == gameBtns[row][1]['text'] == gameBtns[row][2]['text'] != "":
            gameBtns[row][0].config(bg="#A6F6FF")
            gameBtns[row][1].config(bg="#A6F6FF")
            gameBtns[row][2].config(bg="#A6F6FF")
            winsound.PlaySound("winSound.wav",winsound.SND_ASYNC)
            return True
    # check 3 vertical line
    for col in range(3):
        if gameBtns[0][col]['text'] == gameBtns[1][col]['text'] == gameBtns[2][col]['text'] != "":
            gameBtns[0][col].config(bg="#A6F6FF")
            gameBtns[1][col].config(bg="#A6F6FF")
            gameBtns[2][col].config(bg="#A6F6FF")
            winsound.PlaySound("winSound.wav",winsound.SND_ASYNC)
            return True
    # check diagonals :
    # \
    if gameBtns[0][0]['text'] == gameBtns[1][1]['text'] == gameBtns[2][2]['text'] != "":
        gameBtns[0][0].config(bg="#A6F6FF")
        gameBtns[1][1].config(bg="#A6F6FF")
        gameBtns[2][2].config(bg="#A6F6FF")
        winsound.PlaySound("winSound.wav",winsound.SND_ASYNC)
        return True
    # / 
    elif gameBtns[0][2]['text'] == gameBtns[1][1]['text'] == gameBtns[2][0]['text'] != "":
        gameBtns[0][2].config(bg="#A6F6FF")
        gameBtns[1][1].config(bg="#A6F6FF")
        gameBtns[2][0].config(bg="#A6F6FF")
        winsound.PlaySound("winSound.wav",winsound.SND_ASYNC)
        return True
    # check equality
    if checkEmptyCells() == False:
        for row in range(3):
            for col in range(3):
                gameBtns[row][col].config(bg='#C70039')
        winsound.PlaySound("toeStatus.wav",winsound.SND_ASYNC)
        return 'tie'
    
    else:
        return False
# function check empty cells (if not win game end and restart game)
def checkEmptyCells():
    emptyCells = 9
    for row in range(3):
        for col in range(3):
            if gameBtns[row][col]['text'] != "":
                emptyCells-=1
    if emptyCells == 0 :
        return False
    else:
        return True

# function start game
def startGame():
    global player
    player = rand.choice(playersChoice)
    whosPlayLabel.config(text= (player + " Should Play"))
    for row in range(3):
        for col in range(3):
            gameBtns[row][col].config(text="",bg='#F1B4BB')

window = Tk()
window.title("Tic-Tac-Toe Game".center(20))
window.configure(bg='#132043')
window.iconbitmap('./icon.ico')
# window.geometry("400x300")


playersChoice = ['O','X']
player = rand.choice(playersChoice)
gameBtns= [
    ['','',''],
    ['','',''],
    ['','','']
]
whosPlayLabel = Label(text=(player + " Should Play"),bg='#132043',foreground='#F1B4BB',font=("Courier",30,"normal"))
whosPlayLabel.pack(side=TOP,pady=15)
restartBtn = Button(text="restart",font=("consolas",24,"normal"),bg="#F1B4BB",foreground='#132043',command=startGame)
restartBtn.pack(side=BOTTOM,pady=10)

# Frame Of Buttons That has Values X Or O
btnsFrame = Frame(window)
btnsFrame.pack(side=BOTTOM,pady=15,padx=30)
for row in range(3):
    for col in range(3):
        gameBtns[row][col] = Button(btnsFrame, text="",bg='#F1B4BB', font=("consolas",24), width=5, height=2, 
                                    command = lambda row=row , col=col : drawAndNextPlayer(row,col))
        gameBtns[row][col].grid(row=row, column=col)

window.mainloop()