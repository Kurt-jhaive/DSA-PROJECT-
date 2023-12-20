from tkinter import *
from tkinter import messagebox
import tkinter as tk
import subprocess
import pandas as pd
import os
import sys

from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\favorites1_frame")

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
def home_button_clicked():
    window.destroy()
    subprocess.Popen(["homeframe/homeframe.exe"])

def register_button_clicked():
    window.destroy()
    subprocess.Popen(["registerframe/registerframe.exe"])

def donate_button_clicked():
    window.destroy()
    subprocess.Popen(["donateframe/donateframe.exe"])

def favorites_button_clicked():
    window.destroy()
    subprocess.Popen(["favorites1frame/favorites1frame.exe"])

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


def display_favorite_pet():
    # read the whole text file of the favorites
    with open(resource_path("../../_internal/data/temp_favorites.txt"), "r") as file:
        total_favorites = file.readlines()

    # if there are more than 3 favorites, show the next button
    if len(total_favorites) > 3:
        next_button.place(  
            x=656.0,
            y=405.0,
            width=112.89242553710938,
            height=39.0
        )
    if len(total_favorites) < 3:
        next_button.place_forget()

    # read the text file of the favorites and get the first 3 pets if there are 3 pets and below
    with open(resource_path("../../_internal/data/temp_favorites.txt"), "r") as file:
        if len(total_favorites) == 0:
            favorites = []
            messagebox.showinfo("No Favorites", "You have no favorites yet.")
        if len(total_favorites) == 1:
            favorites = [file.readline().strip() for _ in range(1)]
        elif len(total_favorites) == 2:
            favorites = [file.readline().strip() for _ in range(2)]
        elif len(total_favorites) > 2:
            favorites = [file.readline().strip() for _ in range(3)]

    if len(favorites) == 1:
        # show only the first pet
        first_pet = favorites[0].split(",")[0]
        name = pets[first_pet]["name"]
        breed = pets[first_pet]["breed"]
        age = pets[first_pet]["age"]
        picture = pets[first_pet]["picture"]
        gender = pets[first_pet]["gender"]

        canvas.itemconfigure(rectangle_1, state="normal")
        canvas.itemconfigure(pet1_name_canvas, text=f"{name}, {gender}", state="normal")
        canvas.itemconfigure(pet1_breed_canvas, text=breed, state="normal")
        canvas.itemconfigure(pet1_age_canvas, text=age, state="normal")
        canvas.itemconfigure(pet1_pic_canvas, image=picture, state="normal")
        adopt_button1.place(
            x=578.0,
            y=131.0,
            width=183.0,
            height=37.0
        )
        # hide the second and third pet
        canvas.itemconfigure(rectangle_2, state="hidden")
        canvas.itemconfigure(rectangle_3, state="hidden")
        canvas.itemconfigure(pet2_name_canvas, state="hidden")
        canvas.itemconfigure(pet2_breed_canvas, state="hidden")
        canvas.itemconfigure(pet2_age_canvas, state="hidden")
        canvas.itemconfigure(pet2_pic_canvas, state="hidden")
        canvas.itemconfigure(pet3_name_canvas, state="hidden")
        canvas.itemconfigure(pet3_breed_canvas, state="hidden")
        canvas.itemconfigure(pet3_age_canvas, state="hidden")
        canvas.itemconfigure(pet3_pic_canvas, state="hidden")
        adopt_button2.place_forget()
        adopt_button3.place_forget()
    elif len(favorites) == 2:
        # show the first pet and the second pet
        first_pet = favorites[0].split(",")[0]
        name = pets[first_pet]["name"]
        breed = pets[first_pet]["breed"]
        age = pets[first_pet]["age"]
        picture = pets[first_pet]["picture"]
        gender = pets[first_pet]["gender"]

        canvas.itemconfigure(rectangle_1, state="normal")
        canvas.itemconfigure(pet1_name_canvas, text=f"{name}, {gender}", state="normal")
        canvas.itemconfigure(pet1_breed_canvas, text=breed, state="normal")
        canvas.itemconfigure(pet1_age_canvas, text=age, state="normal")
        canvas.itemconfigure(pet1_pic_canvas, image=picture, state="normal")
        adopt_button1.place(
            x=578.0,
            y=131.0,
            width=183.0,
            height=37.0
        )

        second_pet = favorites[1].split(",")[0]
        name = pets[second_pet]["name"]
        breed = pets[second_pet]["breed"]
        age = pets[second_pet]["age"]
        picture = pets[second_pet]["picture"]
        gender = pets[second_pet]["gender"]

        canvas.itemconfigure(rectangle_1, state="normal")
        canvas.itemconfigure(rectangle_2, state="normal")
        canvas.itemconfigure(pet2_name_canvas, text=f"{name}, {gender}", state="normal")
        canvas.itemconfigure(pet2_breed_canvas, text=breed, state="normal")
        canvas.itemconfigure(pet2_age_canvas, text=age, state="normal")
        canvas.itemconfigure(pet2_pic_canvas, image=picture, state="normal")
        adopt_button2.place(
            x=578.0,
            y=225.0,
            width=183.0,
            height=37.0
        )

        # hide the third pet
        canvas.itemconfigure(rectangle_3, state="hidden")
        canvas.itemconfigure(pet3_name_canvas, state="hidden")
        canvas.itemconfigure(pet3_breed_canvas, state="hidden")
        canvas.itemconfigure(pet3_age_canvas, state="hidden")
        canvas.itemconfigure(pet3_pic_canvas, state="hidden")
        adopt_button3.place_forget()
    elif len(favorites) == 3:
        # show the first pet, second pet, and third pet
        first_pet = favorites[0].split(",")[0]
        name = pets[first_pet]["name"]
        breed = pets[first_pet]["breed"]
        age = pets[first_pet]["age"]
        picture = pets[first_pet]["picture"]
        gender = pets[first_pet]["gender"]

        canvas.itemconfigure(rectangle_1, state="normal")
        canvas.itemconfigure(pet1_name_canvas, text=f"{name}, {gender}", state="normal")
        canvas.itemconfigure(pet1_breed_canvas, text=breed, state="normal")
        canvas.itemconfigure(pet1_age_canvas, text=age, state="normal")
        canvas.itemconfigure(pet1_pic_canvas, image=picture, state="normal")
        adopt_button1.place(
            x=578.0,
            y=131.0,
            width=183.0,
            height=37.0
        )

        second_pet = favorites[1].split(",")[0]
        name = pets[second_pet]["name"]
        breed = pets[second_pet]["breed"]
        age = pets[second_pet]["age"]
        picture = pets[second_pet]["picture"]
        gender = pets[second_pet]["gender"]

        canvas.itemconfigure(rectangle_1, state="normal")
        canvas.itemconfigure(rectangle_2, state="normal")
        canvas.itemconfigure(pet2_name_canvas, text=f"{name}, {gender}", state="normal")
        canvas.itemconfigure(pet2_breed_canvas, text=breed, state="normal")
        canvas.itemconfigure(pet2_age_canvas, text=age, state="normal")
        canvas.itemconfigure(pet2_pic_canvas, image=picture, state="normal")
        adopt_button2.place(
            x=578.0,
            y=225.0,
            width=183.0,
            height=37.0
        )

        third_pet = favorites[2].split(",")[0]
        name = pets[third_pet]["name"]
        breed = pets[third_pet]["breed"]
        age = pets[third_pet]["age"]
        picture = pets[third_pet]["picture"]
        gender = pets[third_pet]["gender"]

        canvas.itemconfigure(rectangle_1, state="normal")
        canvas.itemconfigure(rectangle_2, state="normal")
        canvas.itemconfigure(rectangle_3, state="normal")
        canvas.itemconfigure(pet3_name_canvas, text=f"{name}, {gender}", state="normal")
        canvas.itemconfigure(pet3_breed_canvas, text=breed, state="normal")
        canvas.itemconfigure(pet3_age_canvas, text=age, state="normal")
        canvas.itemconfigure(pet3_pic_canvas, image=picture, state="normal")
        adopt_button3.place(
            x=578.0,
            y=316.0,
            width=183.0,
            height=37.0
        )

