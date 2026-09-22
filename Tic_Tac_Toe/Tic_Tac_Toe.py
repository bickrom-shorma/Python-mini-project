import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("400x450")

player = "X"

buttons = []


def click(button):
    global player

    if button["text"] == "":
        button["text"] = player

        if check_winner():
            result.config(text=f"Player {player} Wins!")
            disable_buttons()
            return

        if all(button["text"] != "" for button in buttons):
            result.config(text="Draw!")
            return

        if player == "X":
            player = "O"
        else:
            player = "X"

        result.config(text=f"Player {player}'s Turn")


def check_winner():
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if (buttons[a]["text"] != "" and
            buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"]):
            return True

    return False


def disable_buttons():
    for button in buttons:
        button.config(state="disabled")


def restart():
    global player

    player = "X"

    for button in buttons:
        button.config(text="", state="normal")

    result.config(text="Player X's Turn")


result = tk.Label(
    window,
    text="Player X's Turn",
    font=("Arial", 18)
)

result.pack(pady=20)


frame = tk.Frame(window)
frame.pack()


for i in range(9):
    button = tk.Button(
        frame,
        text="",
        font=("Arial", 30),
        width=5,
        height=2,
        command=lambda i=i: click(buttons[i])
    )

    button.grid(
        row=i // 3,
        column=i % 3
    )

    buttons.append(button)


restart_button = tk.Button(
    window,
    text="Restart",
    font=("Arial", 15),
    command=restart
)

restart_button.pack(pady=20)


window.mainloop()