import tkinter as tk
from tkinter import messagebox

from utils.generator import generate_password
from utils.strength_checker import check_strength
from utils.clipboard import copy_to_clipboard

from gui.styles import *
from gui.widgets import create_button


def run_app():

    root = tk.Tk()
    root.title("Advanced Password Generator")
    root.geometry("500x500")
    root.config(bg=BG_COLOR)

    tk.Label(
        root,
        text="Advanced Password Generator",
        bg=BG_COLOR,
        fg=FG_COLOR,
        font=TITLE_FONT
    ).pack(pady=20)

    length_var = tk.IntVar(value=12)

    letters_var = tk.BooleanVar(value=True)
    numbers_var = tk.BooleanVar(value=True)
    symbols_var = tk.BooleanVar(value=True)
    exclude_var = tk.BooleanVar()

    tk.Label(root, text="Password Length", bg=BG_COLOR, fg=FG_COLOR, font=FONT).pack()

    tk.Spinbox(root, from_=4, to=50, textvariable=length_var, font=FONT).pack(pady=10)

    tk.Checkbutton(root, text="Include Letters", variable=letters_var,
                   bg=BG_COLOR, fg=FG_COLOR, selectcolor=BG_COLOR).pack()

    tk.Checkbutton(root, text="Include Numbers", variable=numbers_var,
                   bg=BG_COLOR, fg=FG_COLOR, selectcolor=BG_COLOR).pack()

    tk.Checkbutton(root, text="Include Symbols", variable=symbols_var,
                   bg=BG_COLOR, fg=FG_COLOR, selectcolor=BG_COLOR).pack()

    tk.Checkbutton(root, text="Exclude Similar Characters",
                   variable=exclude_var,
                   bg=BG_COLOR,
                   fg=FG_COLOR,
                   selectcolor=BG_COLOR).pack()

    password_entry = tk.Entry(
        root,
        width=30,
        font=("Arial", 16),
        bg=ENTRY_BG,
        fg="white"
    )

    password_entry.pack(pady=20)

    strength_label = tk.Label(
        root,
        text="",
        bg=BG_COLOR,
        fg="yellow",
        font=FONT
    )

    strength_label.pack()

    def generate():

        password = generate_password(
            length_var.get(),
            letters_var.get(),
            numbers_var.get(),
            symbols_var.get(),
            exclude_var.get()
        )

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        strength = check_strength(password)

        strength_label.config(text=f"Strength: {strength}")

    def copy():

        password = password_entry.get()

        if password:
            copy_to_clipboard(password)
            messagebox.showinfo("Copied", "Password copied successfully!")

    create_button(root, "Generate Password", generate).pack(pady=10)

    create_button(root, "Copy Password", copy).pack(pady=10)

    root.mainloop()