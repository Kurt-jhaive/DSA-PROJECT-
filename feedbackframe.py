from tkinter import *
from tkinter import messagebox
import subprocess
import pandas as pd
import os   
import sys

from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\feedback_frame")

# ---------------------------- PATH ------------------------------- #
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


ratings = 0

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def back_button_clicked():
    window.destroy()
    subprocess.Popen(["homeframe/homeframe.exe"])
def submit_button_clicked():
    if save_input():
        messagebox.showinfo("Success", "Your feedback has been submitted!")
        window.destroy()
        subprocess.Popen(["homeframe/homeframe.exe"])
def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

def change_profile_display():
    #read the text file
    with open(resource_path("data/current_user.txt"), "r") as file:
        current_user = file.read().strip()
    
    #get the display name of the current user
    df = pd.read_csv(resource_path('data/profile_data.csv'))
    user_row = df[df['username'] == current_user]
    display_name = user_row['display_name'].values[0]
    display_location = user_row['address'].values[0]

    #change the display name and location
    canvas.itemconfigure(display_name_canvas, text=display_name)
    canvas.itemconfigure(profile_location, text=display_location)

def save_input():
    feedback = feedback_textbox.get("1.0", END).strip()
    with open(resource_path("data/current_user.txt"), "r") as file:
        current_user = file.read().strip()
    pd.read_csv(resource_path("data/feedback_data.csv"))

    data = pd.DataFrame({
        "username": [current_user],
        "star_ratings": [ratings],
        "feedback": [feedback],
    })

    data.to_csv(resource_path("data/feedback_data.csv"), index=False, mode="a", header=False)
    return True

