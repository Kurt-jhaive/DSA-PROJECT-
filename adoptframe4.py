from tkinter import *
from tkinter import messagebox
import subprocess
import os
import sys

from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\adoption4_frame")

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
    subprocess.Popen(["adoptframe3/adoptframe3.exe"])
def next_button_clicked():
    if save_input():
        window.destroy()
        subprocess.Popen(["adoptframe5/adoptframe5.exe"])

def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

def save_input():
    if not all([question4_textbox.get(), question5_textbox.get(), question6_textbox.get(), q8.get()]):
        messagebox.showerror("Error", "Please fill up all fields.")
        return False
    else:
        messagebox.showinfo("Success", "Please proceed to the next set of questions.")
        inputs = [question4_textbox.get(), question5_textbox.get(), question6_textbox.get(), q8.get()]
        with open(resource_path("data/adopt4_data.txt"), "w") as f:
            f.write('\n'.join(inputs) + '\n')
        return True
    
def read_input():
    # read the inputted data from the file and display it
    try:
        with open(resource_path("data/adopt4_data.txt"), "r") as f:
            question4_textbox.insert(0, f.readline().strip())
            question5_textbox.insert(0, f.readline().strip())
            question6_textbox.insert(0, f.readline().strip())
            q8.set(f.readline().strip())
    except FileNotFoundError:
        with open(resource_path("data/adopt4_data.txt"), "w") as f:
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
    height = 500,
    width = 820,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption4_frame/image_1.png")))
image_1 = canvas.create_image(
    289.0,
    139.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption4_frame/image_2.png")))
image_2 = canvas.create_image(
    394.0,
    191.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption4_frame/image_3.png")))
image_3 = canvas.create_image(
    394.0,
    98.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption4_frame/image_4.png")))
image_4 = canvas.create_image(
    394.0,
    289.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption4_frame/button_1.png")))
back_button = Button(
    image=button_image_1,
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

button_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption4_frame/button_2.png")))
next_button = Button(
    image=button_image_2,
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

image_image_5 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption4_frame/image_5.png")))
image_5 = canvas.create_image(
    319.0,
    54.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption4_frame/image_6.png")))
image_6 = canvas.create_image(
    338.0,
    242.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption4_frame/image_7.png")))
image_7 = canvas.create_image(
    285.0,
    348.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption4_frame/image_8.png")))
image_8 = canvas.create_image(
    63.0,
    383.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption4_frame/image_9.png")))
image_9 = canvas.create_image(
    102.0,
    386.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption4_frame/image_10.png")))
image_10 = canvas.create_image(
    181.0,
    383.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption4_frame/image_11.png")))
image_11 = canvas.create_image(
    216.0,
    386.0,
    image=image_image_11
)
question4_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
question4_textbox.place(
    x=62.0,
    y=84.0,
    width=665.0,
    height=31.0
)
question5_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
question5_textbox.place(
    x=62.0,
    y=177.0,
    width=665.0,
    height=31.0
)
question6_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
question6_textbox.place(
    x=62.0,
    y=274.0,
    width=665.0,
    height=31.0
)
# Does everyone in the family support your decision to adopt a pet?
q8 = StringVar() 

dot_image = PhotoImage(file=relative_to_assets(resource_path("forms/adoption4_frame/dot.png")))
black_dot_image = PhotoImage(file=relative_to_assets(resource_path("forms/adoption4_frame/black_dot.png")))
black_dot_small_image = PhotoImage(file=relative_to_assets(resource_path("forms/adoption4_frame/black_dot_small.png")))
pink_dot_image = PhotoImage(file=relative_to_assets(resource_path("forms/adoption4_frame/pink_dot.png")))
yes3_radio = Radiobutton(
    variable=q8,
    value='yes',
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    bd=0,
    indicatoron=False,
    image=dot_image,
    selectimage=pink_dot_image,
)
yes3_radio.place(
    x=55,
    y=375
)
no3_radio = Radiobutton(
    variable=q8,
    value='no',
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    bd=0,
    indicatoron=False,
    image=dot_image,
    selectimage=pink_dot_image,
)
no3_radio.place(
    x=173,
    y=375
)

read_input()

window.resizable(False, False)
window.mainloop()
