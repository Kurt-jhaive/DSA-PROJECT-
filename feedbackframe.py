from tkinter import *
from tkinter import messagebox
import subprocess


from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\feedbackform_resources")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def back_button_clicked():
    window.destroy()
    subprocess.Popen(["python", "homeframe.py"])

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
    409.0,
    79.0,
    image=image_image_1
)

canvas.create_text(
    115.0,
    56.0,
    anchor="nw",
    text="Marie Cris Edusma",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    115.0,
    77.0,
    anchor="nw",
    text="Taguig City",
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
user_button = Button(
    bg = "#F19FB5",
    activebackground= "#F19FB5",
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("user_button clicked"),
    relief="flat"
)
user_button.place(
    x=65.0,
    y=55.0,
    width=44.103515625,
    height=43.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    412.0,
    145.0,
    image=image_image_2
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
back_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=back_button_clicked,
    relief="flat"
)
back_button.place(
    x=537.0,
    y=421.0,
    width=112.89242553710938,
    height=39.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
submit_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("submit_button clicked"),
    relief="flat"
)
submit_button.place(
    x=659.0,
    y=421.0,
    width=112.89242553710938,
    height=39.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    407.0,
    321.0,
    image=image_image_3
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
star_button1 = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("star_button1 clicked"),
    relief="flat"
)
star_button1.place(
    x=289.0,
    y=176.0,
    width=40.0,
    height=41.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
star_button2 = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("star_button2 clicked"),
    relief="flat"
)
star_button2.place(
    x=335.0,
    y=176.0,
    width=40.0,
    height=41.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
star_button3 = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("star_button3 clicked"),
    relief="flat"
)
star_button3.place(
    x=382.0,
    y=176.0,
    width=39.0,
    height=41.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
star_button4 = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("star_button4 clicked"),
    relief="flat"
)
star_button4.place(
    x=427.0,
    y=176.0,
    width=40.0,
    height=41.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
star_button5 = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("star_button5 clicked"),
    relief="flat"
)
star_button5.place(
    x=474.0,
    y=176.0,
    width=40.0,
    height=41.0
)
window.resizable(False, False)
window.mainloop()
