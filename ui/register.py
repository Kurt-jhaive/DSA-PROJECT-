import tkinter as tk
from tkinter import Button, Entry, Radiobutton, StringVar, Text, Label

class RegisterFrame(tk.Canvas):
    def __init__(self, master=None, images=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)
        self.images = images

        image_1 = self.create_image(
            158.0,
            251.0,
            image=self.images["image_1"]
        )

        image_2 = self.create_image(
            358.0,
            72.0,
            image=self.images["image_2"]
        )

        favorites_button = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=self.images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("favorites_button clicked"),
            relief="flat"
        )
        favorites_button.place(
            x=713.0,
            y=42.0,
            width=31.0,
            height=34.0
        )

        hamburger_menu = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=self.images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            # command=hamburger_menu_clicked,
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
            image=self.images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            # command=close_hamburger_menu_clicked,
            relief="flat"
        )

        display_name_canvas = self.create_text(
            105.0,
            66.0,
            anchor="nw",
            text="Marie Cris Edusma",
            fill="#FFFFFF",
            font=("Inter SemiBold", 14 * -1, "bold")
        )

        profile_location = self.create_text(
            105.0,
            82.0,
            anchor="nw",
            text="Taguig City",
            fill="#FFFFFF",
            font=("Inter SemiBold", 11 * -1, "bold")
        )

        home_button = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["button_3"],
            borderwidth=0,
            highlightthickness=0,
            # command=home_button_clicked,
            relief="flat"
        )
        home_button.place(
            x=95.0,
            y=155.0,
            width=120.0,
            height=30.0
        )

        register_button = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["button_4"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        register_button.place(
            x=95.0,
            y=204.0,
            width=120.0,
            height=30.0
        )

        donate_button = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["button_5"],
            borderwidth=0,
            highlightthickness=0,
            # command=donate_button_clicked,
            relief="flat"
        )
        donate_button.place(
            x=95.0,
            y=253.0,
            width=120.0,
            height=30.0
        )

        button_6 = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["button_6"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        button_6.place(
            x=65.0,
            y=64.0,
            width=34.0,
            height=36.0
        )

        image_3 = self.create_image(
            416.0,
            113.0,
            image=self.images["image_3"]
        )

        image_4 = self.create_image(
            416.0,
            171.0,
            image=self.images["image_4"]
        )

        image_5 = self.create_image(
            416.0,
            234.0,
            image=self.images["image_5"]
        )

        image_6 = self.create_image(
            539.0,
            333.0,
            image=self.images["image_6"]
        )

        image_7 = self.create_image(
            664.0,
            237.0,
            image=self.images["image_7"]
        )

        image_8 = self.create_image(
            664.0,
            172.0,
            image=self.images["image_8"]
        )

        image_9 = self.create_image(
            664.0,
            111.0,
            image=self.images["image_9"]
        )

        upload_image_button = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=self.images["button_7"],
            borderwidth=0,
            highlightthickness=0,
            # command=upload_image_button_clicked,
            relief="flat"
        )
        upload_image_button.place(
            x=311.0,
            y=411.0,
            width=159.0,
            height=39.0
        )

        upload_label = Label(
            text="",   
            fg="#000716",
            bg="#FFFFFF",
            font=("Inter Bold", 12 * -1)
        )
        upload_label.place(
            x=311.0,
            y=450.0,
            width=159.0,
            height=39.0
        )

        submit_button = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=self.images["button_8"],  
            borderwidth=0,
            highlightthickness=0,
            # command=submit_button_clicked,
            relief="flat"
        )
        submit_button.place(
            x=486.0,
            y=411.0,
            width=159.0,
            height=39.0
        )
        petname_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        petname_textbox .place(
            x=316.0,
            y=105.0,
            width=195.0,
            height=27
        )
        breed_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        breed_textbox.place(
            x=568.0,
            y=105.0,
            width=195.0,
            height=27
        )
        age_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        age_textbox.place(
            x=316.0,
            y=164.0,
            width=195.0,
            height=27
        )
        gender_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        gender_textbox.place(
            x=568.0,
            y=164.0,
            width=195.0,
            height=27
        )
        color_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        color_textbox.place(
            x=316.0,
            y=227.0,
            width=195.0,
            height=27
        )
        size_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        size_textbox.place(
            x=568.0,
            y=227.0,
            width=195.0,
            height=27
        )
        description_textbox = Text(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        description_textbox.place(
            x=316.0,
            y=295.0,
            width=447.0,
            height=91
        )

        #----------------------- Hamburger Menu------------------
        # HAMBURGER FRAME
        pink_menu_rectangle_canvas = self.create_image(
            654.0,
            194.0,
            image=self.images["pink_menu_rectangle"],    
            state="hidden",
        )

        account_settings = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["account"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("account_settings clicked"),
            relief="flat"
        )

        privacy_policy = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["privacy"],
            borderwidth=0,
            highlightthickness=0,
            # command=privacy_button_clicked,
            relief="flat"
        )

        terms_conditions = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["terms"],
            borderwidth=0,
            highlightthickness=0,
            # command=terms_button_clicked,
            relief="flat"
        )

        give_feedback = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["feedback"],
            borderwidth=0,
            highlightthickness=0,
            # command=feedback_button_clicked,
            relief="flat"
        )

        log_out = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["logout"],
            borderwidth=0,
            highlightthickness=0,
            # command=log_out_button_clicked,
            relief="flat"
        )