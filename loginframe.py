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



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r'forms\login_resources\frame0')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_entry_click(event):
    # Function to handle the click event on the Entry widgets
    if username_textbox.get() == 'Username':
        username_textbox.delete(0, "end")  # Delete default text
        username_textbox.configure(fg="black", bd=2, relief="solid")  # Change text color and outline

    if password_textbox.get() == 'Password':
        password_textbox.delete(0, "end")  # Delete default text
        password_textbox.configure(show="*", fg="black", bd=2, relief="solid")  # Change text color, show asterisks, and outline

def on_focus_out(event):
    # Function to handle the focus-out event on the Entry widgets
    if username_textbox.get() == '':
        username_textbox.insert(0, 'Username')  # Restore default text
        username_textbox.configure(fg="grey", bd=1, relief="solid")  # Change text color and outline

    if password_textbox.get() == '':
       password_textbox.insert(0, 'Password')  # Restore default text
       password_textbox.configure(show="", fg="grey", bd=1, relief="solid")  # Change text color, hide asterisks, and outline

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
x = (screen_width - 620) // 2
y = (screen_height - 600) // 2

window.geometry(f"620x400+{x}+{y}")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 405,
    width = 632,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    349.0,
    38.0,
    anchor="nw",
    text="Login",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1),

)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    165.0,
    226.0,
    image=image_image_1
)

canvas.create_text(
    349.0,
    38.0,
    anchor="nw",
    text="Login",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    474.5,
    110.0,
    image=entry_image_1
)
username_textbox = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000000",
    highlightthickness=0
)
username_textbox.place(
    x=356.0,
    y=101.0,
    width=237.0,
    height=25.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    474.5,
    166.0,
    image=entry_image_2
)
password_textbox = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000000",
    show='*',
    highlightthickness=0
)
password_textbox.place(
    x=356.0,
    y=157.0,
    width=237.0,
    height=25.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=login_button_clicked,


    relief="flat"
)
button_3.place(
    x=349.0,
    y=232.0,
    width=112.0,
    height=27.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
sign_up_button = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up_button_clicked,
    relief="flat"
)
sign_up_button.place(
    x=481.906982421875,
    y=233.0,
    width=118.093017578125,
    height=27.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=505.0,
    y=198.0,
    width=127.0,
    height=23.42340087890625
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    163.0,
    192.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
