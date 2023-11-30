import customtkinter as ctk
from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
import subprocess


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path (r"forms\signup5_resources\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window = Tk()

def sign_up5_back_button_clicked():
    window.withdraw()
    subprocess.Popen(["python", "loginframe.py"])
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
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    296.0,
    57.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
sign_up5_back_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up5_back_button_clicked,
    relief="flat"
)
sign_up5_back_button.place(
    x=230.0,
    y=294.0,
    width=154.39837646484375,
    height=27.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=205.0,
    y=85.0,
    width=204.0,
    height=7.0
)

canvas.create_text(
    188.0,
    201.0,
    anchor="nw",
    text="Are you excited to find your perfect match?",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_text(
    253.0,
    172.0,
    anchor="nw",
    text="MEOW! AFR!",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=126.0,
    y=77.0,
    width=9.627197265625,
    height=16.506439208984375
)
window.resizable(False, False)
window.mainloop()
