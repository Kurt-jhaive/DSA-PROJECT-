


from pathlib import Path

from tkinter import *
import os
import subprocess


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\signup4_resources\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def sign_up4_next_button_clicked():
    window.withdraw()
    subprocess.Popen(["python", "signupframe5.py"])

def sign_up4_back_button_clicked():
    window.withdraw()
    subprocess.Popen(["python", "signupframe3.py"])
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
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=198.0,
    y=85.0,
    width=204.0,
    height=7.0
)

canvas.create_text(
    217.0,
    158.0,
    anchor="nw",
    text="Please enter your address?\n",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_text(
    166.0,
    247.0,
    anchor="nw",
    text="This is how your address will appear in the PurffectMatch",
    fill="#969696",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    238.0,
    130.0,
    anchor="nw",
    text=f"MEOW, !",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up4_next_button_clicked,
    relief="flat"
)
button_2.place(
    x=223.0,
    y=294.0,
    width=154.0,
    height=27.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    303.0,
    222.5,
    image=entry_image_1
)

address_textbox = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
address_textbox.place(
    x=146.0,
    y=213.0,
    width=316.0,
    height=19.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
back_button4 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up4_back_button_clicked,
    relief="flat"
)
back_button4.place(
    x=126.0,
    y=77.0,
    width=9.627197265625,
    height=16.506439208984375
)
window.resizable(False, False)
window.mainloop()
