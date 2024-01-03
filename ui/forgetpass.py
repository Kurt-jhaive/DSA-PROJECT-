import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Entry, Label

class ForgetPassFrame(tk.Canvas):
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

        email_image_label = Label(
            bg="#FFFFFF",
            image=self.images["label_email"],
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

        otp_image_label = Label(
            bg="#FFFFFF",
            image=self.images["label_otp"],
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

        newpass_image_label = Label(
            bg="#FFFFFF",
            image=self.images["label_newpass"],
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

        login_button = Button(
            image=self.images["button_login"],
            borderwidth=0,
            highlightthickness=0,
            command=self.login_button_clicked,
            relief="flat"
        )
        login_button.place(
            x=413.0,
            y=404.0,
            width=159.0,
            height=39.0
        )

        submit_button = Button(
            image=self.images["button_submit"],
            borderwidth=0,
            highlightthickness=0,
            command=self.submit_button,
            relief="flat"
        )
        submit_button.place(
            x=522.0,
            y=345.0,
            width=159.0,
            height=39.0
        )

        signup_button = Button(
            image=self.images["button_signup"],
            borderwidth=0,
            highlightthickness=0,
            command=self.sign_up_button_clicked,
            relief="flat"
        )
        signup_button.place(
            x=627.0,
            y=404.0,
            width=159.0,
            height=39.0
        )

        otp_button = Button(
            bg="#FFFFFF",
            image=self.images["button_otp"],
            borderwidth=0,
            highlightthickness=0,
            command=self.send_otp,
            relief="flat"
        )
        otp_button.place(
            x=722.0,
            y=243.0,
            width=62.0,
            height=12.0
        )

        image_2 = self.create_image(
            189.0,
            241.0,
            image=self.images["image_2"]
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
    
    def send_otp(self):
        pass
        # add the functionality of sending otp

    def submit_button_clicked(self):
        pass
        # add the functionality of submitting the otp and new password
    
    def login_button_clicked(self):
        self.main_app.show_login()

    def sign_up_button_clicked(self):
        self.main_app.show_signup()