def delete_favorites():
    with open(resource_path("../../_internal/data/temp_favorites.txt"), "r") as file:
        lines = file.readlines()

    new_lines = lines[3:]

    with open(resource_path("../../_internal/data/temp_favorites.txt"), "w") as file:
        file.writelines(new_lines)

def next_button_clicked():   
    delete_favorites()
    display_favorite_pet()

def copy_favorites_data():
    with open(resource_path("../../_internal/data/favorites.txt"), "r") as file:
        lines = file.readlines()
    with open(resource_path("../../_internal/data/temp_favorites.txt"), "w") as file:
        file.writelines(lines)
        

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
    file=relative_to_assets(resource_path("forms/favorites1_frame/image_1.png")))
image_1 = canvas.create_image(
    158.0,
    251.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/favorites1_frame/image_2.png")))
image_2 = canvas.create_image(
    369.0,
    72.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets(resource_path("forms/favorites1_frame/button_1.png")))
favorites_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=favorites_button_clicked,
    relief="flat"
)
favorites_button.place(
    x=705.0,
    y=46.0,
    width=37.0,
    height=35.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/favorites1_frame/button_2.png")))
menu_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("menu_button clicked"),
    relief="flat"
)
menu_button.place(
    x=749.0,
    y=45.0,
    width=23.0,
    height=35.0
)

