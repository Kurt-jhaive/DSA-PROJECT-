from tkinter import *
from tkinter import messagebox
import subprocess
import pandas as pd
import os
import sys

from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\thankyou_donate")

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

# function that opens a defined exe file when clicked

def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

def continue_button_clicked():
    window.destroy()
    subprocess.Popen(["homeframe/homeframe.exe"])

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
    file=relative_to_assets(resource_path("forms/thankyou_donate/image_1.png")))
image_1 = canvas.create_image(
    409.0,
    252.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets(resource_path("forms/thankyou_donate/button_1.png")))
continue_button = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=continue_button_clicked,
    relief="flat"
)
continue_button.place(
    x=318.0,
    y=376.0,
    width=174.0,
    height=37.0
)
window.resizable(False, False)
window.mainloop()
