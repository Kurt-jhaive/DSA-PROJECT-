from tkinter import *
from tkinter import messagebox
import subprocess
import pandas as pd


from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\favorites1_frame")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def home_button_clicked():
    window.destroy()
    subprocess.Popen(["python", "homeframe.py"])

def register_button_clicked():
    window.destroy()
    subprocess.Popen(["python", "registerframe.py"])

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
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("favorites_button clicked"),
    relief="flat"
)
favorites_button.place(
    x=705.0,
    y=46.0,
    width=37.0,
    height=35.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
menu_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
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
    bg="#F19FB5",
    activebackground="#F19FB5",
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
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=register_button_clicked,
    relief="flat"
)
register_button.place(
    x=92.0,
    y=204.0,
    width=127.0,
    height=30.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
donate_button = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=donate_button_clicked,
    relief="flat"
)
donate_button.place(
    x=93.0,
    y=253.0,
    width=127.0,
    height=30.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
user_button = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("user_button clicked"),
    relief="flat"
)
user_button.place(
    x=65.0,
    y=64.0,
    width=34.0,
    height=36.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    540.0,
    147.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    540.0,
    242.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    540.0,
    335.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    350.0,
    146.0,
    image=image_image_6
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
adopt_button1 = Button(
    bg="#F8CBD7",
    activebackground="#F8CBD7",
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("adopt_button1 clicked"),
    relief="flat"
)
adopt_button1.place(
    x=578.0,
    y=131.0,
    width=183.0,
    height=37.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
adopt_button2 = Button(
    bg="#F8CBD7",
    activebackground="#F8CBD7",
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("adopt_button2 clicked"),
    relief="flat"
)
adopt_button2.place(
    x=578.0,
    y=225.0,
    width=183.0,
    height=37.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
adopt_button3 = Button(
    bg="#F8CBD7",
    activebackground="#F8CBD7",
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("adopt_button3 clicked"),
    relief="flat"
)
adopt_button3.place(
    x=578.0,
    y=316.0,
    width=183.0,
    height=37.0
)

canvas.create_text(
    393.0,
    341.0,
    anchor="nw",
    text="4 year old",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_text(
    393.0,
    323.0,
    anchor="nw",
    text="Aspin \n",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    393.0,
    307.0,
    anchor="nw",
    text="LEVIS, Female",
    fill="#AD206C",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    388.0,
    248.0,
    anchor="nw",
    text=" 3½ year old ",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_text(
    393.0,
    229.0,
    anchor="nw",
    text="Aspin \n",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    392.0,
    215.0,
    anchor="nw",
    text="FIONA, Female",
    fill="#AD206C",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    393.0,
    156.0,
    anchor="nw",
    text="2 year old",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_text(
    393.0,
    138.0,
    anchor="nw",
    text="Aspin \n",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    393.0,
    122.0,
    anchor="nw",
    text="MILO, Male",
    fill="#AD206C",
    font=("Inter Bold", 16 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    350.0,
    242.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    350.0,
    335.0,
    image=image_image_8
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
next_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("next_button clicked"),
    relief="flat"
)
next_button.place(
    x=656.0,
    y=405.0,
    width=112.89242553710938,
    height=39.0
)
window.resizable(False, False)
window.mainloop()
