import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.label = tk.Label(master, text="Choose rock, paper, or scissors:")
        self.label.pack()

        choices = ['rock', 'paper', 'scissors']
        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set(choices[0])

        self.user_choice_menu = tk.OptionMenu(master, self.user_choice_var, *choices)
        self.user_choice_menu.pack()

        self.play_button = tk.Button(master, text="Play", command=self.play_game)
        self.play_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.score_label = tk.Label(master, text="")
        self.score_label.pack()

    def play_game(self):
        user_choice = self.user_choice_var.get()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        result = self.determine_winner(user_choice, computer_choice)
        self.display_result(user_choice, computer_choice, result)

        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1

        self.update_score_label()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            return "You win!"
        else:
            return "Computer wins!"

    def display_result(self, user_choice, computer_choice, result):
        self.result_label.config(text=f"You chose {user_choice.capitalize()}. Computer chose {computer_choice.capitalize()}.\n{result}")

    def update_score_label(self):
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
