
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
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\kairaform1_resources\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def register_button_clicked():
    window.destroy()
    subprocess.Popen(["python", "registerframe.py"])
def donate_button_clicked():
    window.destroy()
    subprocess.Popen(["python", "donateframe.py"])
def description_button_clicked():
    window.destroy()
    subprocess.Popen(["python", "kairaframe2description.py"])

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
    158.0,
    251.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    372.0,
    72.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    544.0,
    312.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    672.0,
    381.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    448.0,
    307.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    668.0,
    285.0,
    image=image_image_6
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
dogs_filter_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("dogs_filter_button clicked"),
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
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("cats_filter_button clicked"),
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
filter_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("filter_button clicked"),
    relief="flat"
)
filter_button.place(
    x=311.0,
    y=90.0,
    width=79.0,
    height=30.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
home_button = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("home_button clicked"),
    relief="flat"
)
home_button.place(
    x=95.0,
    y=155.0,
    width=120.0,
    height=30.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
register_button = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=register_button_clicked,
    relief="flat"
)
register_button.place(
    x=95.0,
    y=204.0,
    width=120.0,
    height=30.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
donate_button = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=donate_button_clicked,
    relief="flat"
)
donate_button.place(
    x=95.0,
    y=253.0,
    width=120.0,
    height=30.0
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    641.0,
    189.0,
    image=image_image_7
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
adopt_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("adopt_button clicked"),
    relief="flat"
)
adopt_button.place(
    x=585.0,
    y=415.0,
    width=183.0,
    height=37.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
favorites_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("favorites_button clicked"),
    relief="flat"
)
favorites_button.place(
    x=713.0,
    y=42.0,
    width=31.0,
    height=34.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
menu_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("menu_button clicked"),
    relief="flat"
)
menu_button.place(
    x=749.0,
    y=42.0,
    width=23.0,
    height=35.0
)

canvas.create_text(
    105.0,
    68.0,
    anchor="nw",
    text="Marie Cris Edusma",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    105.0,
    84.0,
    anchor="nw",
    text="Taguig City",
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=68.0,
    y=67.0,
    width=34.0,
    height=36.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
close_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("close_button clicked"),
    relief="flat"
)
close_button.place(
    x=624.0,
    y=126.0,
    width=42.0,
    height=43.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
add_to_favorites_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("add_to_favorites_button clicked"),
    relief="flat"
)
add_to_favorites_button.place(
    x=672.0,
    y=126.0,
    width=43.0,
    height=44.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
description_button= Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=description_button_clicked,
    relief="flat"
)
description_button.place(
    x=721.0,
    y=125.0,
    width=46.0,
    height=46.0
)
window.resizable(False, False)
window.mainloop()
