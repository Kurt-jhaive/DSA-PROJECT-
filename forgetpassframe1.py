
from pathlib import Path
from tkinter import *
from tkinter import messagebox
import subprocess
import smtplib
import random
import pandas as pd



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\forgetpassframe_resources\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
my_email = "yasgamingofficial@gmail.com"
email_password = "xvwi jcex gwqq zwtg"
smtp_server = "smtp.gmail.com"
smtp_port = 587
typed_email = ""
otp = ""

def check_email():
    global typed_email
    typed_email = email_textbox.get()
    df = pd.read_csv("data/new_credentials.csv")
    if typed_email in df['email'].values:
        return True
    else:
        return False

def send_otp():
    global otp, typed_email
    if check_email():
        otp = str(random.randint(100000, 999999))
        messagebox.showinfo("Pending", "Your OTP has been sent! Please wait for the email from our team.")

        # replace the [OTP] with the otp variable
        with open("otp_email_letter.txt") as file:
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
        df = pd.read_csv("data/new_credentials.csv")
        df.loc[df['email'] == typed_email, 'password'] = new_password
        df.to_csv("data/new_credentials.csv", index=False)
        messagebox.showinfo("Success", "Your password has been reset successfully!")

        window.destroy()
        subprocess.Popen(["python", "loginframe.py"])
    else:
        messagebox.showerror("Error", "The OTP you entered is invalid. Please try again.")

def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

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

canvas.create_text(
    410.0,
    47.0,
    anchor="nw",
    text="Forget Password",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=410.0,
    y=95.0,
    width=376.0,
    height=62.59821701049805
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=410.0,
    y=173.0,
    width=376.0,
    height=62.59821701049805
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=410.0,
    y=262.0,
    width=376.0,
    height=62.59821701049805
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
login_button = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
login_button.place(
    x=413.0,
    y=404.0,
    width=159.0,
    height=39.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
submit_button1 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=submit_button,
    relief="flat"
)
submit_button1.place(
    x=522.0,
    y=345.0,
    width=159.0,
    height=39.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
sign_up_button = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
sign_up_button.place(
    x=627.0,
    y=404.0,
    width=159.0,
    height=39.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
send_otp1 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=send_otp,
    relief="flat"
)
send_otp1.place(
    x=722.0,
    y=243.0,
    width=62.0,
    height=12.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    189.0,
    241.0,
    image=image_image_2
)
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
