from tkinter import *
from tkinter import messagebox
import subprocess
import os
import sys


from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\privacy3_frame")

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
    subprocess.Popen(["privacyframe2/privacyframe2.exe"])
def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()
def i_agree_button_clicked():
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
    file=relative_to_assets(resource_path("forms/privacy3_frame/image_1.png")))
image_1 = canvas.create_image(
    409.0,
    129.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/privacy3_frame/image_2.png")))
image_2 = canvas.create_image(
    407.0,
    287.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets(resource_path("forms/privacy3_frame/button_1.png")))
back_button = Button(
    image=button_image_1,
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

button_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/privacy3_frame/button_2.png")))
submit_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=i_agree_button_clicked,
    relief="flat"
)
submit_button.place(
    x=659.0,
    y=421.0,
    width=112.89242553710938,
    height=39.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets(resource_path("forms/privacy3_frame/image_3.png")))
image_3 = canvas.create_image(
    423.0,
    380.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
