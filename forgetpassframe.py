from tkinter import *
from tkinter import messagebox
import subprocess
import smtplib
import random
import pandas as pd

my_email = "yasgamingofficial@gmail.com"
email_password = "xvwi jcex gwqq zwtg"
smtp_server = "smtp.gmail.com"
smtp_port = 587
typed_email = ""
otp = ""

def check_email():
    global typed_email
    typed_email = email_entry.get()
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
        typed_email = email_entry.get()

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
    typed_otp = otp_entry.get()
    if typed_otp == otp:
        new_password = new_password_entry.get()
        df = pd.read_csv("data/new_credentials.csv")
        df.loc[df['email'] == typed_email, 'password'] = new_password
        df.to_csv("data/new_credentials.csv", index=False)
        messagebox.showinfo("Success", "Your password has been reset successfully!")

        window.destroy()
        subprocess.Popen(["python", "loginframe.py"])
    else:
        messagebox.showerror("Error", "The OTP you entered is invalid. Please try again.")



window = Tk()   
window.title("Forgot Password")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates for the window to be centered
x = (screen_width - 820) // 2
y = (screen_height - 500) // 2

window.geometry(f"820x500+{x}+{y}")
window.configure(bg="#FFFFFF")

email_label = Label(window, text="Email",)
email_label.pack()

email_entry = Entry(window)
email_entry.pack()

otp_label = Label(window, text="OTP")
otp_label.pack()

otp_entry = Entry(window)
otp_entry.pack()

otp_button = Button(window, text="Send OTP", command=send_otp)
otp_button.pack()

new_password_label = Label(window, text="New Password")
new_password_label.pack()

new_password_entry = Entry()
new_password_entry.pack()

submit_button = Button(window, text="Submit", command=submit_button)
submit_button.pack()

window.mainloop()
