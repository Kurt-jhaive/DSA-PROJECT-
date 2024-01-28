import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Entry, Label
from function_helper import resource_path
import random
import smtplib
import pandas as pd
from tkinter import messagebox


class ForgetPassFrame(tk.Canvas):
    my_email = "purrfectmatch.python@gmail.com"
    email_password = "qlde sugx xcbw eatc"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    typed_email = ""
    otp = None

    def __init__(self, master=None, images=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)

        # To access the methods of the MainApp class
        self.main_app = master  

        self.images = images

        image_1 = self.create_image(
            190.0,
            250.0,
            image=self.images["image_1"]    
        )

        self.create_text(
            410.0,
            47.0,
            anchor="nw",
            text="Forget Password",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1)
        )

        self.email_image_label = Label(
            bg="#FFFFFF",
            image=self.images["label_email"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.email_image_label.place(
            x=410.0,
            y=95.0,
            width=376.0,
            height=62.59821701049805
        )

        self.otp_image_label = Label(
            bg="#FFFFFF",
            image=self.images["label_otp"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.otp_image_label.place(
            x=410.0,
            y=173.0,
            width=376.0,
            height=62.59821701049805
        )

        self.newpass_image_label = Label(
            bg="#FFFFFF",
            image=self.images["label_newpass"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.newpass_image_label.place(
            x=410.0,
            y=262.0,
            width=376.0,
            height=62.59821701049805
        )

        self.login_button = Button(
            image=self.images["button_login"],
            borderwidth=0,
            highlightthickness=0,
            command=self.login_button_clicked,
            relief="flat"
        )
        self.login_button.place(
            x=413.0,
            y=404.0,
            width=159.0,
            height=39.0
        )

        self.submit_button = Button(
            image=self.images["button_submit"],
            borderwidth=0,
            highlightthickness=0,
            command=self.submit_button_clicked,
            relief="flat"
        )
        self.submit_button.place(
            x=522.0,
            y=345.0,
            width=159.0,
            height=39.0
        )

        self.signup_button = Button(
            image=self.images["button_signup"],
            borderwidth=0,
            highlightthickness=0,
            command=self.sign_up_button_clicked,
            relief="flat"
        )
        self.signup_button.place(
            x=627.0,
            y=404.0,
            width=159.0,
            height=39.0
        )

        self.otp_button = Button(
            bg="#FFFFFF",
            image=self.images["button_otp"],
            borderwidth=0,
            highlightthickness=0,
            command=self.send_otp,
            relief="flat"
        )
        self.otp_button.place(
            x=722.0,
            y=243.0,
            width=62.0,
            height=12.0
        )

        self.image_2 = self.create_image(
            189.0,
            241.0,
            image=self.images["image_2"]
        )

        # Entry of email, otp, and new password
        self.email_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.email_textbox.place(
            x=423.0,
            y=115.0,
            width=355.0,
            height=37
        )
        self.otp_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.otp_textbox.place(
            x=423.0,
            y=190.0,
            width=355.0,
            height=37
        )
        self.newpassword_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            show='*'
        )
        self.newpassword_textbox.place(
            x=423.0,
            y=279.0,
            width=355.0,
            height=37
        )

    def check_email(self):
        self.typed_email = self.email_textbox.get()
        df = pd.read_csv(resource_path("data/profile_data.csv"))
        if self.typed_email in df['email'].values:
            return True
        else:
            return False

    def send_otp(self):
        if self.check_email():
            self.otp = str(random.randint(100000, 999999))
            messagebox.showinfo("Pending", "Your OTP has been sent!")

            # replace the [OTP] with the otp variable
            with open(resource_path("data/otp_email_letter.txt")) as file:
                letter = file.read().replace("[OTP]", self.otp)
            self.typed_email = self.email_textbox.get()

            # Send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.email_password)
                connection.sendmail(from_addr=self.my_email, to_addrs=self.typed_email, msg=f"Subject:OTP Request\n\n{letter}")
        else:
            messagebox.showerror("Error", "The email you entered is not registered. Please try again.")

    def submit_button_clicked(self):
        typed_otp = self.otp_textbox.get()
        if typed_otp == self.otp:
            new_password = self.newpassword_textbox.get()
            df = pd.read_csv(resource_path("data/profile_data.csv"))
            df.loc[df['email'] == self.typed_email, 'password'] = new_password
            df.to_csv(resource_path("data/profile_data.csv"), index=False)
            messagebox.showinfo("Success", "Your password has been reset successfully!")

            self.destroy()
            self.main_app.show_login()
        else:
            messagebox.showerror("Error", "The OTP you entered is invalid. Please try again.")
   
    def login_button_clicked(self):
        self.main_app.show_login()

    def sign_up_button_clicked(self):
        self.main_app.show_signup_1()



    
