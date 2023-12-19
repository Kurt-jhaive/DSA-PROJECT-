from tkinter import *
from tkinter import messagebox
import random
import subprocess
import pandas as pd
import os
import sys

from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\home_frame")


favorites = []
random_pet = ""

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

def register_button_clicked():
    window.destroy()
    subprocess.Popen(["registerframe/registerframe.exe"])

def donate_button_clicked():
    window.destroy()
    subprocess.Popen(["donateframe/donateframe.exe"])

def favorites_button_clicked():
    window.destroy()
    subprocess.Popen(["favoritesframe/favoritesframe.exe"])

def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

def change_pet():
    # change the image of the dog
    global random_pet
    if len(favorites) == len(pets):
        messagebox.showinfo("No more pets", "You have seen all the pets!")
        return
    else:
        random_pet = random.choice(list(pets.keys()))
        while random_pet in favorites:
            random_pet = random.choice(list(pets.keys()))
        

        name = pets[random_pet]["name"]
        picture = pets[random_pet]["picture"]
        description = pets[random_pet]["description"]
        quote = pets[random_pet]["quote"]

        canvas.itemconfigure(pet_name, text=name)
        canvas.itemconfigure(pet_pic, image=picture)
        canvas.itemconfigure(pet_desc, image=description)
        canvas.itemconfigure(pet_quote, image=quote)

        print(random_pet)   

def ekis_button_clicked():
    change_pet()


def add_to_favorites_button_clicked(dictionary):
    if random_pet in favorites:
        messagebox.showinfo("Already added", "This pet is already in your favorites!")
    else:
        favorites.append(random_pet)

        print("added to favorites", random_pet)
        print(favorites)

        with open(resource_path('data/favorites.txt'), 'w') as file:
            for item in favorites:
                file.write(item + '\n')

        change_pet()

def description_button_clicked(dictionary):
    full_desc = pets[random_pet]["full_desc"]   

    canvas.itemconfigure(pet_desc, state="hidden")
    canvas.itemconfigure(pet_quote, state="hidden")

    canvas.itemconfigure(pet_full_desc, image=full_desc, state="normal")
    close_description_button.place(
        x=718.0,
        y=122.0,
        width=46.0,
        height=46.0
    )

def close_description_button_clicked():
    canvas.itemconfigure(pet_full_desc, state="hidden")
    canvas.itemconfigure(pet_desc, state="normal")
    canvas.itemconfigure(pet_quote, state="normal")
 
    close_description_button.place_forget()


def check_list():
    # this function will update the favorites list
    with open(resource_path('data/favorites.txt'), 'r') as file:
        for line in file: 
            favorites.append(line.strip())

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

def adopt_button_clicked():
    # put the random_pet in the current_user's adopted list
    with open(resource_path("data/current_pet.txt"), "w") as file:
        file.write(random_pet + '\n')

    window.destroy()
    subprocess.Popen(["adoptframe1/adoptframe1.exe"])

def home_button_clicked():
    window.destroy()
    subprocess.Popen(["homeframe/homeframe.exe"])


def hamburger_menu_clicked():
    # show the hamburger menu
    canvas.itemconfigure(pink_menu_rectangle_canvas, state="normal")
    ekis_button.lower()
    add_to_favorites_button.lower()
    description_button.lower()
    close_description_button.lower()
    close_hamburger_menu.place(
        x=750.0,
        y=49.0,
        width=19.0,
        height=22.0
    )    
    account_settings.place(
        x=549.0,
        y=96.0,
        width=205.0,
        height=30.0
    )
    privacy_policy.place(
        x=550.0,
        y=133.0,
        width=203.99925231933594,
        height=32.0
    )
    terms_conditions.place(
        x=549.0,
        y=173.0,
        width=205.0,
        height=29.0
    )
    give_feedback.place(
        x=551.0,
        y=212.0,
        width=202.0,
        height=32.291259765625
    )
    log_out.place(
        x=550.0,
        y=256.0,
        width=204.0,
        height=31.0
    )

def close_hamburger_menu_clicked():
    # hide the hamburger menu
    canvas.itemconfigure(pink_menu_rectangle_canvas, state="hidden")
    ekis_button.lift()
    add_to_favorites_button.lift()
    description_button.lift()
    close_description_button.lift()
    account_settings.place_forget()
    privacy_policy.place_forget()
    terms_conditions.place_forget()
    give_feedback.place_forget()
    log_out.place_forget()
    close_hamburger_menu.place_forget()

def privacy_button_clicked():
    window.destroy()
    subprocess.Popen(["privacyframe1/privacyframe1.exe"])

