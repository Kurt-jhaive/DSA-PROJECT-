from tkinter import *
from tkinter import messagebox
import subprocess
import pandas as pd
import os
import sys

from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\adoption1_frame")


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
    subprocess.Popen(["homeframe/homeframe.exe"])
def next_button_clicked():
    if save_input():
        window.destroy()
        subprocess.Popen(["adoptframe2/adoptframe2.exe"])
def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()
    
def change_profile_display():
    #read the text file
    with open(resource_path("../../_internal/data/current_user.txt"), "r") as file:
        current_user = file.read().strip()
    
    #get the display name of the current user
    df = pd.read_csv(resource_path("../../_internal/data/profile_data.csv"))
    user_row = df[df['username'] == current_user]
    display_name = user_row['display_name'].values[0]
    display_location = user_row['address'].values[0]

    #change the display name and location
    canvas.itemconfigure(display_name_canvas, text=display_name)
    canvas.itemconfigure(profile_location, text=display_location)

def save_input():
    if not all([name_textbox.get(), birthdate_textbox.get(), address_textbox.get(), occupation_textbox.get(), email_textbox.get(), phone_textbox.get(), socialmedia_textbox.get()]):
        messagebox.showerror("Error", "Please fill up all fields.")
        return False
    else:
        messagebox.showinfo("Success", "Please proceed to the next set of questions.")
        inputs = [name_textbox.get(), birthdate_textbox.get(), address_textbox.get(), occupation_textbox.get(), email_textbox.get(), phone_textbox.get(), socialmedia_textbox.get()]
        with open(resource_path("../../_internal/data/adopt1_data.txt"), "w") as f:
            f.write('\n'.join(inputs) + '\n')
        return True

def read_input():
    # read the inputted data from the file and display it
    try:
        with open(resource_path("../../_internal/data/adopt1_data.txt"), "r") as f:
            name_textbox.insert(0, f.readline().strip())
            birthdate_textbox.insert(0, f.readline().strip())
            address_textbox.insert(0, f.readline().strip())
            occupation_textbox.insert(0, f.readline().strip())
            email_textbox.insert(0, f.readline().strip())
            phone_textbox.insert(0, f.readline().strip())
            socialmedia_textbox.insert(0, f.readline().strip())
    except FileNotFoundError:
        with open(resource_path("../../_internal/data/adopt1_data.txt"), "w") as f:
            pass

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
    height = 527,
    width = 819,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption1_frame/image_1.png")))
image_1 = canvas.create_image(
    409.0,
    79.0,
    image=image_image_1
)

display_name_canvas = canvas.create_text(
    115.0,
    58.0,
    anchor="nw",
    text="Marie Cris Edusma",
    fill="#FFFFFF",
    font=("Inter SemiBold", 14 * -1, "bold")
)

profile_location = canvas.create_text(
    115.0,
    77.0,
    anchor="nw",
    text="Taguig City",
    fill="#FFFFFF",
    font=("Inter SemiBold", 12 * -1, "bold")
)

button_image_1 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption1_frame/button_1.png")))
button_1 = Button(
    bg="#F19FB5",
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    activebackground="#F19FB5",
)
button_1.place(
    x=65.0,
    y=55.0,
    width=44.103515625,
    height=43.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption1_frame/image_2.png")))
image_2 = canvas.create_image(
    425.0,
    140.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption1_frame/image_3.png")))
image_3 = canvas.create_image(
    111.0,
    158.0,
    image=image_image_3
)

button_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption1_frame/button_2.png")))
back_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=back_button_clicked,
    relief="flat"
)
back_button.place(
    x=535.0,
    y=407.0,
    width=112.89242553710938,
    height=39.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption1_frame/button_3.png")))
next_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=next_button_clicked,
    relief="flat"
)
next_button.place(
    x=657.0,
    y=407.0,
    width=112.89242553710938,
    height=39.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption1_frame/image_4.png")))
image_4 = canvas.create_image(
    216.0,
    435.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption1_frame/image_5.png")))
image_5 = canvas.create_image(
    603.0,
    367.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption1_frame/image_6.png")))
image_6 = canvas.create_image(
    216.0,
    367.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption1_frame/image_7.png")))
image_7 = canvas.create_image(
    603.0,
    295.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption1_frame/image_8.png")))
image_8 = canvas.create_image(
    216.0,
    295.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption1_frame/image_9.png")))
image_9 = canvas.create_image(
    603.0,
    221.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption1_frame/image_10.png")))
image_10 = canvas.create_image(
    216.0,
    221.0,
    image=image_image_10
)
name_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,

)
name_textbox.place(
    x=58.0,
    y=216.0,
    width=315.0,
    height=23
)
birthdate_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,

)
birthdate_textbox.place(
    x=445.0,
    y=216.0,
    width=315.0,
    height=23
)
address_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,

)
address_textbox.place(
    x=58.0,
    y=289.0,
    width=315.0,
    height=23
)
occupation_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,

)
occupation_textbox.place(
    x=445.0,
    y=289.0,
    width=315.0,
    height=23
)
email_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,

)
email_textbox.place(
    x=58.0,
    y=359.0,
    width=315.0,
    height=23
)
phone_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,

)
phone_textbox.place(
    x=445.0,
    y=359.0,
    width=315.0,
    height=23
)
socialmedia_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,

)
socialmedia_textbox.place(
    x=58.0,
    y=429.0,
    width=315.0,
    height=23
)

change_profile_display()
read_input()

window.resizable(False, False)
window.mainloop()
