import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Entry

class DonateFrame(tk.Canvas):
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
            352.0,
            72.0,
            image=self.images["image_2"]
        )

        favorites_button = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=self.images["button_1"],
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

        button_3 = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["button_3"],
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
            image=self.images["button_4"],
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
            image=self.images["button_5"],
            borderwidth=0,
            highlightthickness=0,
            # command=register_button_clicked,
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
            image=self.images["button_6"],
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

        button_7 = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["button_7"],
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

        image_3 = self.create_image(
            540.0,
            323.0,
            image=self.images["image_3"]    
        )

        image_4 = self.create_image(
            540.0,
            259.0,
            image=self.images["image_4"]
        )

        image_5 = self.create_image(
            540.0,
            194.0,
            image=self.images["image_5"]
        )

        image_6 = self.create_image(
            415.0,
            133.0,
            image=self.images["image_6"]
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
            x=455.0,
            y=412.0,
            width=159.0,
            height=39.0
        )

        image_7 = self.create_image(
            663.0,
            133.0,
            image=self.images["image_7"]
        )

        image_8 = self.create_image(
            540.0,
            387.0,
            image=self.images["image_8"]
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