def terms_button_clicked():
    window.destroy()
    subprocess.Popen(["termsframe1/termsframe1.exe"])

def feedback_button_clicked():
    window.destroy()
    subprocess.Popen(["feedbackframe/feedbackframe.exe"])

def log_out_button_clicked():
    window.destroy()
    subprocess.Popen(["purrfectmatch.exe"])


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
    file=relative_to_assets(resource_path("forms/home_frame/image_1.png")))
image_1 = canvas.create_image(
    544.0,
    309.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/image_2.png")))
image_2 = canvas.create_image(
    158.0,
    251.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/image_3.png")))
image_3 = canvas.create_image(
    372.0,
    72.0,
    image=image_image_3
)

button_image_3 = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/button_3.png")))
favorites_button= Button(
    bg="#FFFFFF",
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=favorites_button_clicked,
    relief="flat",
    activebackground="#FFFFFF",
)
favorites_button.place(
    x=715.0,
    y=48.0,
    width=27.0,
    height=23.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/button_4.png")))
menu_button = Button(
    bg="#FFFFFF",
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=hamburger_menu_clicked,
    relief="flat",
    activebackground="#FFFFFF",
)
menu_button.place(
    x=750.0,
    y=49.0,
    width=19.0,
    height=22.0
)

# second menu button to be displayed when the first menu button is clicked
close_hamburger_menu = Button(
    bg="#FFFFFF",
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=close_hamburger_menu_clicked,
    relief="flat",
    activebackground="#FFFFFF",
)


button_image_5 = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/button_5.png")))
filter_button = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("filter button clicked"),
    relief="flat"
)
filter_button.place(
    x=311.0,
    y=90.0,
    width=79.0,
    height=30.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/button_6.png")))
home_button = Button(
    bg="#F19FB5",
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    activebackground="#F19FB5",
    command=home_button_clicked,
)
home_button.place(
    x=95.0,
    y=155.0,
    width=120.0,
    height=30.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/button_7.png")))
register_button = Button(
    bg="#F19FB5",
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=register_button_clicked,
    relief="flat",
    activebackground="#F19FB5", 
)
register_button.place(
    x=95.0,
    y=204.0,
    width=120.0,
    height=30.0
)


button_image_8 = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/button_8.png")))
donate_button = Button(
    bg="#F19FB5",
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=donate_button_clicked,
    relief="flat",
    activebackground="#F19FB5",
)
donate_button.place(
    x=95.0,
    y=253.0,
    width=120.0,
    height=30.0
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

button_image_9 = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/button_9.png")))
button_9 = Button(
    bg="#F19FB5",
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat",
    activebackground="#F19FB5",
)
button_9.place(
    x=65.0,
    y=64.0,
    width=34.0,
    height=36.0
)

ekis_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/button_10.png")))
ekis_button = Button(
    bg="#FFFFFF",
    image=ekis_image,
    borderwidth=0,
    highlightthickness=0,
    command=ekis_button_clicked,
    relief="flat",
    activebackground="#FFFFFF",
)
ekis_button.place(
    x=621.0,
    y=123.0,
    width=42.0,
    height=43.0
)

pets = {
    "milo": {
        "name": "MILO, 1",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/milo/picture.png"))),
        "description": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/milo/description.png"))),
        "quote": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/milo/quote.png"))),
        "full_desc": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/milo/full_desc.png")))
    },
    "fiona": {
        "name": "FIONA, 3 1/2",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/fiona/picture.png"))),
        "description": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/fiona/description.png"))),
        "quote": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/fiona/quote.png"))),
        "full_desc": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/fiona/full_desc.png")))
    },
    "levis": {
        "name": "LEVIS, 2",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/levis/picture.png"))),
        "description": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/levis/description.png"))),
        "quote": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/levis/quote.png"))),
        "full_desc": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/levis/full_desc.png")))
    },
    "kaira": {
        "name": "KAIRA, 2",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/kaira/picture.png"))),
        "description": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/kaira/description.png"))),
        "quote": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/kaira/quote.png"))),
        "full_desc": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/kaira/full_desc.png")))
    },
    "pepper": {
        "name": "PEPPER, 3",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/pepper/picture.png"))),
        "description": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/pepper/description.png"))),
        "quote": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/pepper/quote.png"))),
        "full_desc": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/dogs/pepper/full_desc.png")))
    },   
    "candy": {
        "name": "CANDY, 2",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/candy/picture.png"))),   
        "description": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/candy/description.png"))),
        "quote": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/candy/quote.png"))),
        "full_desc": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/candy/full_desc.png"))),        
    },
    "lemon": {
        "name": "LEMON, 3",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/lemon/picture.png"))),
        "description": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/lemon/description.png"))),
        "quote": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/lemon/quote.png"))),
        "full_desc": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/lemon/full_desc.png"))),
    },
    "luna": {
        "name": "LUNA, 1",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/luna/picture.png"))),
        "description": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/luna/description.png"))),
        "quote": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/luna/quote.png"))),
        "full_desc": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/luna/full_desc.png"))),    
    },
    "orange": {
        "name": "ORANGE, 3",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/orange/picture.png"))),
        "description": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/orange/description.png"))),
        "quote": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/orange/quote.png"))),
        "full_desc": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/orange/full_desc.png"))),
    },
    "sugar": {
        "name": "SUGAR, 1",
        "picture": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/sugar/picture.png"))),
        "description": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/sugar/description.png"))),
        "quote": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/sugar/quote.png"))),
        "full_desc": PhotoImage(file=relative_to_assets(resource_path("forms/home_frame/cats/sugar/full_desc.png"))),
    },

}

pet_name  = canvas.create_text(
    582.0,
    176.0,
    anchor="nw",
    text="MILO, 1",
    fill="#000000",
    font=("Inter", 22 * -1, "bold")
)

pet_pic = canvas.create_image(
    448.0,
    307.0,
    image=pets["milo"]["picture"]
)

pet_desc = canvas.create_image(
    674.0,
    288.0,
    image=pets["milo"]["description"]
)

pet_quote = canvas.create_image(
    673.0,
    399.0,
    image=pets["milo"]["quote"]
)

pet_full_desc = canvas.create_image(
    664.0,
    309.0,
    image=pets["milo"]["full_desc"],
    state="hidden",
)


button_image_11 = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/button_11.png")))
add_to_favorites_button = Button(
    bg="#FFFFFF",
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_to_favorites_button_clicked(pets),
    relief="flat",
    activebackground="#FFFFFF",
)
add_to_favorites_button.place(
    x=669.0,
    y=123.0,
    width=43.0,
    height=44.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/button_12.png")))
description_button = Button(
    bg="#FFFFFF",
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: description_button_clicked(pets),
    relief="flat",
    activebackground="#FFFFFF",
)
description_button.place(
    x=718.0,
    y=122.0,
    width=46.0,
    height=46.0
)

close_description_button = Button(
    bg="#FFFFFF",
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=close_description_button_clicked,
    relief="flat",
    activebackground="#FFFFFF",
)

button_image_13 = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/button_13.png")))
adopt_button = Button(
    bg="#FFFFFF",
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=adopt_button_clicked,
    relief="flat",
    activebackground="#FFFFFF",
)
adopt_button.place(
    x=581.0,
    y=414.0,
    width=183.0,
    height=37.0
)

canvas.create_rectangle(
    215.0,
    151.99999378994107,
    229.83099189214408,
    187.3240229487419,
    fill="#F19FB5",
    outline="")

canvas.create_rectangle(
    215.0,
    203.99999378994107,
    229.83099189214408,
    239.3240229487419,
    fill="#F19FB5",
    outline="")

canvas.create_rectangle(
    216.0,
    253.99999378994107,
    230.83099189214408,
    289.3240229487419,
    fill="#F19FB5",
    outline="")


#----------------------- Hamburger Menu------------------
# HAMBURGER FRAME
pink_menu_rectangle_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/pink_menu.png")))
pink_menu_rectangle_canvas = canvas.create_image(
    654.0,
    194.0,
    image=pink_menu_rectangle_image,
    state="hidden",
)

account_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/account.png")))
account_settings = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=account_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("account_settings clicked"),
    relief="flat"
)
privacy_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/privacy.png")))
privacy_policy = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=privacy_image,
    borderwidth=0,
    highlightthickness=0,
    command=privacy_button_clicked,
    relief="flat"
)
terms_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/terms.png")))
terms_conditions = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=terms_image,
    borderwidth=0,
    highlightthickness=0,
    command=terms_button_clicked,
    relief="flat"
)
feedback_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/feedback.png")))
give_feedback = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=feedback_image,
    borderwidth=0,
    highlightthickness=0,
    command=feedback_button_clicked,
    relief="flat"
)
logout_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/home_frame/logout.png")))
log_out = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=logout_image,
    borderwidth=0,
    highlightthickness=0,
    command=log_out_button_clicked,
    relief="flat"
)

change_pet()
check_list()    
change_profile_display()

window.resizable(False, False)
window.mainloop()
