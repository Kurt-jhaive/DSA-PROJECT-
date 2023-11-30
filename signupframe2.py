
from pathlib import Path

from tkinter import *
import os
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\signup2_resources\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def signupform2_signup_button():
    # Store the values before withdrawing the window
    confirm_password_value = confirm_password.get()
    email_address_value = email_address.get()
    contact_number_value = contact_number.get()

    window.withdraw()

    # open the signupframe3.py and pass the stored values as arguments
    subprocess.Popen(["python", "signupframe3.py", confirm_password_value, email_address_value, contact_number_value])

def signupform2_back_button():
    window.withdraw()
    # open the signupframe3.py without passing any arguments
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
# Create StringVar variables to store the values of Entry widgets
confirm_password_var = StringVar()
email_address_var = StringVar()
contact_number_var = StringVar()

confirm_password = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    show='*',
    highlightthickness=0,
    textvariable=confirm_password_var
)
email_address = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=email_address_var
)
contact_number = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=contact_number_var
)

# Set the values of Entry widgets from the StringVar variables
confirm_password.insert(0, confirm_password_var.get())
email_address.insert(0, email_address_var.get())
contact_number.insert(0, contact_number_var.get())

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 400,
    width = 620,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
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
    x=615.0,
    y=209.0,
    width=5.0,
    height=76.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    163.0,
    200.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    163.0,
    190.0,
    image=image_image_2
)

canvas.create_text(
    345.0,
    41.0,
    anchor="nw",
    text="Sign Up ",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    470.5,
    113.0,
    image=entry_image_1
)
confirm_password = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    show = '*',
    highlightthickness=0
)
confirm_password.place(
    x=354.0,
    y=103,
    width=236.0,
    height=26.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    470.5,
    168.0,
    image=entry_image_2
)
email_address = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
email_address.place(
    x=354.0,
    y=158.0,
    width=236.0,
    height=26.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    470.5,
    223.0,
    image=entry_image_3
)
contact_number = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
contact_number.place(
    x=354.0,
    y=213.0,
    width=236.0,
    height=26.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
signupframe2_signup_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=signupform2_signup_button,
    relief="flat"
)
signupframe2_signup_button.place(
    x=418.0,
    y=274.0,
    width=112.0,
    height=27.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
terms_and_conditions = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
terms_and_conditions.place(
    x=345.0,
    y=331.0,
    width=251.0,
    height=46.0
)

window.resizable(False, False)
window.mainloop()
