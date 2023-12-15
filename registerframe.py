from tkinter import *
from tkinter import messagebox, filedialog
import subprocess
import pandas as pd
import shutil
import os


from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\register_frame")

new_file_path = ''


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def home_button_clicked():
    window.destroy()
    subprocess.Popen(["python", "homeframe.py"])

def donate_button_clicked():
    window.destroy()
    subprocess.Popen(["python", "donateframe.py"])

def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

def upload_image_button_clicked():
    global new_file_path
    file_path = filedialog.askopenfilename()

    if file_path:
        # Create a new folder called "uploads" if it doesn't exist
        if not os.path.exists("uploads"):
            os.mkdir("uploads")
            os.system("cd uploads && mkdir register_application_images")

        # Get the filename of the selected image
        filename = os.path.basename(file_path)

        # Create a new path to store the image in the "uploads" folder
        new_file_path = os.path.join("uploads/register_application_images", filename)

        # Copy the image to the "uploads" folder
        shutil.copy(file_path, new_file_path)

        upload_label.configure(text=f"{filename}")


def submit_button_clicked(): 
    csv_file_path = 'data/register_data.csv'

    # check if all fields are filled up
    if not(petname_textbox.get() and breed_textbox.get() and age_textbox.get() and gender_textbox.get() and color_textbox.get() and size_textbox.get() and description_textbox.get("1.0", END).strip() and new_file_path):
        messagebox.showerror("Error", "Please fill up all fields and upload an image.")
    else:
        # Get input from the user
        inputted_pet_name = petname_textbox.get()
        inputted_breed = breed_textbox.get()
        inputted_age = age_textbox.get()
        inputted_gender = gender_textbox.get()
        inputted_color = color_textbox.get()
        inputted_size = size_textbox.get()
        inputted_description = description_textbox.get("1.0", END).strip()

        try:
            df = pd.read_csv(csv_file_path)
        except FileNotFoundError:
            # If the file doesn't exist, create a new DataFrame
            df = pd.DataFrame(columns=['pet_name', 'breed', 'age', 'gender', 'color', 'size', 'description', 'image_path'])

        # Create a new DataFrame with the inputted data
        new_data = pd.DataFrame({
            'pet_name': [inputted_pet_name],
            'breed': [inputted_breed],
            'age': [inputted_age],
            'gender': [inputted_gender],
            'color': [inputted_color],
            'size': [inputted_size],
            'description': [inputted_description],
            'image_path': [new_file_path]
        })

        # Append the new data to the existing DataFrame
        df = pd.concat([df, new_data], ignore_index=True)

        # Save the updated DataFrame to the CSV file
        df.to_csv(csv_file_path, index=False)

        # refresh the window after prompting a message
        messagebox.showinfo("Success", "Your registration of a pet has been submitted. Please wait for our team to contact you.")

def change_profile_display():
    #read the text file
    with open("data/current_user.txt", "r") as file:
        current_user = file.read().strip()
    
    #get the display name of the current user
    df = pd.read_csv('data/profile_data.csv')
    user_row = df[df['username'] == current_user]
    display_name = user_row['display_name'].values[0]
    display_location = user_row['address'].values[0]

    #change the display name and location
    canvas.itemconfigure(display_name_canvas, text=display_name)
    canvas.itemconfigure(profile_location, text=display_location)



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
    158.0,
    251.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    358.0,
    72.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
favorites_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("favorites_button clicked"),
    relief="flat"
)
favorites_button.place(
    x=713.0,
    y=42.0,
    width=31.0,
    height=34.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
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
    y=42.0,
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
    file=relative_to_assets("button_3.png"))
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
    file=relative_to_assets("button_4.png"))
register_button = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
register_button.place(
    x=95.0,
    y=204.0,
    width=120.0,
    height=30.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
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
    x=95.0,
    y=253.0,
    width=120.0,
    height=30.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=65.0,
    y=64.0,
    width=34.0,
    height=36.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    416.0,
    113.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    416.0,
    171.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    416.0,
    234.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    539.0,
    333.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    664.0,
    237.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    664.0,
    172.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    664.0,
    111.0,
    image=image_image_9
)

upload_button_img = PhotoImage(
    file=relative_to_assets("button_7.png"))
upload_image_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=upload_button_img,
    borderwidth=0,
    highlightthickness=0,
    command=upload_image_button_clicked,
    relief="flat"
)
upload_image_button.place(
    x=311.0,
    y=411.0,
    width=159.0,
    height=39.0
)

upload_label = Label(
    text="",   
    fg="#000716",
    bg="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)
upload_label.place(
    x=311.0,
    y=450.0,
    width=159.0,
    height=39.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
submit_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=submit_button_clicked,
    relief="flat"
)
submit_button.place(
    x=486.0,
    y=411.0,
    width=159.0,
    height=39.0
)
petname_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
petname_textbox .place(
    x=316.0,
    y=105.0,
    width=195.0,
    height=27
)
breed_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
breed_textbox.place(
    x=568.0,
    y=105.0,
    width=195.0,
    height=27
)
age_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
age_textbox.place(
    x=316.0,
    y=164.0,
    width=195.0,
    height=27
)
gender_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
gender_textbox.place(
    x=568.0,
    y=164.0,
    width=195.0,
    height=27
)
color_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
color_textbox.place(
    x=316.0,
    y=227.0,
    width=195.0,
    height=27
)
size_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
size_textbox.place(
    x=568.0,
    y=227.0,
    width=195.0,
    height=27
)
description_textbox = Text(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
description_textbox.place(
    x=316.0,
    y=295.0,
    width=447.0,
    height=91
)

change_profile_display()

window.resizable(False, False)
window.mainloop()
