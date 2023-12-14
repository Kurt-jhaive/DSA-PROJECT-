from tkinter import *
from tkinter import messagebox
import subprocess
import pandas as pd

from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\signup1_frame")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def back_button_1_clicked():
    window.withdraw()
    # open the signupframe2.py
    subprocess.Popen(["python", "signupframe.py"])

def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

def save_input():
    # Get input from the user
    inputted_name = name_textbox.get()
    inputted_address = address_textbox.get()

    # get the data in the text file
    with open('data/signup_data.txt', 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
    
    print(data)
    #save to csv
    csv_file_path = 'data/profile_data.csv'

    df = pd.DataFrame({
        'first_name': [data[0]],
        'middle_name': [data[1]],
        'last_name': [data[2]],
        'username': [data[3]],
        'password': [data[4]],
        'confirm_password': [data[5]],
        'email': [data[6]],
        'contact_number': [data[7]],
        'display_name': [inputted_name],
        'address': [inputted_address]
    })

    # append the dataframe
    df.to_csv(csv_file_path, mode='a', index=False, header=False)

def continue_button_1_clicked():
    canvas.itemconfigure(name_canvas, state="hidden")
    canvas.itemconfigure(text1, state="hidden")
    canvas.itemconfigure(text2, state="hidden")
    canvas.itemconfigure(text3, state="hidden")
    loading_button.place_forget()
    name_textbox.place_forget()
    continue_button_1.place_forget()

    #show next 
    canvas.itemconfigure(rectangle1, state="normal")
    canvas.itemconfigure(rectangle2, state="normal")
    canvas.itemconfigure(adress_text1, state="normal")
    canvas.itemconfigure(adress_text2, state="normal")
    canvas.itemconfigure(adress_text3, state="normal")
    canvas.itemconfigure(address_canvas, state="normal")
    address_textbox.place(
        x=182.0,
        y=289.0,
        width=457.0,
        height=29.0
    )
    continue_button_2.place(
        x=343.0,
        y=387.0,
        width=159.0,
        height=39.0
    )
    back_button_2.place(
        x=137.0,
        y=111.0,
        width=9.62713623046875,
        height=16.5064697265625
    )

def continue_button_2_clicked():
    canvas.itemconfigure(rectangle1, state="hidden")
    canvas.itemconfigure(rectangle2, state="hidden")
    canvas.itemconfigure(adress_text1, state="hidden")
    canvas.itemconfigure(adress_text2, state="hidden")
    canvas.itemconfigure(adress_text3, state="hidden")
    canvas.itemconfigure(address_canvas, state="hidden")
    address_textbox.place_forget()
    continue_button_2.place_forget()
    
    #show next
    canvas.itemconfigure(last_text_1, state="normal")
    canvas.itemconfigure(last_text_2, state="normal")
    loading_line_button_full.place(
        x=259.5927734375,
        y=119.0,
        width=324.4072265625,
        height=7.0
    )
    yes_button.place(
        x=327.0,
        y=355.0,
        width=159.0,
        height=39.0
    )
    back_button_3.place(
        x=137.0,
        y=111.0,
        width=9.62713623046875,
        height=16.5064697265625
    )

def back_button_2_clicked():
    canvas.itemconfigure(rectangle1, state="hidden")
    canvas.itemconfigure(rectangle2, state="hidden")
    canvas.itemconfigure(adress_text1, state="hidden")
    canvas.itemconfigure(adress_text2, state="hidden")
    canvas.itemconfigure(adress_text3, state="hidden")
    canvas.itemconfigure(address_canvas, state="hidden")
    address_textbox.place_forget()
    continue_button_2.place_forget()
    back_button_2.place_forget()

    #show previous
    canvas.itemconfigure(name_canvas, state="normal")
    canvas.itemconfigure(text1, state="normal")
    canvas.itemconfigure(text2, state="normal")
    canvas.itemconfigure(text3, state="normal")
    loading_button.place(
        x=259.5927734375,
        y=119.0,
        width=324.174560546875,
        height=7.0
    )
    name_textbox.place(
        x=202.0,
        y=280.0,
        width=457.0,
        height=29.0
    )
    continue_button_1.place(
        x=343.0,
        y=387.0,
        width=159.0,
        height=39.0
    )
    back_button_1.place(
        x=137.0,
        y=111.0,
        width=9.62713623046875,
        height=16.506439208984375
    )

def back_button_3_clicked():
    canvas.itemconfigure(last_text_1, state="hidden")
    canvas.itemconfigure(last_text_2, state="hidden")
    loading_line_button_full.place_forget()
    yes_button.place_forget()
    back_button_3.place_forget()

    #show previous
    canvas.itemconfigure(rectangle1, state="normal")
    canvas.itemconfigure(rectangle2, state="normal")
    canvas.itemconfigure(adress_text1, state="normal")
    canvas.itemconfigure(adress_text2, state="normal")
    canvas.itemconfigure(adress_text3, state="normal")
    canvas.itemconfigure(address_canvas, state="normal")
    address_textbox.place(
        x=182.0,
        y=289.0,
        width=457.0,
        height=29.0
    )
    continue_button_2.place(
        x=343.0,
        y=387.0,
        width=159.0,
        height=39.0
    )
    back_button_2.place(
        x=137.0,
        y=111.0,
        width=9.62713623046875,
        height=16.5064697265625
    )

def yes_button_clicked():
    save_input()
    window.withdraw()
    subprocess.Popen(["python", "loginframe.py"])


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

purrfect_image = PhotoImage(
    file=relative_to_assets("purrfectmatch.png"))
title_canvas = canvas.create_image(
    404.0,
    98.0,
    image=purrfect_image
)

loading_image = PhotoImage(
    file=relative_to_assets("loading_line.png"))
loading_button = Button(
    image=loading_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("loading_button clicked"),
    relief="flat"
)
loading_button.place(
    x=259.5927734375,
    y=119.0,
    width=324.174560546875,
    height=7.0
)

text1 = canvas.create_text(
    273.0,
    231.0,
    anchor="nw",
    text="What purrfect name do you prefer to go by?",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

text2 = canvas.create_text(
    275.0,
    338.0,
    anchor="nw",
    text="This is how your name will appear in the PurffectMatch",
    fill="#7C7C7C",
    font=("Inter", 12 * -1)
)

text3 = canvas.create_text(
    205.0,
    186.0,
    anchor="nw",
    text="HEY THERE, FUTURE PURR PARENTS!",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

name_image = PhotoImage(
    file=relative_to_assets("name.png"))
name_canvas = canvas.create_image(
    431.0,
    294.0,
    image=name_image
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

back_image = PhotoImage(
    file=relative_to_assets("back.png"))
back_button_1 = Button(
    bg="#FFFFFF",
    image=back_image,
    borderwidth=0,
    highlightthickness=0,
    command=back_button_1_clicked,
    relief="flat",
    activebackground="#FFFFFF",
)
back_button_1.place(
    x=137.0,
    y=111.0,
    width=9.62713623046875,
    height=16.506439208984375
)

continue_image = PhotoImage(
    file=relative_to_assets("continue.png"))
continue_button_1 = Button(
    image=continue_image,
    borderwidth=0,
    highlightthickness=0,
    command=continue_button_1_clicked,
    relief="flat"
)
continue_button_1.place(
    x=343.0,
    y=387.0,
    width=159.0,
    height=39.0
)


# # ------------next page ----------------
rectangle1 = canvas.create_rectangle(
    259.5927734375,
    119.0,
    583.767333984375,
    126.0,
    fill="#D9D9D9",
    outline="",
    state="hidden",
)

rectangle2 = canvas.create_rectangle(
    259.5927734375,
    119.0,
    480.36370849609375,
    126.0,
    fill="#F19FB5",
    outline="",
    state="hidden",
)

adress_text1 = canvas.create_text(
    319.0,
    235.0,
    anchor="nw",
    text="Please enter your address?",
    fill="#000000",
    font=("Inter Bold", 16 * -1),
    state="hidden"
)

adress_text2 = canvas.create_text(
    265.0,
    339.0,
    anchor="nw",
    text="This is how your address will appear in the PurffectMatch",
    fill="#969696",
    font=("Inter", 12 * -1),
    state="hidden"
)

adress_text3 = canvas.create_text(
    330.0,
    195.0,
    anchor="nw",
    text="MEOW, MARIE!",
    fill="#000000",
    font=("Inter Bold", 24 * -1),
    state="hidden"
)

address_image = PhotoImage(
    file=relative_to_assets("address.png"))
address_canvas = canvas.create_image(
    410.0,
    303.0,
    image=address_image,
    state="hidden"
)
address_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)

continue_button_2 = Button(
    image=continue_image,
    borderwidth=0,
    highlightthickness=0,
    command=continue_button_2_clicked,
    relief="flat"
)

back_button_2 = Button(
    bg="#FFFFFF",
    image=back_image,
    borderwidth=0,
    highlightthickness=0,
    command=back_button_2_clicked,
    relief="flat",
    activebackground="#FFFFFF",
)

# ------------last page ----------------
loading_image_last = PhotoImage(
    file=relative_to_assets("loading_line_full.png"))
loading_line_button_full = Button(
    image=loading_image_last,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("loading_line_button_full clicked"),
    relief="flat"
)

last_text_1 = canvas.create_text(
    331.0,
    222.0,
    anchor="nw",
    text="MEOW! ARF!",
    fill="#000000",
    font=("Inter Bold", 24 * -1),
    state="hidden"
)

last_text_2 = canvas.create_text(
    265.0,
    267.0,
    anchor="nw",
    text="Are you excited to find your perfect match?",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1),
    state="hidden"
)

back_button_3 = Button(
    bg="#FFFFFF",
    image=back_image,
    borderwidth=0,
    highlightthickness=0,
    command=back_button_3_clicked,
    relief="flat",
    activebackground="#FFFFFF",
)

yes_image = PhotoImage(
    file=relative_to_assets("yes.png"))
yes_button = Button(
    image=yes_image,
    borderwidth=0,
    highlightthickness=0,
    command= yes_button_clicked,
    relief="flat"
)

window.resizable(False, False)
window.mainloop()
