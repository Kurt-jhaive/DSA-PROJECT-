


import customtkinter as ctk
import pandas as pd
from PIL import Image
from tkinter import messagebox
import smtplib
import random
import shutil
import os
from pathlib import Path

from tkinter import *
import os
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\signup1_resources\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def sign_up1_back_button_clicked():
    window.withdraw()
    subprocess.Popen(["python", "loginframe.py"])

def sign_up1_next_button_clicked():
    window.withdraw()
    subprocess.Popen(["python", "signupframe2.py"])
window = Tk()
# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates for the window to be centered
x = (screen_width - 620) // 2
y = (screen_height - 600) // 2

window.geometry(f"620x400+{x}+{y}")
window.configure(bg="#FFFFFF")



canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 400,
    width = 620,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    349.0,
    37.0,
    anchor="nw",
    text="Sign Up ",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)
scrollable_frame = Frame(canvas, bg="#FFFFFF")
canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    scrollable_frame,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.pack(side="top")
button_1.place(
    x=615.0,
    y=60.0,
    width=5.0,
    height=76.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    163.0,
    200.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    474.5,
    109.0,
    image=entry_image_1
)
first_name_signup = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
first_name_signup.place(
    x=359.0,
    y=99.0,
    width=235.0,
    height=27.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    474.5,
    274.0,
    image=entry_image_2
)


entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    474.5,
    335.0,
    image=entry_image_3
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    474.5,
    164.0,
    image=entry_image_4
)
middle_name_signup = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
middle_name_signup.place(
    x=359.0,
    y=154.0,
    width=235.0,
    height=27.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    474.5,
    219.0,
    image=entry_image_5
    
)
last_name_signup = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
last_name_signup.place(
    x=359.0,
    y=209.0,
    width=235.0,
    height=27.0
)
user_name_signup = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
user_name_signup.place(
    x=359.0,
    y=264.0,
    width=235.0,
    height=27.0
)

password_signup = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    show = '*',
    highlightthickness=0
)
password_signup.place(
    x=359.0,
    y=326.0,
    width=235.0,
    height=27.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    163.0,
    190.0,
    image=image_image_2
)
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
next_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up1_next_button_clicked,
    relief="flat"
)
next_button.place(
    x=523.0,
    y=369.0,
    width=77.0,
    height=27.0
)
button_image_3 =PhotoImage(
    file=relative_to_assets("back_button.png"))
back_button= Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up1_back_button_clicked,
    relief="flat"
)
back_button.place(
    x=349.0,
    y=369.0,
    width=77.0,
    h=27.0
)
window.resizable(False, False)
window.mainloop()




