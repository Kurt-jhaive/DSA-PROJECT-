import tkinter as tk
from tkinter import Button, Entry, Radiobutton, StringVar, Text, Label

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
        first_name_img = self.create_image(
            594.0,
            118.70454406738281,
            image=self.images["form_image_1"]
        )

        middle_name_img = self.create_image(
            594.0,
            186.0,
            image=self.images["form_image_2"]
        )

        last_name_img = self.create_image(
            594.0,
            253.52588653564453,
            image=self.images["form_image_3"]
        )

        username_img = self.create_image(
            594.0,
            320.66865730285645,
            image=self.images["form_image_4"]
        )

        password_img = self.create_image(
            594.0,
            395.33442878723145,
            image=self.images["form_image_5"]
        )


        first_name_signup  = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            cursor="ibeam",
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

        next_button1 = Button(
            image=self.images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            command=self.next_button_clicked,
            relief="flat",
        )
        next_button1.place(
            x=665.0,
            y=441.0,
            width=112.89242553710938,
            height=39.0
        )

        back_button1 = Button(
            image=self.images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=self.back_button1_clicked,
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
        confirm_pass_img = self.create_image(
            594.0,
            122.410400390625,
            image=self.images["form_image_6"],
            state="hidden",
        )
        email_img = self.create_image(
            594.0,
            191.41039276123047,
            image=self.images["form_image_7"],
            state="hidden",
        )
        contact_no_img = self.create_image(
            594.0,
            259.69991302490234,
            image=self.images["form_image_8"],
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
        terms_and_conditions = Button(
            image=self.images["terms_image"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            bg="#FFFFFF",
                
        )
        back_button2 = Button(
            image=self.images["back_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.back_button2_clicked,
            relief="flat"
        )

        signup_button = Button(
            image=self.images["signup_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.signup_button_clicked,
            relief="flat"
        ) 

    def back_button1_clicked(self):
        self.main_app.show_login()

    def back_button2_clicked(self):
        pass
        # add the functionality of going back to the previous form
    
    def next_button_clicked(self):
        pass
        # add the functionality of going to the next form
    
    def signup_button_clicked(self):
        pass
        self.app_main.show_signup_2()
        # add the functionality of signing up