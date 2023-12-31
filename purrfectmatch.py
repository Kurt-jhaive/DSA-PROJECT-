from tkinter import *
from tkinter import messagebox
import pandas as pd
import os
import subprocess
from pathlib import Path
import sys


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r'forms\login_frame')

# ---------------------------- PATH ------------------------------- #
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def login_button_clicked():
    global user_id

    df = pd.read_csv(resource_path("data/profile_data.csv"))

    entered_username = username_textbox.get()
    entered_password = password_textbox.get()

    user_record = df[(df['username'] == entered_username) & (df['password'] == entered_password)]

    if not user_record.empty:
        #put the username in a text file
        with open(resource_path("data/current_user.txt"), "w") as file:
            file.write(entered_username)
        messagebox.showinfo("Login Successful", "Welcome, {}!".format(entered_username))
        window.destroy()
        subprocess.Popen(["homeframe/homeframe.exe"])
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
        
# function that opens a defined exe file when clicked

def sign_up_button_clicked():
    window.destroy()
    subprocess.Popen(["signupframe1/signupframe1.exe"])

def forgot_password_button_clicked():
    window.destroy()
    subprocess.Popen(["forgetpassframe1/forgetpassframe1.exe"])

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
    file=relative_to_assets(resource_path("forms/purrfectmatch_frame/image_1.png")))
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
    file=relative_to_assets(resource_path("forms/purrfectmatch_frame/button_1.png")))
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
    file=relative_to_assets(resource_path("forms/purrfectmatch_frame/button_2.png")))
forgot_password_button = Button(
    bg="#FFFFFF",
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=forgot_password_button_clicked,
    relief="flat",
    activebackground="#FFFFFF",

)
forgot_password_button .place(
    x=658.0,
    y=267.00010681152344,
    width=161.62887573242188,
    height=34.91102600097656
)

entry_image_1 = PhotoImage(
    file=relative_to_assets(resource_path("forms/purrfectmatch_frame/entry_1.png")))
entry_bg_1 = canvas.create_image(
    592.5,
    223.27298736572266,
    image=entry_image_1
)
username_textbox = Entry(
    font=("Inter", 15 * -1),
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
    file=relative_to_assets(resource_path("forms/purrfectmatch_frame/entry_2.png")))
entry_bg_2 = canvas.create_image(
    592.5,
    141.29910278320312,
    image=entry_image_2
)
password_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show='*'
    
)
password_textbox.place(
    x=421.0,
    y=213.0,
    width=344.0,
    height=36.59820556640625
)

button_image_3 = PhotoImage(
    file=relative_to_assets(resource_path("forms/purrfectmatch_frame/button_3.png")))
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
    file=relative_to_assets(resource_path("forms/purrfectmatch_frame/image_2.png")))
image_2 = canvas.create_image(
    179.0,
    221.0,
    image=image_image_2
)

window.resizable(False, False)
window.mainloop()
