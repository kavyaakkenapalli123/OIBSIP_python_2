import tkinter as tk
from gui.styles import *

def create_button(parent, text, command):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=BTN_COLOR,
        fg="white",
        font=FONT,
        padx=10,
        pady=5
    )