
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
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\registerform_resources\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def home_button_clicked():
    window.destroy()
    subprocess.Popen(["python", "miloframe1.py"])
def donate_button_clicked():
    window.destroy()
    subprocess.Popen(["python", "donateframe.py"])

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
    388.0,
    72.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
favorites_button = Button(
    image=button_image_1,
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

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
menu_button = Button(
    image=button_image_2,
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
    102.0,
    65.0,
    anchor="nw",
    text="Marie Cris Edusma",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    102.0,
    81.0,
    anchor="nw",
    text="Taguig City",
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
home_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=home_button_clicked,
    relief="flat"
)
home_button.place(
    x=95.0,
    y=155.0,
    width=120.0,
    height=30.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
register_button = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("register_button clicked"),
    relief="flat"
)
register_button.place(
    x=95.0,
    y=204.0,
    width=120.0,
    height=30.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
donate_button = Button(
    image=button_image_5,
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

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=65.0,
    y=64.0,
    width=34.0,
    height=36.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    416.0,
    113.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    416.0,
    171.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    416.0,
    234.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    539.0,
    333.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    664.0,
    237.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    664.0,
    172.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    664.0,
    111.0,
    image=image_image_9
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
upload_image_button = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("upload_image_button clicked"),
    relief="flat"
)
upload_image_button.place(
    x=311.0,
    y=411.0,
    width=159.0,
    height=39.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
submit_button = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("submit_button clicked"),
    relief="flat"
)
submit_button.place(
    x=486.0,
    y=411.0,
    width=159.0,
    height=39.0
)
petname_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
petname_textbox .place(
    x=316.0,
    y=105.0,
    width=195.0,
    height=27
)
breed_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
breed_textbox.place(
    x=568.0,
    y=105.0,
    width=195.0,
    height=27
)
age_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
age_textbox.place(
    x=316.0,
    y=164.0,
    width=195.0,
    height=27
)
gender_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
gender_textbox.place(
    x=568.0,
    y=164.0,
    width=195.0,
    height=27
)
color_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
color_textbox.place(
    x=316.0,
    y=227.0,
    width=195.0,
    height=27
)
size_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
size_textbox.place(
    x=568.0,
    y=227.0,
    width=195.0,
    height=27
)
description_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
description_textbox.place(
    x=316.0,
    y=295.0,
    width=447.0,
    height=91
)
window.resizable(False, False)
window.mainloop()
