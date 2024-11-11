from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Rock Paper Scissors App")
root.geometry("500x400")
root.configure(bg="lawn green")

def top_win():
    root.update()
    global ropasclb, rpslbl, uscore, cscore, uscorel, cscorel
    uscore = 0
    cscore = 0
    top = Toplevel()
    top.title("Rock Paper Scissors App")
    top.geometry("450x350")
    top.configure(bg="gold")
    rock = Button(top, text="ROCK", command=crock, width=15, bg="saddle brown", fg="snow", font=("Courier New", 10, "bold"))
    rock.place(x=10, y=20)
    paper = Button(top, text="PAPER", command=cpaper, width=15, bg="saddle brown", fg="snow", font=("Courier New", 10, "bold"))
    paper.place(x=160, y=20)
    scissors = Button(top, text="SCISSORS", command=cscissors, width=15, bg="saddle brown", fg="snow", font=("Courier New", 10, "bold"))
    scissors.place(x=310, y=20)
    ropasclb = Label(top, width=15, bg="saddle brown", fg="snow")
    ropasclb.place(x=170, y=60)
    rpslbl = Label(top, bg="gold", font=("Times New Roman", 15))
    rpslbl.place(relx=0.35, rely=0.5)
    cscore_lbl = Label(top, text="Computer", bg="DarkOliveGreen1")
    cscore_lbl.place(x=40, y=250)
    uscore_lbl = Label(top, text="User", bg="DarkOliveGreen1")
    uscore_lbl.place(x=360, y=250)
    cscorel = Label(top, text=cscore, bg="DarkOliveGreen1")
    cscorel.place(x=40, y=270)
    uscorel = Label(top, text=uscore, bg="DarkOliveGreen1")
    uscorel.place(x=377, y=270)

def crock():
    global uscore, cscore
    rps = random.choice(['rock', 'paper', 'scissors'])
    ropasclb.config(text=rps.upper())
    if rps == 'rock':
        rpslbl.config(text="Its a tie game", fg="orange")
    elif rps == 'paper':
        rpslbl.config(text="You lost the game", fg="red")
        cscore = cscore + 1
        cscorel.config(text=cscore)
    elif rps == 'scissors':
        rpslbl.config(text="You won the game", fg="green2")
        uscore = uscore + 1
        uscorel.config(text=uscore)
    if uscore == 5:
        rpslbl.config(text="You won the match :)", fg="green2")
    elif cscore == 5:
        rpslbl.config(text="You lost the match :(", fg="red")

def cpaper():
    global uscore, cscore
    rps = random.choice(['rock', 'paper', 'scissors'])
    ropasclb.config(text=rps.upper())
    if rps == 'paper':
        rpslbl.config(text="Its a tie game", fg="orange")
    elif rps == 'scissors':
        rpslbl.config(text="You lost the game", fg="red")
        cscore = cscore + 1
        cscorel.config(text=cscore)
    elif rps == 'rock':
        rpslbl.config(text="You won the game", fg="green2")
        uscore = uscore + 1
        uscorel.config(text=uscore)
    if uscore == 5:
        rpslbl.config(text="You won the match :)", fg="green2")
    elif cscore == 5:
        rpslbl.config(text="You lost the match :(", fg="red")
    
def cscissors():
    global uscore, cscore
    rps = random.choice(['rock', 'paper', 'scissors'])
    ropasclb.config(text=rps.upper())
    if rps == 'scissors':
        rpslbl.config(text="Its a tie game", fg="orange")
    elif rps == 'rock':
        rpslbl.config(text="You lost the game", fg="red")
        cscore = cscore + 1
        cscorel.config(text=cscore)
    elif rps == 'paper':
        rpslbl.config(text="You won the game", fg="green2")
        uscore = uscore + 1
        uscorel.config(text=uscore)
    if uscore == 5:
        rpslbl.config(text="You won the match :)", fg="green2")
    elif cscore == 5:
        rpslbl.config(text="You lost the match :(", fg="red")
    
bg = Image.open("rps.jpeg")
bg_img = ImageTk.PhotoImage(bg)

i_l = Label(root, image=bg_img)
i_l.place(x=(500 // 2) - (bg.size[1] // 2), y=70)

root.update()
rps_lbl = Label(root, text="Rock Paper Scissors", font=("Corbel New", 12), bg="medium blue", fg="snow")
rps_lbl.place(x=((500 // 2) - (rps_lbl.winfo_width()) // 2) - 75, y=20)

lgsb = Button(root, text="Lets get Started!", command=top_win, font=("Algerian", 13), bg="medium blue", fg="snow")
lgsb.place(x=((500 // 2) - (rps_lbl.winfo_width()) // 2) - 80, y=350)

root.mainloop()