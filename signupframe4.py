from pathlib import Path

from tkinter import *
import os
import subprocess
from tkinter import messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\signup4_resources\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def sign_up_button_clicked():
    window.withdraw()
    # Call the signup5 function here
    subprocess.Popen(["python", "signupframe5.py"])

def signupform4_back_button():
    window.withdraw()
    # open the signupframe3.py
    subprocess.Popen(["python", "signupframe3.py"])

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
    404.0,
    98.0,
    image=image_image_1
)

canvas.create_rectangle(
    259.5927734375,
    119.0,
    583.767333984375,
    126.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    259.5927734375,
    119.0,
    480.36370849609375,
    126.0,
    fill="#F19FB5",
    outline="")

canvas.create_text(
    319.0,
    235.0,
    anchor="nw",
    text="Please enter your address?",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    265.0,
    339.0,
    anchor="nw",
    text="This is how your address will appear in the PurffectMatch",
    fill="#969696",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    330.0,
    195.0,
    anchor="nw",
    text="MEOW, MARIE!",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    410.0,
    303.0,
    image=entry_image_1
)
address_textbox = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
address_textbox.place(
    x=182.0,
    y=289.0,
    width=457.0,
    height=29.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
back_button4 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=signupform4_back_button,
    relief="flat"
)
back_button4.place(
    x=137.0,
    y=111.0,
    width=9.62713623046875,
    height=16.506439208984375
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
sign_up4_button= Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up_button_clicked,
    relief="flat"
)
sign_up4_button.place(
    x=340.0,
    y=388.0,
    width=159.0,
    height=39.0
)
window.resizable(False, False)
window.mainloop()
