from tkinter import *
from tkinter import messagebox
from pathlib import Path
import subprocess
from pathlib import Path
import pandas as pd
import os


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\signup1_resources\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def sign_up1_back_button_clicked():
    window.withdraw()
    subprocess.Popen(["python", "loginframe.py"])

def sign_up1_next_button_clicked():
    # make sure that the user has entered all the required information
    if first_name_signup.get() == "" or last_name_signup.get() == "" or user_name_signup.get() == "" or password_signup.get() == "":
        messagebox.showerror("Error", "Please fill in all the required information.")
        return

    submit_input()
    window.withdraw()
    subprocess.Popen(["python", "signupframe2.py"])

def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

def read_input():
    csv_file_path = "inputs/signup_input.csv"

    if os.path.exists(csv_file_path) and os.stat(csv_file_path).st_size > 0:
        df = pd.read_csv(csv_file_path)

        # get the first values from the dataframe
        first_name = df['first_name'].values[0]
        mid_name = df['mid_name'].values[0]
        last_name = df['last_name'].values[0]
        username = df['username'].values[0] 
        password = df['password'].values[0]

        # Insert values into GUI entry fields only if they are not null
        if pd.notna(first_name):
            first_name_signup.insert(0, first_name)
        if pd.notna(mid_name):
            middle_name_signup.insert(0, mid_name)
        if pd.notna(last_name):
            last_name_signup.insert(0, last_name)
        if pd.notna(username):
            user_name_signup.insert(0, username)
        if pd.notna(password):
            password_signup.insert(0, password)

def submit_input(): 
    csv_file_path = "inputs/signup_input.csv"
    df = pd.read_csv(csv_file_path)

    # get the first values from the dataframe
    confirm_pass = df['confirm_password'].values[0]
    email = df['email'].values[0]
    contact = df['contact_number'].values[0]

    # Get input from the user
    inputted_first_name = first_name_signup.get()
    inputted_mid_name = middle_name_signup.get()
    inputted_last_name = last_name_signup.get()
    inputted_username = user_name_signup.get()
    inputted_password = password_signup.get()

    df = pd.DataFrame({
        'first_name': [inputted_first_name],
        'mid_name': [inputted_mid_name],
        'last_name': [inputted_last_name],
        'username': [inputted_username],
        'password': [inputted_password],
        'confirm_password': [confirm_pass],
        'email': [email],
        'contact_number': [contact]
    })

    # save the dataframe as a csv file
    df.to_csv(csv_file_path, mode='w', index=False)


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
    190.0,
    250.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    183.0,
    237.0,
    image=image_image_2
)


entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    594.0,
    395.33442878723145,
    image=entry_image_1
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    594.0,
    320.66865730285645,
    image=entry_image_2
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    594.0,
    253.52588653564453,
    image=entry_image_3
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    594.0,
    186.0,
    image=entry_image_4
)

first_name_signup  = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    cursor="ibeam"
)
first_name_signup.place(
    x=419.0,
    y=106.0,
    width=353.0,
    height=34.0
)
first_name_signup.focus()

middle_name_signup = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
middle_name_signup.place(
    x=419.0,
    y=174.0,
    width=353.0,
    height=34.0
)

last_name_signup= Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
last_name_signup.place(
    x=419.0,
    y=241.0,
    width=353.0,
    height=34
)

user_name_signup  = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
user_name_signup.place(
    x=419.0,
    y=309.0,
    width=353.0,
    height=34
)

password_signup = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show='*'
)
password_signup.place(
    x=419.0,
    y=383.0,
    width=353.0,
    height=34
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    594.0,
    118.70454406738281,
    image=entry_image_5
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
next_button1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up1_next_button_clicked,
    relief="flat"
)
next_button1.place(
    x=665.0,
    y=441.0,
    width=112.89242553710938,
    height=39.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
back_button1 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up1_back_button_clicked,
    relief="flat"
)
back_button1.place(
    x=410.0,
    y=441.0,
    width=112.8924560546875,
    height=39.0
)

canvas.create_text(
    410.0,
    49.0,
    anchor="nw",
    text="Sign Up ",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

read_input()

window.resizable(False, False)
window.mainloop()