def unfilled_star_button1_clicked():
    global ratings
    ratings = 1
    unfilled_star_button1.place_forget()
    filled_star_button1.place(
        x=289.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
def filled_star_button1_clicked():
    global ratings
    ratings = 0
    filled_star_button1.place_forget()
    filled_star_button2.place_forget()
    filled_star_button3.place_forget()
    filled_star_button4.place_forget()
    filled_star_button5.place_forget()
    unfilled_star_button1.place(
        x=289.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
    unfilled_star_button2.place(
        x=335.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
    unfilled_star_button3.place(
        x=382.0,
        y=176.0,
        width=39.0,
        height=41.0
    )
    unfilled_star_button4.place(
        x=427.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
    unfilled_star_button5.place(
        x=474.0,
        y=176.0,
        width=40.0,
        height=41.0
    )  
def unfilled_star_button2_clicked():
    global ratings
    ratings = 2
    unfilled_star_button2.place_forget()
    filled_star_button1.place(
        x=289.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
    filled_star_button2.place(
        x=335.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
def filled_star_button2_clicked():
    global ratings
    ratings = 1
    filled_star_button2.place_forget()
    filled_star_button3.place_forget()
    filled_star_button4.place_forget()
    filled_star_button5.place_forget()
    unfilled_star_button2.place(
        x=335.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
    unfilled_star_button3.place(
        x=382.0,
        y=176.0,
        width=39.0,
        height=41.0
    )
    unfilled_star_button4.place(
        x=427.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
    unfilled_star_button5.place(
        x=474.0,
        y=176.0,
        width=40.0,
        height=41.0
    )  
def unfilled_star_button3_clicked():
    global ratings
    ratings = 3
    unfilled_star_button3.place_forget()
    filled_star_button1.place(
        x=289.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
    filled_star_button2.place(
        x=335.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
    filled_star_button3.place(
        x=382.0,
        y=176.0,
        width=39.0,
        height=41.0
    )
def filled_star_button3_clicked():
    global ratings
    ratings = 2
    filled_star_button3.place_forget()
    filled_star_button4.place_forget()
    filled_star_button5.place_forget()
    unfilled_star_button3.place(
        x=382.0,
        y=176.0,
        width=39.0,
        height=41.0
    )
    unfilled_star_button4.place(
        x=427.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
    unfilled_star_button5.place(
        x=474.0,
        y=176.0,
        width=40.0,
        height=41.0
    )    
def unfilled_star_button4_clicked():
    global ratings
    ratings = 4
    unfilled_star_button4.place_forget()
    filled_star_button1.place(
        x=289.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
    filled_star_button2.place(
        x=335.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
    filled_star_button3.place(
        x=382.0,
        y=176.0,
        width=39.0,
        height=41.0
    )
    filled_star_button4.place(
        x=427.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
def filled_star_button4_clicked():
    global ratings
    ratings = 3
    filled_star_button4.place_forget()
    filled_star_button5.place_forget()
    unfilled_star_button4.place(
        x=427.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
    unfilled_star_button5.place(
        x=474.0,
        y=176.0,
        width=40.0,
        height=41.0
    )    
def unfilled_star_button5_clicked():
    global ratings
    ratings = 5
    unfilled_star_button5.place_forget()
    filled_star_button1.place(
        x=289.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
    filled_star_button2.place(
        x=335.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
    filled_star_button3.place(
        x=382.0,
        y=176.0,
        width=39.0,
        height=41.0
    )
    filled_star_button4.place(
        x=427.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
    filled_star_button5.place(
        x=474.0,
        y=176.0,
        width=40.0,
        height=41.0
    )
def filled_star_button5_clicked():
    global ratings
    ratings = 4
    filled_star_button5.place_forget()
    unfilled_star_button5.place(
        x=474.0,
        y=176.0,
        width=40.0,
        height=41.0
    )



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
    file=relative_to_assets(resource_path("forms/feedback_frame/image_1.png")))
image_1 = canvas.create_image(
    409.0,
    79.0,
    image=image_image_1
)

display_name_canvas = canvas.create_text(
    115.0,
    59.0,
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
    file=relative_to_assets(resource_path("forms/feedback_frame/button_1.png")))
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
    file=relative_to_assets(resource_path("forms/feedback_frame/image_2.png")))
image_2 = canvas.create_image(
    412.0,
    145.0,
    image=image_image_2
)

button_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/feedback_frame/button_2.png")))
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
    file=relative_to_assets(resource_path("forms/feedback_frame/button_3.png")))
submit_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=submit_button_clicked,
    relief="flat"
)
submit_button.place(
    x=659.0,
    y=421.0,
    width=112.89242553710938,
    height=39.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets(resource_path("forms/feedback_frame/image_3.png")))
image_3 = canvas.create_image(
    407.0,
    321.0,
    image=image_image_3
)


feedback_textbox = Text(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("Inter", 12 * -1)
)
feedback_textbox.place(
    x=80.0,
    y=275.0,
    width=655.0,
    height=101.0
)

# ------------------------------ star images ------------------------------
filled_star_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/feedback_frame/filled_star.png")))
unfilled_star_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/feedback_frame/unfilled_star.png")))

# ------------------------------ star buttons ------------------------------
unfilled_star_button1 = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=unfilled_star_image,
    borderwidth=0,
    highlightthickness=0,
    command=unfilled_star_button1_clicked,
    relief="flat"
)
unfilled_star_button1.place(
    x=289.0,
    y=176.0,
    width=40.0,
    height=41.0
)
filled_star_button1 = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=filled_star_image,
    borderwidth=0,
    highlightthickness=0,
    command=filled_star_button1_clicked,
    relief="flat"
)


unfilled_star_button2 = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=unfilled_star_image,
    borderwidth=0,
    highlightthickness=0,
    command=unfilled_star_button2_clicked,
    relief="flat"
)
unfilled_star_button2.place(
    x=335.0,
    y=176.0,
    width=40.0,
    height=41.0
)
filled_star_button2 = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=filled_star_image,
    borderwidth=0,
    highlightthickness=0,
    command=filled_star_button2_clicked,
    relief="flat"
)

unfilled_star_button3 = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=unfilled_star_image,
    borderwidth=0,
    highlightthickness=0,
    command=unfilled_star_button3_clicked,
    relief="flat"
)
unfilled_star_button3.place(
    x=382.0,
    y=176.0,
    width=39.0,
    height=41.0
)
filled_star_button3 = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=filled_star_image,
    borderwidth=0,
    highlightthickness=0,
    command=filled_star_button3_clicked,
    relief="flat"
)

unfilled_star_button4 = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=unfilled_star_image,
    borderwidth=0,
    highlightthickness=0,
    command=unfilled_star_button4_clicked,
    relief="flat"
)
unfilled_star_button4.place(
    x=427.0,
    y=176.0,
    width=40.0,
    height=41.0
)
filled_star_button4 = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=filled_star_image,
    borderwidth=0,
    highlightthickness=0,
    command=filled_star_button4_clicked,
    relief="flat"
)

unfilled_star_button5 = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=unfilled_star_image,
    borderwidth=0,
    highlightthickness=0,
    command=unfilled_star_button5_clicked,
    relief="flat"
)
unfilled_star_button5.place(
    x=474.0,
    y=176.0,
    width=40.0,
    height=41.0
)
filled_star_button5 = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=filled_star_image,
    borderwidth=0,
    highlightthickness=0,
    command=filled_star_button5_clicked,
    relief="flat"
)

change_profile_display()

window.resizable(False, False)
window.mainloop()
