import tkinter as tk
from tkinter import Button, Entry, Radiobutton, StringVar, Text, Label
from data_handler import read_input
import pandas as pd

class SignupFrame1(tk.Canvas):
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

        image_2 = self.create_image(
            183.0,
            237.0,
            image=self.images["image_2"]
        )

        self.create_text(
            410.0,
            49.0,
            anchor="nw",
            text="Sign Up ",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1)
        )

        #image for the entry boxes
        self.first_name_img = self.create_image(
            594.0,
            118.70454406738281,
            image=self.images["form_image_1"]
        )

        self.middle_name_img = self.create_image(
            594.0,
            186.0,
            image=self.images["form_image_2"]
        )

        self.last_name_img = self.create_image(
            594.0,
            253.52588653564453,
            image=self.images["form_image_3"]
        )

        self.username_img = self.create_image(
            594.0,
            320.66865730285645,
            image=self.images["form_image_4"]
        )

        self.password_img = self.create_image(
            594.0,
            395.33442878723145,
            image=self.images["form_image_5"]
        )


        self.first_name_signup  = Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            cursor="ibeam",
        )
        self.first_name_signup.place(
            x=419.0,
            y=106.0,
            width=353.0,
            height=34.0
        )
        self.first_name_signup.focus()

        self.middle_name_signup = Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.middle_name_signup.place(
            x=419.0,
            y=174.0,
            width=353.0,
            height=34.0
        )

        self.last_name_signup= Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.last_name_signup.place(
            x=419.0,
            y=241.0,
            width=353.0,
            height=34
        )

        self.user_name_signup  = Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.user_name_signup.place(
            x=419.0,
            y=309.0,
            width=353.0,
            height=34
        )

        self.password_signup = Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            show='*'
        )
        self.password_signup.place(
            x=419.0,
            y=383.0,
            width=353.0,
            height=34
        )

        self.next_button1 = Button(
            image=self.images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            command=self.next_button_clicked,
            relief="flat",
        )
        self.next_button1.place(
            x=665.0,
            y=441.0,
            width=112.89242553710938,
            height=39.0
        )

        self.back_button1 = Button(
            image=self.images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=self.back_button1_clicked,
            relief="flat"
        )
        self.back_button1.place(
            x=410.0,
            y=441.0,
            width=112.8924560546875,
            height=39.0
        )

        #-----------Next Form-----------------
        # image for the next form
        self.confirm_pass_img = self.create_image(
            594.0,
            122.410400390625,
            image=self.images["form_image_6"],
            state="hidden",
        )
        self.email_img = self.create_image(
            594.0,
            191.41039276123047,
            image=self.images["form_image_7"],
            state="hidden",
        )
        self.contact_no_img = self.create_image(
            594.0,
            259.69991302490234,
            image=self.images["form_image_8"],
            state="hidden",
        )

        self.confirm_password = Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            show='*'
        )
        self.email_address = Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.contact_number = Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.terms_and_conditions = Button(
            image=self.images["terms_image"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            bg="#FFFFFF",
        )
        self.back_button2 = Button(
            image=self.images["back_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.back_button2_clicked,
            relief="flat"
        )
        self.signup_button = Button(
            image=self.images["signup_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.signup_button_clicked,
            relief="flat"
        ) 

        # read the inputted data from the file and put it into the entry widgets
        self.read_input_data()

    def back_button1_clicked(self):
        self.main_app.show_login()

    def next_button_clicked(self):
        # Hide the current part of the form
        self.itemconfigure(self.first_name_img, state="hidden")
        self.itemconfigure(self.middle_name_img, state="hidden")
        self.itemconfigure(self.last_name_img, state="hidden")
        self.itemconfigure(self.username_img, state="hidden")
        self.itemconfigure(self.password_img, state="hidden")
        self.first_name_signup.place_forget()
        self.middle_name_signup.place_forget()
        self.last_name_signup.place_forget()
        self.user_name_signup.place_forget()
        self.password_signup.place_forget()
        self.back_button1.place_forget()    
        self.next_button1.place_forget()

        # Show the next part of the form
        self.itemconfigure(self.confirm_pass_img, state="normal")
        self.confirm_password.place(x=415.0, y=111.0, width=356.0, height=32)
        self.itemconfigure(self.email_img, state="normal")
        self.email_address.place(x=415.0, y=179.0, width=356.0, height=32)
        self.itemconfigure(self.contact_no_img, state="normal")
        self.contact_number.place(x=415.0, y=250.0, width=356.0, height=32)
        self.terms_and_conditions.place(x=443.0, y=391.0, width=301.0, height=61.0)
        self.back_button2.place(x=410.0, y=309.0, width=112.8924560546875, height=39.0)
        self.signup_button.place(x=619.0, y=309.0, width=159.0, height=38.57142639160156)

        # Set the focus to the first entry box
        self.confirm_password.focus()
    
    def back_button2_clicked(self):
        # Hide the current part of the form
        self.itemconfigure(self.confirm_pass_img, state="hidden")
        self.itemconfigure(self.email_img, state="hidden")
        self.itemconfigure(self.contact_no_img, state="hidden")
        self.confirm_password.place_forget()
        self.email_address.place_forget()
        self.contact_number.place_forget()
        self.terms_and_conditions.place_forget()
        self.back_button2.place_forget()
        self.signup_button.place_forget()

        # Show the previous part of the form
        self.itemconfigure(self.first_name_img, state="normal")
        self.itemconfigure(self.middle_name_img, state="normal")
        self.itemconfigure(self.last_name_img, state="normal")
        self.itemconfigure(self.username_img, state="normal")
        self.itemconfigure(self.password_img, state="normal")
        self.first_name_signup.place(x=419.0, y=106.0, width=353.0, height=34.0)
        self.middle_name_signup.place(x=419.0, y=174.0, width=353.0, height=34.0)
        self.last_name_signup.place(x=419.0, y=241.0, width=353.0, height=34)
        self.user_name_signup.place(x=419.0, y=309.0, width=353.0, height=34)
        self.password_signup.place(x=419.0, y=383.0, width=353.0, height=34)
        self.next_button1.place(x=665.0, y=441.0, width=112.89242553710938, height=39.0)
        self.back_button1.place(x=410.0, y=441.0, width=112.8924560546875, height=39.0)

        # Set the focus to the first entry box
        self.first_name_signup.focus()

    def signup_button_clicked(self):
        self.save_input_data()
        self.main_app.show_signup_2()

    def save_input_data(self):
        #save the inputs to the data/signup_data.txt file
        with open("data/signup_data.txt", "w") as f:
            f.write(self.first_name_signup.get() + "\n")
            f.write(self.middle_name_signup.get() + "\n")
            f.write(self.last_name_signup.get() + "\n")
            f.write(self.user_name_signup.get() + "\n")
            f.write(self.password_signup.get() + "\n")
            f.write(self.confirm_password.get() + "\n")
            f.write(self.email_address.get() + "\n")
            f.write(self.contact_number.get() + "\n")

    def read_input_data(self):
        read_input(self)