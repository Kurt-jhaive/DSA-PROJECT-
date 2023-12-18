from tkinter import *
from tkinter import messagebox
import subprocess
import pandas as pd


from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\hamburger_frame")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    415.0,
    252.0,
    image=image_image_1
)


# HAMBURGER FRAME
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    654.0,
    194.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
account_settings = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("account_settings clicked"),
    relief="flat"
)
account_settings.place(
    x=549.0,
    y=96.0,
    width=205.0,
    height=30.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
terms_conditions = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("terms_conditions clicked"),
    relief="flat"
)
terms_conditions.place(
    x=549.0,
    y=173.0,
    width=205.0,
    height=29.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
give_feedback = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("give_feedback clicked"),
    relief="flat"
)
give_feedback.place(
    x=551.0,
    y=212.0,
    width=202.0,
    height=32.291259765625
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
log_out = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("log_out clicked"),
    relief="flat"
)
log_out.place(
    x=550.0,
    y=256.0,
    width=204.0,
    height=31.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
privacy_policy = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("privacy_policy clicked"),
    relief="flat"
)
privacy_policy.place(
    x=550.0,
    y=133.0,
    width=203.99925231933594,
    height=32.0
)
window.resizable(False, False)
window.mainloop()
