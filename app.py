from tkinter import *
from time import time, sleep
import random
from tkinter import messagebox

global lbl_answer
global lbl_show

root = Tk()
root.title("Magic 8ball | By: Aron")
root.iconbitmap("8ball.ico")
root.geometry("318x400")

def bruh():
    lbl_show.destroy()


def answer():
    global lbl_show
    list =[
    "It is certain",
    "Without a doubt",
    "You may rely on it",
    "Yes definitely",
    "It is decidedly so",
    "As I see it, yes",
    "Most likely",
    "Yes",
    "Outlook good",
    "Signs point to yes",
    "Reply hazy try again",
    "Better not tell you now",
    "Ask again later",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "Outlook not so good",
    "My sources say no",
    "Very doubtful",
    "My reply is no"
]
    sleep(1)
    lbl_show = Label(root, text="You said, " + e1.get() + "?" + " and your answer is...", font=("Arial", 11))
    lbl_show.grid(row=4, column=0)
    lbl_answer = Label(root, text="Answer: " + random.choice(list), font=("Arial", 14))
    lbl_answer.grid(row=5, column=0)
    response = messagebox.askquestion("Magic 8ball", "Would you like to play again?")
    
    if response == "yes":
        lbl_show.destroy()
        lbl_answer.destroy()


    else:
        print("WINDOW CLOSED")
        root.destroy()
    


lbl1 = Label(root, text="Type Your Question In Below", fg="white", bg="black", font=("Arial", 18))
lbl1.grid(row=1, column=0)

e1 = Entry(root, width=50, borderwidth=5)

e1.grid(row=2, column=0, columnspan=2)


btn = Button(root, text="SHAKE!", width=10, height=5, bg="blue", fg="white", command=answer)
btn.grid(row=3, column=0, padx=10, pady=10)


Label(root, text="Made by: Aron", font=("Arial", 16)).grid(row=9, column=0)

mainloop()