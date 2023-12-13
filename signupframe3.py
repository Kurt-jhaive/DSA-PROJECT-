from tkinter import *
from tkinter import messagebox
from pathlib import Path
import subprocess


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\signup3_resources\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def sign_up_button_clicked():
    window.withdraw()
    # Call the signup4 function here
    subprocess.Popen(["python", "signupframe4.py"])

def signupform3_back_button():
    window.withdraw()
    # open the signupframe2.py
    subprocess.Popen(["python", "signupframe1.py"])

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
    width=324.174560546875,
    height=7.0
)

canvas.create_text(
    273.0,
    231.0,
    anchor="nw",
    text="What purrfect name do you prefer to go by?",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    275.0,
    338.0,
    anchor="nw",
    text="This is how your name will appear in the PurffectMatch",
    fill="#7C7C7C",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    205.0,
    186.0,
    anchor="nw",
    text="HEY THERE, FUTURE PURR PARENTS!",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    431.0,
    294.0,
    image=entry_image_1
)
name_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
name_textbox.place(
    x=202.0,
    y=280.0,
    width=457.0,
    height=29.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
signupframe3_back_button= Button(
    bg="#FFFFFF",
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=signupform3_back_button,
    relief="flat",
    activebackground="#FFFFFF",
)
signupframe3_back_button.place(
    x=137.0,
    y=111.0,
    width=9.62713623046875,
    height=16.506439208984375
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
signupframe3_next_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up_button_clicked,
    relief="flat"
)
signupframe3_next_button.place(
    x=343.0,
    y=387.0,
    width=159.0,
    height=39.0
)
window.resizable(False, False)
window.mainloop()
