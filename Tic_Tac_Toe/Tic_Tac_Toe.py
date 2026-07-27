
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tic-Tac-Toe")

player = "X"
buttons = []

def Check_win():
       ways_to_win = [
          [0,1,2],
          [3,4,5],
          [6,7,8],
          [0,3,6],
          [1,4,7],
          [2,5,8],
          [0,4,8],
          [2,4,6]
    ]
       
for i in ways_to_win:
    a = i[0]
    b=  i[1]
    c = i[2]

    if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "" :
          


        