display_name_canvas = canvas.create_text(
    105.0,
    66.0,
    anchor="nw",
    text="Marie Cris Edusma",
    fill="#FFFFFF",
    font=("Inter SemiBold", 14 * -1, "bold")
)

profile_location = canvas.create_text(
    105.0,
    82.0,
    anchor="nw",
    text="Taguig City",
    fill="#FFFFFF",
    font=("Inter SemiBold", 11 * -1, "bold")
)

button_image_3 = PhotoImage(
    file=relative_to_assets(resource_path("forms/favorites1_frame/button_3.png")))
home_button = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=home_button_clicked,
    relief="flat"
)
home_button.place(
    x=95.0,
    y=155.0,
    width=120.0,
    height=30.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets(resource_path("forms/favorites1_frame/button_4.png")))
register_button = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=register_button_clicked,
    relief="flat"
)
register_button.place(
    x=92.0,
    y=204.0,
    width=127.0,
    height=30.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets(resource_path("forms/favorites1_frame/button_5.png")))
donate_button = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=donate_button_clicked,
    relief="flat"
)
donate_button.place(
    x=93.0,
    y=253.0,
    width=127.0,
    height=30.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets(resource_path("forms/favorites1_frame/button_6.png")))
user_button = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("user_button clicked"),
    relief="flat"
)
user_button.place(
    x=65.0,
    y=64.0,
    width=34.0,
    height=36.0
)

pets = {
    "milo": {
        "name": "MILO",
        "gender": "Male",
        "breed": "Aspin",
        "age": "2 year old",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/favorites1_frame/milo.png"))),
    },
    "fiona": {
        "name": "FIONA",
        "gender": "Female",
        "breed": "Aspin",
        "age": "3½ year old",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/favorites1_frame/fiona.png"))),
    },
    "levis": {
        "name": "LEVIS",
        "gender": "Female",
        "breed": "Aspin",
        "age": "4 year old",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/favorites1_frame/levis.png"))),
    },
    "kaira": {
        "name": "KAIRA",
        "gender": "Female",
        "breed": "Aspin-Mixed",
        "age": "2 year old",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/favorites1_frame/kaira.png"))),
    },
    "pepper": {
        "name": "PEPPER",
        "gender": "Female",
        "breed": "Aspin-Border Collie Mix",
        "age": "3 year old",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/favorites1_frame/pepper.png"))),
    },   
    "candy": {
        "name": "CANDY",
        "gender": "Female",
        "breed": "Puspin",
        "age": "2 year old",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/favorites1_frame/candy.png"))),       
    },
    "lemon": {
        "name": "LEMON",
        "gender": "Male",
        "breed": "Domestic Shorthair",
        "age": "3 year old",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/favorites1_frame/lemon.png"))),
    },
    "luna": {
        "name": "LUNA",
        "gender": "Male",
        "breed": "Persian Siamese",
        "age": "1 year old",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/favorites1_frame/luna.png"))), 
    },
    "orange": {
        "name": "ORANGE",
        "gender": "Female",
        "breed": "Puspin",
        "age": "3 year old",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/favorites1_frame/orange.png"))),
    },
    "sugar": {
        "name": "SUGAR",
        "gender": "Female",
        "breed": "Puspin",
        "age": "1 year old",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/favorites1_frame/sugar.png"))),
    },
}

