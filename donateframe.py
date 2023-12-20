from tkinter import *
from tkinter import messagebox
import subprocess
import pandas as pd
import os
import sys


from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\donate_frame")

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

def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()


def submit_button_clicked(): 
    csv_file_path = resource_path("../../_internal/data/donate_data.csv")

    # check if all fields are filled up
    if not(name_textbox.get() and contactnumber_textbox.get() and address_textbox.get() and email_textbox.get() and donation_type_textbox.get()):
        messagebox.showerror("Error", "Please fill up all fields.")
    else:
        # messagebox.showinfo("Success", "Your registration for donation has been submitted! Please wait for our team to contact you.")

        # Get input from the user
        inputted_name = name_textbox.get()
        inputted_contactnumber = contactnumber_textbox.get()
        inputted_address = address_textbox.get()
        inputted_email = email_textbox.get()
        inputted_donation = donation_type_textbox.get()

        try:
            df = pd.read_csv(csv_file_path)
        except FileNotFoundError:
            # If the file doesn't exist, create a new DataFrame
            df = pd.DataFrame(columns=['name', 'contact_number', 'address', 'email', 'donation_type'])

        # Create a new DataFrame with the inputted data
        new_data = pd.DataFrame({
            'name': [inputted_name],
            'contact_number': [inputted_contactnumber],
            'address': [inputted_address],
            'email': [inputted_email],
            'donation_type': [inputted_donation]
        })

        # Append the new data to the existing DataFrame
        df = pd.concat([df, new_data], ignore_index=True)

        # Save the updated DataFrame to the CSV file
        df.to_csv(csv_file_path, index=False)

        window.destroy()
        subprocess.Popen(["thankyou_donate/thankyou_donate.exe"])

def change_profile_display():
    #read the text file
    with open(resource_path("../../_internal/data/current_user.txt"), "r") as file:
        current_user = file.read().strip()
    
    #get the display name of the current user
    df = pd.read_csv(resource_path('../../_internal/data/profile_data.csv'))
    user_row = df[df['username'] == current_user]
    display_name = user_row['display_name'].values[0]
    display_location = user_row['address'].values[0]

    #change the display name and location
    canvas.itemconfigure(display_name_canvas, text=display_name)
    canvas.itemconfigure(profile_location, text=display_location)

def hamburger_menu_clicked():
    # show the hamburger menu
    canvas.itemconfigure(pink_menu_rectangle_canvas, state="normal")
    contactnumber_textbox.lower()
    address_textbox.lower()
    email_textbox.lower()
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
    contactnumber_textbox.lift()
    address_textbox.lift()
    email_textbox.lift()
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
    file=relative_to_assets(resource_path("forms/donate_frame/image_1.png")))
image_1 = canvas.create_image(
    158.0,
    251.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/image_2.png")))
image_2 = canvas.create_image(
    352.0,
    72.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/button_1.png")))
favorites_button = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("favorites_buttonclicked"),
    relief="flat"
)
favorites_button.place(
    x=713.0,
    y=42.0,
    width=31.0,
    height=34.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/button_2.png")))
hamburger_menu = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=hamburger_menu_clicked,
    relief="flat"
)
hamburger_menu.place(
    x=749.0,
    y=42.0,
    width=23.0,
    height=35.0
)
close_hamburger_menu = Button(
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=close_hamburger_menu_clicked,
    relief="flat"
)



button_image_3 = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/button_3.png")))
button_3 = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=65.0,
    y=64.0,
    width=34.0,
    height=36.0
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

button_image_4 = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/button_4.png")))
home_button = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_4,
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

button_image_5 = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/button_5.png")))
register_button = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=register_button_clicked,
    relief="flat"
)
register_button.place(
    x=95.0,
    y=204.0,
    width=120.0,
    height=30.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/button_6.png")))
donate_button = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
donate_button.place(
    x=95.0,
    y=253.0,
    width=120.0,
    height=30.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/button_7.png")))
button_7 = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=65.0,
    y=64.0,
    width=34.0,
    height=36.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/image_3.png")))
image_3 = canvas.create_image(
    540.0,
    323.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/image_4.png")))
image_4 = canvas.create_image(
    540.0,
    259.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/image_5.png")))
image_5 = canvas.create_image(
    540.0,
    194.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/image_6.png")))
image_6 = canvas.create_image(
    415.0,
    133.0,
    image=image_image_6
)

button_image_8 = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/button_8.png")))
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
    x=455.0,
    y=412.0,
    width=159.0,
    height=39.0
)

image_image_7 = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/image_7.png")))
image_7 = canvas.create_image(
    663.0,
    133.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/image_8.png")))
image_8 = canvas.create_image(
    540.0,
    387.0,
    image=image_image_8
)
name_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
name_textbox.place(
    x=318.0,
    y=124.0,
    width=194.0,
    height=30
)
contactnumber_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
contactnumber_textbox.place(
    x=567.0,
    y=125.0,
    width=194.0,
    height=30
)
address_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
address_textbox.place(
    x=318.0,
    y=186.0,
    width=443.0,
    height=28
)
email_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
email_textbox.place(
    x=318.0,
    y=251.0,
    width=443.0,
    height=28
)
donation_type_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
donation_type_textbox.place(
    x=318.0,
    y=315.0,
    width=443.0,
    height=28
)

#----------------------- Hamburger Menu------------------
# HAMBURGER FRAME
pink_menu_rectangle_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/pink_menu.png")))
pink_menu_rectangle_canvas = canvas.create_image(
    654.0,
    194.0,
    image=pink_menu_rectangle_image,
    state="hidden",
)

account_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/donate_frame/account.png")))
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
    file=relative_to_assets(resource_path("forms/donate_frame/privacy.png")))
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
    file=relative_to_assets(resource_path("forms/donate_frame/terms.png")))
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
    file=relative_to_assets(resource_path("forms/donate_frame/feedback.png")))
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
    file=relative_to_assets(resource_path("forms/donate_frame/logout.png")))
log_out = Button(
    bg="#F19FB5",
    activebackground="#F19FB5",
    image=logout_image,
    borderwidth=0,
    highlightthickness=0,
    command=log_out_button_clicked,
    relief="flat"
)

change_profile_display()

window.resizable(False, False)
window.mainloop()
