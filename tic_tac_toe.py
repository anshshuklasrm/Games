import tkinter as tk
from tkinter import messagebox
import random

# Global variables
PLAYER = "X"
COMPUTER = "O"
board = [["" for _ in range(3)] for _ in range(3)]

def on_button_click(row, col):
    global board

    if board[row][col] == "":
        board[row][col] = PLAYER
        button = buttons[row][col]
        button.config(text=PLAYER, state=tk.DISABLED)

        if check_winner(PLAYER):
            messagebox.showinfo("Game Over", "You win!")
            reset_game()
        elif is_board_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            computer_move()

def computer_move():
    available_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                available_moves.append((row, col))

    if available_moves:
        row, col = random.choice(available_moves)
        board[row][col] = COMPUTER
        button = buttons[row][col]
        button.config(text=COMPUTER, state=tk.DISABLED)

        if check_winner(COMPUTER):
            messagebox.showinfo("Game Over", "Computer wins!")
            reset_game()
        elif is_board_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()

def check_winner(player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_board_full():
    for row in board:
        if "" in row:
            return False
    return True

def reset_game():
    global board

    board = [["" for _ in range(3)] for _ in range(3)]

    for row in range(3):
        for col in range(3):
            button = buttons[row][col]
            button.config(text="", state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Create the welcome label
welcome_label = tk.Label(window, text="Welcome to the Tic Tac Toe Game\nDesigned by Ansh", font=("Helvetica", 16))
welcome_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Create the buttons
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text="", width=10, height=5,
                           command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row+1, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)

# Run the main loop
window.mainloop()