pink_rectangle = PhotoImage(
    file=relative_to_assets(resource_path("forms/favorites1_frame/pink_rectangle.png")))
rectangle_1 = canvas.create_image(
    540.0,
    147.0,
    image=pink_rectangle,
    state="hidden"
)
rectangle_2 = canvas.create_image(
    540.0,
    242.0,
    image=pink_rectangle,
    state="hidden"
)
rectangle_3 = canvas.create_image(
    540.0,
    335.0,
    image=pink_rectangle,
    state="hidden"
)

adopt_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/favorites1_frame/adopt_me.png")))
adopt_button1 = Button(
    bg="#F8CBD7",
    activebackground="#F8CBD7",
    image=adopt_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("adopt_button1 clicked"),
    relief="flat"
)
adopt_button2 = Button(
    bg="#F8CBD7",
    activebackground="#F8CBD7",
    image=adopt_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("adopt_button2 clicked"),
    relief="flat"
)
adopt_button3 = Button(
    bg="#F8CBD7",
    activebackground="#F8CBD7",
    image=adopt_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("adopt_button3 clicked"),
    relief="flat"
)

pet1_name_canvas = canvas.create_text(
    393.0,
    122.0,
    anchor="nw",
    text="MILO, Male",
    fill="#AD206C",
    font=("Inter Bold", 16 * -1),
    state="hidden"
)
pet1_breed_canvas = canvas.create_text(
    393.0,
    138.0,
    anchor="nw",
    text="Aspin \n",
    fill="#000000",
    font=("Inter Bold", 16 * -1),
    state="hidden"
)
pet1_age_canvas = canvas.create_text(
    393.0,
    156.0,
    anchor="nw",
    text="2 year old",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1),
    state="hidden"
)

pet2_name_canvas = canvas.create_text(
    393.0,
    215.0,
    anchor="nw",
    text="FIONA, Female",
    fill="#AD206C",
    font=("Inter Bold", 16 * -1),
    state="hidden"
)
pet2_breed_canvas = canvas.create_text(
    393.0,
    229.0,
    anchor="nw",
    text="Aspin \n",
    fill="#000000",
    font=("Inter Bold", 16 * -1),
    state="hidden"
)
pet2_age_canvas = canvas.create_text(
    393.0,
    248.0,
    anchor="nw",
    text=" 3½ year old ",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1),
    state="hidden"
)

pet3_name_canvas = canvas.create_text(
    393.0,
    307.0,
    anchor="nw",
    text="LEVIS, Female",
    fill="#AD206C",
    font=("Inter Bold", 16 * -1),
    state="hidden"
)
pet3_breed_canvas = canvas.create_text(
    393.0,
    323.0,
    anchor="nw",
    text="Aspin \n",
    fill="#000000",
    font=("Inter Bold", 16 * -1),
    state="hidden"
)
pet3_age_canvas = canvas.create_text(
    393.0,
    341.0,
    anchor="nw",
    text="4 year old",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1),
    state="hidden"
)

pet1_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/favorites1_frame/milo.png")))
pet1_pic_canvas = canvas.create_image(
    350.0,
    146.0,
    image=pet1_image,
    state="hidden"
)
pet2_pic_canvas = canvas.create_image(
    350.0,
    242.0,
    image=pet1_image,
    state="hidden"
)
pet3_pic_canvas = canvas.create_image(
    350.0,
    335.0,
    image=pet1_image,
    state="hidden"
)

button_image_10 = PhotoImage(
    file=relative_to_assets(resource_path("forms/favorites1_frame/button_10.png")))
next_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=next_button_clicked,
    relief="flat"
)


copy_favorites_data()
change_profile_display()
display_favorite_pet()

window.resizable(False, False)
window.mainloop()
