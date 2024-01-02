import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Entry

class HomepageFrame(tk.Canvas):
    def __init__(self, master=None, images=None, pets=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)
        self.images = images
        self.pets = pets

        image_1 = self.create_image(
            544.0,
            309.0,
            image=self.images["image_1"]
        )

        image_2 = self.create_image(
            158.0,
            251.0,
            image=self.images["image_2"]
        )

        image_3 = self.create_image(
            372.0,
            72.0,
            image=self.images["image_3"]
        )

        favorites_button= Button(
            bg="#FFFFFF",
            image=self.images["button_3"],
            borderwidth=0,
            highlightthickness=0,
            # command=favorites_button_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )
        favorites_button.place(
            x=715.0,
            y=48.0,
            width=27.0,
            height=23.0
        )

        menu_button = Button(
            bg="#FFFFFF",
            image=self.images["button_4"],
            borderwidth=0,
            highlightthickness=0,
            # command=hamburger_menu_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )
        menu_button.place(
            x=750.0,
            y=49.0,
            width=19.0,
            height=22.0
        )

        # second menu button to be displayed when the first menu button is clicked
        close_hamburger_menu = Button(
            bg="#FFFFFF",
            image=self.images["button_4"],
            borderwidth=0,
            highlightthickness=0,
            # command=close_hamburger_menu_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )

        filter_button = Button(
            image=self.images["button_5"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("filter button clicked"),
            relief="flat"
        )
        filter_button.place(
            x=311.0,
            y=90.0,
            width=79.0,
            height=30.0
        )

        home_button = Button(
            bg="#F19FB5",
            image=self.images["button_6"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#F19FB5",
            # command=home_button_clicked,
        )
        home_button.place(
            x=95.0,
            y=155.0,
            width=120.0,
            height=30.0
        )

        register_button = Button(
            bg="#F19FB5",
            image=self.images["button_7"],
            borderwidth=0,
            highlightthickness=0,
            # command=register_button_clicked,
            relief="flat",
            activebackground="#F19FB5", 
        )
        register_button.place(
            x=95.0,
            y=204.0,
            width=120.0,
            height=30.0
        )

        donate_button = Button(
            bg="#F19FB5",
            image=self.images["button_8"],
            borderwidth=0,
            highlightthickness=0,
            # command=donate_button_clicked,
            relief="flat",
            activebackground="#F19FB5",
        )
        donate_button.place(
            x=95.0,
            y=253.0,
            width=120.0,
            height=30.0
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

        button_9 = Button(
            bg="#F19FB5",
            image=self.images["button_9"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat",
            activebackground="#F19FB5",
        )
        button_9.place(
            x=65.0,
            y=64.0,
            width=34.0,
            height=36.0
        )

        ekis_button = Button(
            bg="#FFFFFF",
            image=self.images["button_10"],
            borderwidth=0,
            highlightthickness=0,
            # command=ekis_button_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )
        ekis_button.place(
            x=621.0,
            y=123.0,
            width=42.0,
            height=43.0
        )

        pet_name  = self.create_text(
            582.0,
            176.0,
            anchor="nw",
            text="MILO, 1",
            fill="#000000",
            font=("Inter", 22 * -1, "bold")
        )

        pet_pic = self.create_image(
            448.0,
            307.0,
            image=self.pets["milo"]["picture"]
        )

        pet_desc = self.create_image(
            674.0,
            288.0,
            image=self.pets["milo"]["description"]
        )

        pet_quote = self.create_image(
            673.0,
            399.0,
            image=self.pets["milo"]["quote"]
        )

        pet_full_desc = self.create_image(
            664.0,
            309.0,
            image=self.pets["milo"]["full_desc"],
            state="hidden",
        )

        add_to_favorites_button = Button(
            bg="#FFFFFF",
            image=self.images["button_11"],
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: add_to_favorites_button_clicked(pets),
            relief="flat",
            activebackground="#FFFFFF",
        )
        add_to_favorites_button.place(
            x=669.0,
            y=123.0,
            width=43.0,
            height=44.0
        )

        description_button = Button(
            bg="#FFFFFF",
            image=self.images["button_12"],
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: description_button_clicked(pets),
            relief="flat",
            activebackground="#FFFFFF",
        )
        description_button.place(
            x=718.0,
            y=122.0,
            width=46.0,
            height=46.0
        )

        close_description_button = Button(
            bg="#FFFFFF",
            image=self.images["button_12"],
            borderwidth=0,
            highlightthickness=0,
            # command=close_description_button_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )

        adopt_button = Button(
            bg="#FFFFFF",
            image=self.images["button_13"],
            borderwidth=0,
            highlightthickness=0,
            # command=adopt_button_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )
        adopt_button.place(
            x=581.0,
            y=414.0,
            width=183.0,
            height=37.0
        )

        self.create_rectangle(
            215.0,
            151.99999378994107,
            229.83099189214408,
            187.3240229487419,
            fill="#F19FB5",
            outline="")

        self.create_rectangle(
            215.0,
            203.99999378994107,
            229.83099189214408,
            239.3240229487419,
            fill="#F19FB5",
            outline="")

        self.create_rectangle(
            216.0,
            253.99999378994107,
            230.83099189214408,
            289.3240229487419,
            fill="#F19FB5",
            outline="")


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