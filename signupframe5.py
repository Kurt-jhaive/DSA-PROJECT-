from tkinter import *
from tkinter import messagebox
from pathlib import Path
import subprocess


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\signup5_resources\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def sign_up_button_clicked():
    window.withdraw()
    # Go back to the login page
    subprocess.Popen(["python", "loginframe.py"])

def signupform5_back_button():
    window.withdraw()
    # open the signupframe4.py
    subprocess.Popen(["python", "signupframe4.py"])


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
    x=259.5927734375,
    y=119.0,
    width=324.4072265625,
    height=7.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
sign_up5_back_button = Button(
    bg="#FFFFFF",
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=signupform5_back_button,
    relief="flat",
    activebackground="#FFFFFF",
)
sign_up5_back_button.place(
    x=137.0,
    y=111.0,
    width=9.62713623046875,
    height=16.5064697265625
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
sign_up5_next_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command= sign_up_button_clicked,
    relief="flat"
)
sign_up5_next_button.place(
    x=327.0,
    y=355.0,
    width=159.0,
    height=39.0
)

canvas.create_text(
    331.0,
    222.0,
    anchor="nw",
    text="MEOW! ARF!",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    265.0,
    267.0,
    anchor="nw",
    text="Are you excited to find your perfect match?",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)
window.resizable(False, False)
window.mainloop()
