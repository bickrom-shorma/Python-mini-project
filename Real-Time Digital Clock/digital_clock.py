import tkinter as tk
from time import strftime

def update_time():
    crnt_time = strftime('%H:%M:%S')
    time_label.config(text=crnt_time)
    time_label.after(1000,update_time)

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.configure(bg="black")
root.resizable(False,False)

time_label = tk.Label(
    root,
    font=("Courier New", 50, "bold"),
    background = "black",
    foreground = "lime"
)

time_label.pack(anchor="center",expand=True)

update_time()
root.mainloop()