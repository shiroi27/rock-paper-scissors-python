import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]
score = {"Wins": 0, "Losses": 0, "Ties": 0}

# Main Logic
def play(user_choice):
    comp_choice = random.choice(choices)
    if user_choice == comp_choice:
        result = "It's a Tie!"
        score["Ties"] += 1
    elif (
        (user_choice == "Rock" and comp_choice == "Scissors") or
        (user_choice == "Paper" and comp_choice == "Rock") or
        (user_choice == "Scissors" and comp_choice == "Paper")
    ):
        result = "You Win!"
        score["Wins"] += 1
    else:
        result = "You Lose!"
        score["Losses"] += 1
    
    result_var.set(f"You chose: {user_choice}\nComputer chose: {comp_choice}\n{result}\n"
                   f"Wins: {score['Wins']} | Losses: {score['Losses']} | Ties: {score['Ties']}")

# Window Setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("800x500+400+200")
root.resizable(False, False)
root.config(bg="#E0F7FA")

# Header
header = tk.Frame(root, bg="#00BCD4", height=70)
header.pack(fill=tk.X)
title = tk.Label(header, text="~ ROCK PAPER SCISSORS ~", font=("Times New Roman", 24, "bold"), bg="#00BCD4", fg="#000000")
title.pack(pady=15)

# Decorative Line
decorative_line = tk.Frame(root, bg="#00838F", height=5)
decorative_line.pack(fill=tk.X)

# Result Label
result_var = tk.StringVar()
result_var.set("Choose your move!")
result_label = tk.Label(root, textvariable=result_var, font=("Times New Roman", 16, "bold"), bg="#E0F7FA", fg="#000000")
result_label.pack(pady=30)

# Button Frame
btn_frame = tk.Frame(root, bg="#E0F7FA")
btn_frame.pack(pady=10)

rock_btn = tk.Button(btn_frame, text="ROCK", width=12, height=2, font=("Times New Roman", 14, "bold"), bg="#B2EBF2", fg="#000000", command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text="PAPER", width=12, height=2, font=("Times New Roman", 14, "bold"), bg="#B2EBF2", fg="#000000", command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(btn_frame, text="SCISSORS", width=12, height=2, font=("Times New Roman", 14, "bold"), bg="#B2EBF2", fg="#000000", command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

def reset_game():
    score["Wins"] = 0
    score["Losses"] = 0
    score["Ties"] = 0
    result_var.set("Choose your move!")

reset_btn = tk.Button(root, text="RESET", font=("Times New Roman", 12, "bold"), bg="#FFCDD2", fg="#000000", command=reset_game)
reset_btn.pack(pady=10)

# Footer
footer = tk.Label(root, text="Let the best player win!", font=("Arial", 10), bg="#E0F7FA", fg="#555")
footer.pack(side=tk.BOTTOM, pady=10)

root.mainloop()