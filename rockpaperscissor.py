from tkinter import *
import random
root=Tk()
root.title("Rock Paper Scissor Game")
player_choice=""

p_score=0
c_score=0
def computer_choice():
    randomm=random.randint(0, 2)
    computer_choice=" "
    if randomm==0:
        computer_choice="Rock"
        c.delete(0, END)
        c.insert(0, "Rock")
    elif randomm==1:
        computer_choice="Paper"
        c.delete(0, END)
        c.insert(0, "Paper")
    else:
        computer_choice="Scissor"
        c.delete(0, END)
        c.insert(0, "Scissor")
    if player_choice==computer_choice:
        draw()
    elif player_choice=="Rock" and computer_choice=="Scissor":
        player_wins()
    elif player_choice=="Rock" and computer_choice=="Paper":
        computer_wins()
    elif player_choice=="Scissor" and computer_choice=="Rock":
        computer_wins()
    elif player_choice=="Scissor" and computer_choice=="Paper":
        player_wins()
    elif player_choice=="Paper" and computer_choice=="Rock":
        player_wins()
    elif player_choice=="Paper" and computer_choice=="Scissor":
        computer_wins()


def rock():
    p.delete(0, END)
    global player_choice
    player_choice= "Rock"
    p.insert(0, "Rock")
    computer_choice()


def paper():
    p.delete(0, END)
    global player_choice
    player_choice = "Paper"
    p.insert(0, "Paper")
    computer_choice()
def scissor():
    p.delete(0, END)
    global player_choice
    player_choice = "Scissor"
    p.insert(0, "Scissor")
    computer_choice()


label=Label(root, text="")
def rematch():
    c.delete(0, END)
    p.delete(0,END)
    global label
    label.destroy()
    global computer_entry, player_entry
    player_entry.delete(0,END)
    computer_entry.delete(0,END)
    player_entry.insert(0, 0)
    computer_entry.insert(0, 0)
def draw():
    global label
    label.destroy()
    label= Label(root, text="It is a draw!", font=("Times New Roman", 20, "bold"))
    label.grid(row=11, column=1)

def player_wins():
    global label
    label.destroy()
    label = Label(root, text="Player WINS!", font=("Times New Roman", 20, "bold"))
    label.grid(row=11, column=1)
    p_num= int(player_entry.get())
    player_entry.delete(0,END)
    global p_score
    p_score=1+p_num
    player_entry.insert(0, int(p_score))
def computer_wins():
    global label
    label.destroy()
    label = Label(root, text="Computer WINS!", font=("Times New Roman", 20, "bold"))
    label.grid(row=11, column=1)
    c_num= int(computer_entry.get())
    computer_entry.delete(0,END)
    global c_score
    c_score = 1+ c_num
    computer_entry.insert(0, int(c_score))
Label_spacing= Label(text=" ")

Label_player= Label(text="Player                          vs                         Computer")
Label_player.grid(row=0, column=0, columnspan=3)
Label_spacing.grid(row=1, column=0)
Label_spacing.grid(row=2, column=0)
p= Entry(root, width=25, borderwidth=5)
p.grid(row=3, column=0, columnspan=1)
c= Entry(root, width=25, borderwidth=5)
c.grid(row=3, column=2, columnspan=1)

Label_spacing.grid(row=4, column=0)
Label_spacing.grid(row=5, column=0)

button_rock=Button(root, text="Rock", padx=40, pady=20, borderwidth=5, command=rock)
button_paper=Button(root, text="Paper", padx=40, pady=20, borderwidth=5, command=paper)
button_scissor=Button(root, text="Scissor", padx=40, pady=20, borderwidth=5, command=scissor)
button_rematch=Button(root, text="Reset Game", padx=40, pady=40, borderwidth=10, command=rematch)
button_rock.grid(row=6, column=0)
button_paper.grid(row=6, column=1)
button_scissor.grid(row=6, column=2)
Label_spacing.grid(row=7)
Label_spacing.grid(row=8)
Label_spacing.grid(row=9)
button_rematch.grid(row=10, column=1)

score_player=Label(root, text="Player's Score: ")
score_computer= Label(root, text="Computer's Score: ")
Label_spacing.grid(row=12)
Label_spacing.grid(row=13)
Label_spacing.grid(row=14)
score_player.grid(row=15, column=0)
score_computer.grid(row=15, column=2)
player_entry= Entry(root, width=10, borderwidth=5)
computer_entry= Entry(root, width=10, borderwidth=5)
player_entry.grid(row=16, column=0)
computer_entry.grid(row=16, column=2)
player_entry.insert(0,0)
computer_entry.insert(0,0)







root.mainloop()