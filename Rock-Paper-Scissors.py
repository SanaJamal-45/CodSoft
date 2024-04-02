from tkinter import *
from PIL import Image,ImageTk
from random import randint
#main window
root=Tk()
root.title("Rock Paper Scissors")
root.geometry("900x400+100+100")
root.config(bg="#1AA7EC")
#pictures
rock_user_img=ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_user_img=ImageTk.PhotoImage(Image.open("paper-user.png"))
scissors_user_img=ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_comp_img=ImageTk.PhotoImage(Image.open("rock-comp.png"))
paper_comp_img=ImageTk.PhotoImage(Image.open("paper-comp.png"))
scissors_comp_img=ImageTk.PhotoImage(Image.open("scissors-comp.png"))
user_label=Label(root,image=rock_user_img,bg="#1AA7EC")
comp_label=Label(root,image=rock_comp_img,bg="#1AA7EC")
comp_label.grid(row=3,column=0)
user_label.grid(row=3,column=4)
#displaying scores
playerScore = Label(root, text=0, font=50, bg="#F5347F", fg="white",bd=2,relief=SOLID)
computerScore = Label(root, text=0, font=50, bg="#F5347F", fg="white",bd=2,relief=SOLID)
computerScore.grid(row=3, column=1)
playerScore.grid(row=3, column=3)
#displaying headings
user_indicator = Label(root, font= "Arial 15 underline", text="USER", bg="#F5347F", fg="white")
comp_indicator = Label(root, font="Arial 15 underline", text="COMPUTER",
                       bg="#F5347F", fg="white")
user_indicator.grid(row=1, column=4)
comp_indicator.grid(row=1, column=0)
#displaying message
msg = Label(root, font=200, bg="#F5347F", fg="white",text="Let's Play!!!",bd=2,relief=SOLID)
msg.grid(row=3, column=2)
#update message
def updateMessage(x):
    msg['text'] = x
#update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)
#update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)
#checking the winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("GAME DRAW !!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("YOU LOOSE:(")
            updateCompScore()
        else:
            updateMessage("YOU WIN:)")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("YOU LOOSE:(")
            updateCompScore()
        else:
            updateMessage("YOU LOOSE:(")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("YOU LOOSE:(")
            updateCompScore()
        else:
            updateMessage("YOU WIN:)")
            updateUserScore()

    else:
        pass
#choices
choices = ["rock", "paper", "scissor"]
def updateChoice(x):

    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_comp_img)
    elif compChoice == "paper":
        comp_label.configure(image=paper_comp_img)
    else:
        comp_label.configure(image=scissors_comp_img)
    #for user
    if x == "rock":
        user_label.configure(image=rock_user_img)
    elif x == "paper":
        user_label.configure(image=paper_user_img)
    else:
        user_label.configure(image=scissors_user_img)

    checkWin(x, compChoice)
#buttons
rock = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=7, column=1)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=7, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")).grid(row=7, column=3)
root.mainloop()