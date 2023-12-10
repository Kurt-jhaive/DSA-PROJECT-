from tkinter import *
from tkinter import messagebox
from pathlib import Path
import subprocess
import pandas as pd
import os


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\signup2_resources\assets\frame0")

df = pd.read_csv("inputs/signup_input.csv")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def signupform2_signup_button():
    # make sure that the user has entered all the required information
    if confirm_password.get() == "" or email_address.get() == "" or contact_number.get() == "":
        messagebox.showerror("Error", "Please fill in all the required information.")
        return

    save_input()
    submit_input()
    window.withdraw()

    # open the signupframe3.py and pass the stored values as arguments
    subprocess.Popen(["python", "signupframe3.py"])

def signupform2_back_button():
    save_input()
    window.withdraw()
    # open the signupframe2.py without passing any arguments
    subprocess.Popen(["python", "signupframe1.py"])
    
def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        reset_input()
        window.destroy()

def read_input():
    csv_file_path = "inputs/signup_input.csv"

    if os.path.exists(csv_file_path) and os.stat(csv_file_path).st_size > 0:
        df = pd.read_csv(csv_file_path)

        # get the first values from the dataframe
        confirm_pass = df['confirm_password'].values[0]
        email = df['email'].values[0]
        contact = df['contact_number'].values[0]

        if pd.notna(confirm_pass):
            confirm_password.insert(0, confirm_pass)
        if pd.notna(email):
            email_address.insert(0, email)
        if pd.notna(contact):
            contact_number.insert(0, contact)

def save_input():
    global df
    csv_file_path = "inputs/signup_input.csv"

    df = pd.read_csv(csv_file_path)

    # get the first values from the dataframe
    first_name = df['first_name'].values[0]
    mid_name = df['mid_name'].values[0]
    last_name = df['last_name'].values[0]
    username = df['username'].values[0]
    password = df['password'].values[0]

    # Get input from the user
    inputted_confirm_password = confirm_password.get()
    inputted_email = email_address.get()
    inputted_contact_number = contact_number.get()

    df = pd.DataFrame({
        'first_name': [first_name],
        'mid_name': [mid_name],
        'last_name': [last_name],
        'username': [username],
        'password': [password],
        'confirm_password': [inputted_confirm_password],
        'email': [inputted_email],
        'contact_number': [inputted_contact_number],
    })

    # save the dataframe as a csv file
    df.to_csv(csv_file_path, mode='w', index=False)

def submit_input():
        # save the dataframe to the profile_data.csv file
    df.to_csv("data/profile_data.csv", mode='a', index=False, header=False)

def reset_input():
    csv_file_path = "inputs/signup_input.csv"

    # Read the CSV file to get the column names and data types
    df_default = pd.read_csv(csv_file_path, nrows=0)

    # Create a DataFrame for the default values with the same column names and data types
    df_default = pd.DataFrame({
        'first_name': [""],
        'mid_name': [""],
        'last_name': [""],
        'username': [""],
        'password': [""],
        'confirm_password': [""],
        'email': [""],
        'contact_number': [""],
    }, columns=df_default.columns)

    # Save the DataFrame as a CSV file
    df_default.to_csv(csv_file_path, mode='w', index=False)

    

    
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

canvas.create_text(
    410.0,
    42.0,
    anchor="nw",
    text="Sign Up ",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    594.0,
    122.410400390625,
    image=entry_image_1
)
confirm_password = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show='*'
)
confirm_password.place(
    x=415.0,
    y=111.0,
    width=356.0,
    height=32
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    594.0,
    191.41039276123047,
    image=entry_image_2
)
email_address = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
email_address.place(
    x=415.0,
    y=179.0,
    width=356.0,
    height=32
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    594.0,
    259.69991302490234,
    image=entry_image_3
)
contact_number = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
contact_number.place(
    x=415.0,
    y=250.0,
    width=356.0,
    height=32
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
terms_and_conditions = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
terms_and_conditions.place(
    x=443.0,
    y=391.0,
    width=301.0,
    height=61.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
signupframe2_signup_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=signupform2_signup_button,
    relief="flat"
) 
signupframe2_signup_button.place(
    x=619.0,
    y=309.0,
    width=159.0,
    height=38.57142639160156
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
signupframe2_back_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=signupform2_back_button,
    relief="flat"
)
signupframe2_back_button.place(
    x=410.0,
    y=309.0,
    width=112.8924560546875,
    height=39.0
)

read_input()
window.resizable(False, False)
window.mainloop()
