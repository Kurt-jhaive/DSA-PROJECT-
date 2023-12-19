from tkinter import *
from tkinter import messagebox
import subprocess
import pandas as pd
import os
import sys

from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\privacy1_frame")

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
def back_button_clicked():
    window.destroy()
    subprocess.Popen(["homeframe/homeframe.exe"])
def next_button_clicked():
    window.destroy()
    exe_path = "loginframe.exe"
    subprocess.Popen([exe_path])

def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

def change_profile_display():
    #read the text file
    with open(resource_path("data/current_user.txt"), "r") as file:
        current_user = file.read().strip()
    
    #get the display name of the current user
    df = pd.read_csv(resource_path('data/profile_data.csv'))
    user_row = df[df['username'] == current_user]
    display_name = user_row['display_name'].values[0]
    display_location = user_row['address'].values[0]

    #change the display name and location
    canvas.itemconfigure(display_name_canvas, text=display_name)
    canvas.itemconfigure(profile_location, text=display_location)

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
    file=relative_to_assets(resource_path("forms/privacy1_frame/image_1.png")))
image_1 = canvas.create_image(
    409.0,
    79.0,
    image=image_image_1
)

display_name_canvas = canvas.create_text(
    115.0,
    58.0,
    anchor="nw",
    text="Marie Cris Edusma",
    fill="#FFFFFF",
    font=("Inter SemiBold", 14 * -1, "bold")
)

profile_location = canvas.create_text(
    115.0,
    77.0,
    anchor="nw",
    text="Taguig City",
    fill="#FFFFFF",
    font=("Inter SemiBold", 12 * -1, "bold")
)


image_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/privacy1_frame/image_2.png")))
image_2 = canvas.create_image(
    404.0,
    145.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets(resource_path("forms/privacy1_frame/button_1.png")))
user_button = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("user_button clicked"),
    relief="flat"
)
user_button.place(
    x=65.0,
    y=55.0,
    width=44.103515625,
    height=43.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/privacy1_frame/button_2.png")))
back_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=back_button_clicked,
    relief="flat"
)
back_button.place(
    x=537.0,
    y=421.0,
    width=112.89242553710938,
    height=39.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets(resource_path("forms/privacy1_frame/button_3.png")))
next_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=next_button_clicked,
    relief="flat"
)
next_button.place(
    x=659.0,
    y=421.0,
    width=112.89242553710938,
    height=39.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets(resource_path("forms/privacy1_frame/image_3.png")))
image_3 = canvas.create_image(
    400.0,
    206.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets(resource_path("forms/privacy1_frame/image_4.png")))
image_4 = canvas.create_image(
    409.0,
    335.0,
    image=image_image_4
)

change_profile_display()

window.resizable(False, False)
window.mainloop()
