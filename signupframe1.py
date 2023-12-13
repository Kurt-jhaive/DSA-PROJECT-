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

def back_button1_clicked():
    window.withdraw()
    subprocess.Popen(["python", "loginframe.py"])


def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

# def sign_up1_next_button_clicked():
#     # make sure that the user has entered all the required information
#     if first_name_signup.get() == "" or last_name_signup.get() == "" or user_name_signup.get() == "" or password_signup.get() == "":
#         messagebox.showerror("Error", "Please fill in all the required information.")
#         return

#     submit_input()
#     window.withdraw()
#     subprocess.Popen(["python", "signupframe2.py"])

# def read_input():
#     csv_file_path = "inputs/signup_input.csv"

#     df = pd.read_csv(csv_file_path)

#     # get the first values from the dataframe
#     first_name = df['first_name'].values[-1]
#     mid_name = df['mid_name'].values[-1]
#     last_name = df['last_name'].values[-1]
#     username = df['username'].values[-1] 
#     password = df['password'].values[-1]

#     # Insert values into GUI entry fields only if they are not null
#     if pd.notna(first_name):
#         first_name_signup.insert(0, first_name)
#     if pd.notna(mid_name):
#         middle_name_signup.insert(0, mid_name)
#     if pd.notna(last_name):
#         last_name_signup.insert(0, last_name)
#     if pd.notna(username):
#         user_name_signup.insert(0, username)
#     if pd.notna(password):
#         password_signup.insert(0, password)


# def submit_input(): 
#     csv_file_path = "inputs/signup_input.csv"
#     # df = pd.read_csv(csv_file_path)

#     # # get the first values from the dataframe
#     # confirm_pass = df['confirm_password'].values[0]
#     # email = df['email'].values[0]
#     # contact = df['contact_number'].values[0]

#     # Get input from the user
#     inputted_first_name = first_name_signup.get()
#     inputted_mid_name = middle_name_signup.get()
#     inputted_last_name = last_name_signup.get()
#     inputted_username = user_name_signup.get()
#     inputted_password = password_signup.get()

#     try:
#         df = pd.read_csv(csv_file_path)
#     except FileNotFoundError:
#         # If the file doesn't exist, create a new DataFrame
#         df = pd.DataFrame(columns=['first_name', 'mid_name', 'last_name', 'username', 'password'])

#     # Create a new DataFrame with the inputted data
#     new_data = pd.DataFrame({
#         'first_name': [inputted_first_name],
#         'mid_name': [inputted_mid_name],
#         'last_name': [inputted_last_name],
#         'username': [inputted_username],
#         'password': [inputted_password],
#     })

#     # Append the new data to the existing DataFrame
#     # df = pd.concat([df, new_data], ignore_index=True)

#     # Save the updated DataFrame to the CSV file
#     df.to_csv(csv_file_path, index=False, mode='w')

#     # df = pd.DataFrame({
#     #     'first_name': [inputted_first_name],
#     #     'mid_name': [inputted_mid_name],
#     #     'last_name': [inputted_last_name],
#     #     'username': [inputted_username],
#     #     'password': [inputted_password],
#     #     'confirm_password': [confirm_pass],
#     #     'email': [email],
#     #     'contact_number': [contact]
#     # })

#     # # append the dataframe


#     # # save the dataframe as a csv file
#     # df.to_csv(csv_file_path, mode='w', index=False)






def next_button_clicked():
    canvas.itemconfigure(first_name_img, state="hidden")
    canvas.itemconfigure(middle_name_img, state="hidden")
    canvas.itemconfigure(last_name_img, state="hidden")
    canvas.itemconfigure(username_img, state="hidden")
    canvas.itemconfigure(password_img, state="hidden")
    first_name_signup.place_forget()
    middle_name_signup.place_forget()
    last_name_signup.place_forget()
    user_name_signup.place_forget()
    password_signup.place_forget()
    next_button1.place_forget()
    back_button1.place_forget()

    # show the next part of the form
    canvas.itemconfigure(confirm_pass_img, state="normal")
    confirm_password.place(
        x=415.0,
        y=111.0,
        width=356.0,
        height=32
    )

    canvas.itemconfigure(email_img, state="normal")
    email_address.place(
        x=415.0,
        y=179.0,
        width=356.0,
        height=32
    )

    canvas.itemconfigure(contact_no_img, state="normal")
    contact_number.place(
        x=415.0,
        y=250.0,
        width=356.0,
        height=32
    )

    terms_and_conditions.place(
        x=443.0,
        y=391.0,
        width=301.0,
        height=61.0
    )

    back_button2.place(
        x=410.0,
        y=309.0,
        width=112.8924560546875,
        height=39.0
    )

    login_button.place(
        x=619.0,
        y=309.0,
        width=159.0,
        height=38.57142639160156
    )

