from tkinter import *
from tkinter import messagebox
import subprocess
import os
import pandas as pd

from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\adoption6_frame")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def back_button_clicked():
    window.destroy()
    subprocess.Popen(["python", "adoptframe5.py"])

def submit_button_clicked():
    if save_input():
        save_all_data()
        # reset_input()
        window.destroy()
        subprocess.Popen(["python", "homeframe.py"])

def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        # reset_input()
        window.destroy()

def save_input():
    if not all([date_textbox.get(), time_textbox.get(), q11.get()]):
        messagebox.showerror("Error", "Please fill up all fields.")
        return False
    else:
        messagebox.showinfo("Success", "Your adoption application has been submitted! Please wait for our team to contact you.")
        inputs = [date_textbox.get(), time_textbox.get(), q11.get()]
        with open("data/adopt6_data.txt", "w") as f:
            f.write('\n'.join(inputs) + '\n')
        return True

def read_input():
    # read the inputted data from the file and display it
    try:
        with open("data/adopt6_data.txt", "r") as f:
            date_textbox.insert(0, f.readline().strip())
            time_textbox.insert(0, f.readline().strip())
            q11.set(f.readline().strip())
    except FileNotFoundError:
        with open("data/adopt6_data.txt", "w") as f:
            pass

def reset_input():
    # remove the data inside the 6 files
    try:
        with open("data/adopt1_data.txt", "w") as f:
            f.truncate(0)
        with open("data/adopt2_data.txt", "w") as f:
            f.truncate(0)
        with open("data/adopt3_data.txt", "w") as f:
            f.truncate(0)
        with open("data/adopt4_data.txt", "w") as f:
            f.truncate(0)
        with open("data/adopt5_data.txt", "w") as f:
            f.truncate(0)
        with open("data/adopt6_data.txt", "w") as f:
            f.truncate(0)
    except FileNotFoundError:
        pass

def save_all_data():
    # save all the data to the database
    # read the adoptiondata from 1 to 6 and append it to the list without /n
    with open("data/adopt1_data.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    with open("data/adopt2_data.txt", "r") as f:
        data += [line.strip() for line in f.readlines()]
    with open("data/adopt3_data.txt", "r") as f:
        data += [line.strip() for line in f.readlines()]
    with open("data/adopt4_data.txt", "r") as f:
        data += [line.strip() for line in f.readlines()]
    with open("data/adopt5_data.txt", "r") as f:
        data += [line.strip() for line in f.readlines()]
    with open("data/adopt6_data.txt", "r") as f:
        data += [line.strip() for line in f.readlines()]

    # save the data to the database using pandas
    df = pd.read_csv("data/adoption_data.csv")
    df = pd.DataFrame([data], columns=df.columns)
    df.to_csv("data/adoption_data.csv", mode='a', header=False, index=False)


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
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
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
    file=relative_to_assets("button_2.png"))
submit_button = Button(
    bg="#FFFFFF",
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=submit_button_clicked,
    relief="flat"
)
submit_button.place(
    x=657.0,
    y=407.0,
    width=125.0,
    height=39.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    328.0,
    59.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    174.0,
    92.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    174.0,
    190.0,
    image=image_image_3
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    bg="#FFFFFF",
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    activebackground="#FFFFFF",    
)
button_3.place(
    x=56.0,
    y=121.0,
    width=338.0,
    height=50.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    bg="#FFFFFF",
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    activebackground="#FFFFFF",
)
button_4.place(
    x=55.0,
    y=213.0,
    width=338.0,
    height=50.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    267.0,
    292.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    64.0,
    324.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    103.0,
    327.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    182.0,
    324.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    216.0,
    327.0,
    image=image_image_8
)
date_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
date_textbox.place(
    x=62.0,
    y=137.0,
    width=317.0,
    height=28.0
)
time_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
time_textbox.place(
    x=67.0,
    y=230.0,
    width=317.0,
    height=28.0
)


# Will you be able to visit the shelter for the meet-and-greet?
q11 = StringVar()

dot_image = PhotoImage(file=relative_to_assets("dot.png"))
black_dot_image = PhotoImage(file=relative_to_assets("black_dot.png"))
black_dot_small_image = PhotoImage(file=relative_to_assets("black_dot_small.png"))
pink_dot_image = PhotoImage(file=relative_to_assets("pink_dot.png"))
yes6_radio = Radiobutton(
    variable=q11,
    value='yes',
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    bd=0,
    indicatoron=False,
    image=dot_image,
    selectimage=pink_dot_image,
)
yes6_radio.place(
    x=56,
    y=316
)
no6_radio = Radiobutton(
    variable=q11,
    value='no',
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    bd=0,
    indicatoron=False,
    image=dot_image,
    selectimage=pink_dot_image,
)
no6_radio.place(
    x=174,
    y=316
)

read_input()

window.resizable(False, False)
window.mainloop()
