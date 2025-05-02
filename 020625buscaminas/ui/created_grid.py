import tkinter as tk
from tkinter import messagebox
import random

# Grid size and number of mines
GRID_SIZE = 8
MINES_COUNT = 7

# Game state variables
buttons = []
mines = []
revealed = []
flags = []

# Create the grid
def create_grid():
    global buttons
    for row in range(GRID_SIZE):
        row_buttons = []
        for col in range(GRID_SIZE):
            btn = tk.Button(root, text="", width=4, height=2, command=lambda r=row, c=col: reveal_cell(r, c))
            btn.bind("<Button-3>", lambda event, r=row, c=col: flag_cell(r, c))
            btn.grid(row=row, column=col)
            row_buttons.append(btn)
        buttons.append(row_buttons)

# Place mines
def place_mines():
    global mines
    mines = random.sample([(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE)], MINES_COUNT)

# Count neighboring mines
def count_neighboring_mines(row, col):
    count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if (r, c) in mines and 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
                count += 1
    return count

# Reveal a cell
def reveal_cell(row, col):
    if (row, col) in revealed or (row, col) in flags:
        return

    revealed.append((row, col))
    if (row, col) in mines:
        buttons[row][col].config(text="M", bg="red")
        game_over(False)
        return

    count = count_neighboring_mines(row, col)
    buttons[row][col].config(text=str(count) if count > 0 else "", state="disabled", relief="sunken")

    if count == 0:
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
                    reveal_cell(r, c)

    if len(revealed) == GRID_SIZE * GRID_SIZE - MINES_COUNT:
        game_over(True)

# Flag a cell
def flag_cell(row, col):
    if (row, col) in revealed:
        return

    if (row, col) in flags:
        flags.remove((row, col))
        buttons[row][col].config(text="")
    else:
        flags.append((row, col))
        buttons[row][col].config(text="F", fg="blue")

# Handle game over
def game_over(win):
    for r, c in mines:
        buttons[r][c].config(text="M", bg="red")
    if win:
        messagebox.showinfo("Minesweeper", "Congratulations! You win!")
    else:
        messagebox.showinfo("Minesweeper", "Game Over! You hit a mine.")
    root.destroy()

# Initialize the game
root = tk.Tk()
root.title("Minesweeper")
root.geometry("600x600")

def start_game():
    create_grid()
    place_mines()

start_game()
root.mainloop()