from tkinter import *
from tkinter import messagebox
from pathlib import Path
import subprocess
import smtplib
import random
import pandas as pd
import os
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\forgetpass_frame")

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
my_email = "purrfectmatch.python@gmail.com"
email_password = "qlde sugx xcbw eatc"
smtp_server = "smtp.gmail.com"
smtp_port = 587
typed_email = ""
otp = None

def check_email():
    global typed_email
    typed_email = email_textbox.get()
    df = pd.read_csv(resource_path("../../_internal/data/new_credentials.csv"))
    if typed_email in df['email'].values:
        return True
    else:
        return False

def send_otp():
    global otp, typed_email
    if check_email():
        otp = str(random.randint(100000, 999999))
        messagebox.showinfo("Pending", "Your OTP has been sent!")

        # replace the [OTP] with the otp variable
        with open(resource_path("../../_internal/data/otp_email_letter.txt")) as file:
            letter = file.read().replace("[OTP]", otp)
        typed_email = email_textbox.get()

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as connection:
            connection.starttls()
            connection.login(user=my_email, password=email_password)
            connection.sendmail(from_addr=my_email, to_addrs=typed_email, msg=f"Subject:OTP Request\n\n{letter}")
    else:
        messagebox.showerror("Error", "The email you entered is not registered. Please try again.")

def submit_button():
    global otp, typed_email

    # if the typed otp is same w the otp variable, then change the password go to loginframe.py
    typed_otp = otp_textbox.get()
    if typed_otp == otp:
        new_password = newpassword_textbox.get()
        df = pd.read_csv(resource_path("../../_internal/data/profile_data.csv"))
        df.loc[df['email'] == typed_email, 'password'] = new_password
        df.to_csv(resource_path("../../_internal/data/profile_data.csv"), index=False)
        messagebox.showinfo("Success", "Your password has been reset successfully!")

        window.destroy()
        subprocess.Popen(["purrfectmatch.exe"])
    else:
        messagebox.showerror("Error", "The OTP you entered is invalid. Please try again.")

def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

def login_button_clicked():
    window.destroy()
    subprocess.Popen(["purrfectmatch.exe"])

def sign_up_button_clicked():
    window.destroy()
    subprocess.Popen(["signupframe1/signupframe1.exe"])

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
    file=relative_to_assets(resource_path("forms/forgetpass_frame/image_1.png")))
image_1 = canvas.create_image(
    190.0,
    250.0,
    image=image_image_1
)

canvas.create_text(
    410.0,
    47.0,
    anchor="nw",
    text="Forget Password",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

email_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/forgetpass_frame/label_1.png")))
email_image_label = Label(
    bg="#FFFFFF",
    image=email_image,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
email_image_label.place(
    x=410.0,
    y=95.0,
    width=376.0,
    height=62.59821701049805
)

otp_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/forgetpass_frame/label_2.png")))
otp_image_label = Label(
    bg="#FFFFFF",
    image=otp_image,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
otp_image_label.place(
    x=410.0,
    y=173.0,
    width=376.0,
    height=62.59821701049805
)

newpass_image = PhotoImage(
    file=relative_to_assets(resource_path("forms/forgetpass_frame/label_3.png")))
newpass_image_label = Label(
    bg="#FFFFFF",
    image=newpass_image,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
newpass_image_label.place(
    x=410.0,
    y=262.0,
    width=376.0,
    height=62.59821701049805
)

login_btn_img = PhotoImage(
    file=relative_to_assets(resource_path("forms/forgetpass_frame/button_4.png")))
login_button = Button(
    image=login_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=login_button_clicked,
    relief="flat"
)
login_button.place(
    x=413.0,
    y=404.0,
    width=159.0,
    height=39.0
)

submit_btn_img = PhotoImage(
    file=relative_to_assets(resource_path("forms/forgetpass_frame/button_5.png")))
submit_button = Button(
    image=submit_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=submit_button,
    relief="flat"
)
submit_button.place(
    x=522.0,
    y=345.0,
    width=159.0,
    height=39.0
)

signup_btn_img = PhotoImage(
    file=relative_to_assets(resource_path("forms/forgetpass_frame/button_6.png")))
signup_button = Button(
    image=signup_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up_button_clicked,
    relief="flat"
)
signup_button.place(
    x=627.0,
    y=404.0,
    width=159.0,
    height=39.0
)

otp_btn_img = PhotoImage(
    file=relative_to_assets(resource_path("forms/forgetpass_frame/button_7.png")))
otp_button = Button(
    bg="#FFFFFF",
    image=otp_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=send_otp,
    relief="flat"
)
otp_button.place(
    x=722.0,
    y=243.0,
    width=62.0,
    height=12.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/forgetpass_frame/image_2.png")))
image_2 = canvas.create_image(
    189.0,
    241.0,
    image=image_image_2
)

# Entry of email, otp, and new password
email_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
email_textbox.place(
    x=423.0,
    y=115.0,
    width=355.0,
    height=37
)
otp_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
otp_textbox.place(
    x=423.0,
    y=190.0,
    width=355.0,
    height=37
)
newpassword_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show='*'
)
newpassword_textbox.place(
    x=423.0,
    y=279.0,
    width=355.0,
    height=37
)
window.resizable(False, False)
window.mainloop()
