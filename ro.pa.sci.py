import random
import tkinter as tk
from tkinter import *
root = tk.Tk()

def rock_button():
    myLabel = Label(root, text="rock")
    myLabel.pack
   
def paper_button():
    return computer_pick

def scissors_button():
    return computer_pick
    
computer_pick = tk.Entry 


root.config
options = tk.Entry(root, state = "disabled", width=50, font = ("Arial", 30), text="Pick!")
options.pack()

tk.Button(root, text="Rock!", font = ("Arial", 20), width=8, command=rock_button).pack()
tk.Button(root, text="Paper!", font = ("Arial", 20), width=8, command=paper_button).pack()
tk.Button(root, text="Scissors!", font = ("Arial", 20), width=8, command=scissors_button).pack()


user_wins = 1
computer_wins = 1

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won! You have", user_wins, "points!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won! You have", user_wins, "points!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won! You have", user_wins, "points!")
        user_wins += 1
    
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Byebye!")


root.mainloop()