def back_button2_clicked():
    canvas.itemconfigure(confirm_pass_img, state="hidden")
    canvas.itemconfigure(email_img, state="hidden")
    canvas.itemconfigure(contact_no_img, state="hidden")
    confirm_password.place_forget()
    email_address.place_forget()
    contact_number.place_forget()
    terms_and_conditions.place_forget()
    back_button2.place_forget()
    login_button.place_forget()

    canvas.itemconfigure(first_name_img, state="normal")
    canvas.itemconfigure(middle_name_img, state="normal")
    canvas.itemconfigure(last_name_img, state="normal")
    canvas.itemconfigure(username_img, state="normal")
    canvas.itemconfigure(password_img, state="normal")
    first_name_signup.place(
        x=419.0,
        y=106.0,
        width=353.0,
        height=34.0
    )
    middle_name_signup.place(
        x=419.0,
        y=174.0,
        width=353.0,
        height=34.0
    )
    last_name_signup.place(
        x=419.0,
        y=241.0,
        width=353.0,
        height=34
    )
    user_name_signup.place(
        x=419.0,
        y=309.0,
        width=353.0,
        height=34
    )
    password_signup.place(
        x=419.0,
        y=383.0,
        width=353.0,
        height=34
    )
    next_button1.place(
        x=665.0,
        y=441.0,
        width=112.89242553710938,
        height=39.0
    )
    back_button1.place(
        x=410.0,
        y=441.0,
        width=112.8924560546875,
        height=39.0
    )

def login_button_clicked():
    save_input()
    window.withdraw()
    subprocess.Popen(["python", "signupframe3.py"])

def save_input():
    csv_file_path = "data/profile_data.csv"
    df = pd.read_csv(csv_file_path)

    # get the user input
    inputted_first_name = first_name_signup.get()
    inputted_middle_name = middle_name_signup.get()
    inputted_last_name = last_name_signup.get()
    inputted_username = user_name_signup.get()
    inputted_password = password_signup.get()
    inputted_confirm_pass = confirm_password.get()
    inputted_email = email_address.get()
    inputted_contact = contact_number.get()

    df = pd.DataFrame({
        'first_name': [inputted_first_name],
        'middle_name': [inputted_middle_name],
        'last_name': [inputted_last_name],
        'username': [inputted_username],
        'password': [inputted_password],
        'confirm_password': [inputted_confirm_pass],
        'email': [inputted_email],
        'contact_number': [inputted_contact]
    })

    # append the dataframe
    df.to_csv(csv_file_path, mode='a', index=False, header=False)



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
    49.0,
    anchor="nw",
    text="Sign Up ",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

#image for the entry boxes
form_image_1 = PhotoImage(
    file=relative_to_assets("first_name.png"))
first_name_img = canvas.create_image(
    594.0,
    118.70454406738281,
    image=form_image_1,
)

form_image_2 = PhotoImage(
    file=relative_to_assets("middle_name.png"))
middle_name_img = canvas.create_image(
    594.0,
    186.0,
    image=form_image_2
)

form_image_3 = PhotoImage(
    file=relative_to_assets("last_name.png"))
last_name_img = canvas.create_image(
    594.0,
    253.52588653564453,
    image=form_image_3
)

form_image_4 = PhotoImage(
    file=relative_to_assets("username.png"))
username_img = canvas.create_image(
    594.0,
    320.66865730285645,
    image=form_image_4
)

form_image_5 = PhotoImage(
    file=relative_to_assets("password.png"))
password_img = canvas.create_image(
    594.0,
    395.33442878723145,
    image=form_image_5
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


button_image_1 = PhotoImage(
    file=relative_to_assets("next.png"))
next_button1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=next_button_clicked,
    relief="flat",
)
next_button1.place(
    x=665.0,
    y=441.0,
    width=112.89242553710938,
    height=39.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("back.png"))
back_button1 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=back_button1_clicked,
    relief="flat"
)
back_button1.place(
    x=410.0,
    y=441.0,
    width=112.8924560546875,
    height=39.0
)

#-----------Next Form-----------------
# image for the next form
form_image_6 = PhotoImage(
    file=relative_to_assets("confirm_pass.png"))
confirm_pass_img = canvas.create_image(
    594.0,
    122.410400390625,
    image=form_image_6,
    state="hidden",
)
form_image_7 = PhotoImage(
    file=relative_to_assets("email.png"))
email_img = canvas.create_image(
    594.0,
    191.41039276123047,
    image=form_image_7,
    state="hidden",
)
form_image_8 = PhotoImage(
    file=relative_to_assets("contact_no.png"))
contact_no_img = canvas.create_image(
    594.0,
    259.69991302490234,
    image=form_image_8,
    state="hidden",
)


confirm_password = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show='*'
)
email_address = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
contact_number = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)

terms_image = PhotoImage(
    file=relative_to_assets("terms.png"))
terms_and_conditions = Button(
    image=terms_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)

back_image = PhotoImage(
    file=relative_to_assets("back.png"))
back_button2 = Button(
    image=back_image,
    borderwidth=0,
    highlightthickness=0,
    command=back_button2_clicked,
    relief="flat"
)

login_image = PhotoImage(
    file=relative_to_assets("login.png"))
login_button = Button(
    image=login_image,
    borderwidth=0,
    highlightthickness=0,
    command=login_button_clicked,
    relief="flat"
) 

window.resizable(False, False)
window.mainloop()
