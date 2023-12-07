
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

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r'forms\login_resources\assets\frame0')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def check_login():
    global user_id

    df = pd.read_csv(r'data\new_credentials.csv')

    entered_username = username_textbox.get()
    entered_password = password_textbox.get()

    user_record = df[(df['username'] == entered_username) & (df['password'] == entered_password)]

    if not user_record.empty:
        user_id = user_record['user_id'].values[0]
        messagebox.showinfo("Login Successful", "Welcome, {}!".format(entered_username))
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
        
def login_button_clicked():
    check_login()

def sign_up_button_clicked():
    # close the process of the loginframe.py window
    window.destroy()
    
    # Run signupframe1.py
    subprocess.Popen(["python", "signupframe1.py"])

def forgot_password_button_clicked():
    window.destroy()
    subprocess.Popen(["python", "forgetpassframe.py"])

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
    190.0,
    250.0,
    image=image_image_1
)

canvas.create_text(
    410.0,
    48.0,
    anchor="nw",
    text="Login",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
login_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login_button_clicked,
    relief="flat"
)
login_button.place(
    x=410.0,
    y=326.0,
    width=159.0,
    height=39.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
forgot_password_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=forgot_password_button_clicked,
    relief="flat"
)
forgot_password_button .place(
    x=658.0,
    y=267.00010681152344,
    width=161.62887573242188,
    height=34.91102600097656
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    592.5,
    223.27298736572266,
    image=entry_image_1
)
username_textbox = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
username_textbox.place(
    x=421.0,
    y=131.973876953125,
    width=344.0,
    height=36.59822082519531
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    592.5,
    141.29910278320312,
    image=entry_image_2
)
password_textbox = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
    
)
password_textbox.place(
    x=421.0,
    y=213.0,
    width=344.0,
    height=36.59820556640625
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
sign_up_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command= sign_up_button_clicked,
    relief="flat"
)
sign_up_button.place(
    x=616.0,
    y=326.0,
    width=159.0,
    height=39.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    179.0,
    221.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
