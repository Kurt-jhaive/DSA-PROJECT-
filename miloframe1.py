
import customtkinter as ctk
import pandas as pd
from PIL import Image, ImageTk
from tkinter import messagebox
import smtplib
import random
import shutil
import os
from time import sleep

from pathlib import Path

from tkinter import *
import os
import subprocess


from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\miloform1_resources\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

window = Tk()

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the protocol for the window close event
window.protocol("WM_DELETE_WINDOW", close_window)

# Calculate the x and y coordinates for the window to be centered
x = (screen_width - 820) // 2
y = (screen_height - 500) // 2

window.geometry(f"820x500+{x}+{y}")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 820,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    544.0,
    309.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    158.0,
    251.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    388.0,
    72.0,
    image=image_image_3
)

canvas.create_text(
    582.0,
    167.0,
    anchor="nw",
    text="MILO, 1",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    448.0,
    307.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    673.0,
    399.0,
    image=image_image_5
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
dogs_filter_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("dogs filter button clicked"),
    relief="flat"
)
dogs_filter_button.place(
    x=416.0,
    y=90.0,
    width=79.0,
    height=30.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
cats_filter_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("cats filter button clicked"),
    relief="flat"
)
cats_filter_button.place(
    x=521.0,
    y=90.0,
    width=79.0,
    height=30.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
favorites_button= Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
favorites_button.place(
    x=715.0,
    y=48.0,
    width=27.0,
    height=23.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
menu_button = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
menu_button.place(
    x=750.0,
    y=49.0,
    width=19.0,
    height=22.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
filter_button = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("filter button clicked"),
    relief="flat"
)
filter_button.place(
    x=311.0,
    y=90.0,
    width=79.0,
    height=30.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
home_button = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("home button clicked"),
    relief="flat"
)
home_button.place(
    x=95.0,
    y=155.0,
    width=120.0,
    height=30.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
register_button = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("register button clicked"),
    relief="flat"
)
register_button.place(
    x=95.0,
    y=204.0,
    width=127.0,
    height=30.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
donate_button = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("donate button clicked"),
    relief="flat"
)
donate_button.place(
    x=95.0,
    y=253.0,
    width=127.0,
    height=30.0
)

canvas.create_text(
    115.0,
    65.0,
    anchor="nw",
    text="Marie Cris Edusma",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    115.0,
    85.0,
    anchor="nw",
    text="Taguig City",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=65.0,
    y=64.0,
    width=34.0,
    height=36.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
close_button = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("X button clicked"),
    relief="flat"
)
close_button.place(
    x=621.0,
    y=123.0,
    width=42.0,
    height=43.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
add_to_favorites_button = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("add to favorites button clicked"),
    relief="flat"
)
add_to_favorites_button.place(
    x=669.0,
    y=123.0,
    width=43.0,
    height=44.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
description_button = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
description_button.place(
    x=718.0,
    y=122.0,
    width=46.0,
    height=46.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
adopt_button = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("adopt button clicked"),
    relief="flat"
)
adopt_button.place(
    x=581.0,
    y=414.0,
    width=183.0,
    height=37.0
)

canvas.create_rectangle(
    215.0,
    151.99999378994107,
    229.83099189214408,
    187.3240229487419,
    fill="#F19FB5",
    outline="")

canvas.create_rectangle(
    215.0,
    203.99999378994107,
    229.83099189214408,
    239.3240229487419,
    fill="#F19FB5",
    outline="")

canvas.create_rectangle(
    216.0,
    253.99999378994107,
    230.83099189214408,
    289.3240229487419,
    fill="#F19FB5",
    outline="")

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    674.0,
    288.0,
    image=image_image_6
)
window.resizable(False, False)
window.mainloop()
