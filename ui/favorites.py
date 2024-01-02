import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Entry

class FavoritesFrame(tk.Canvas):
    def __init__(self, master=None, images=None, pets=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)
        self.images = images

        image_1 = self.create_image(
            158.0,
            251.0,  
            image=self.images["image_1"]
        )

        image_2 = self.create_image(
            369.0,
            72.0,
            image=self.images["image_2"]
        )

        favorites_button = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=self.images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            # command=favorites_button_clicked,
            relief="flat"
        )
        favorites_button.place(
            x=705.0,
            y=46.0,
            width=37.0,
            height=35.0
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
            y=45.0,
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
            # command=register_button_clicked,
            relief="flat"
        )
        register_button.place(
            x=92.0,
            y=204.0,
            width=127.0,
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
            x=93.0,
            y=253.0,
            width=127.0,
            height=30.0
        )

        user_button = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["button_6"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("user_button clicked"),
            relief="flat"
        )
        user_button.place(
            x=65.0,
            y=64.0,
            width=34.0,
            height=36.0
        )

        rectangle_1 = self.create_image(
            540.0,
            147.0,
            image=self.images["pink_rectangle"],
            state="hidden"
        )
        rectangle_2 = self.create_image(
            540.0,
            242.0,
            image=self.images["pink_rectangle"],
            state="hidden"
        )
        rectangle_3 = self.create_image(
            540.0,
            335.0,
            image=self.images["pink_rectangle"],
            state="hidden"
        )

        adopt_button1 = Button(
            bg="#F8CBD7",
            activebackground="#F8CBD7",
            image=self.images["adopt_me"],
            borderwidth=0,
            highlightthickness=0,
            # command=adopt_button_clicked,
            relief="flat"
        )
        adopt_button2 = Button(
            bg="#F8CBD7",
            activebackground="#F8CBD7",
            image=self.images["adopt_me"],
            borderwidth=0,
            highlightthickness=0,
            # command=adopt_button_clicked,
            relief="flat"
        )
        adopt_button3 = Button(
            bg="#F8CBD7",
            activebackground="#F8CBD7",
            image=self.images["adopt_me"],
            borderwidth=0,
            highlightthickness=0,
            # command=adopt_button_clicked,
            relief="flat"
        )

        pet1_name_canvas = self.create_text(
            393.0,
            122.0,
            anchor="nw",
            text="MILO, Male",
            fill="#AD206C",
            font=("Inter Bold", 16 * -1),
            state="hidden"
        )
        pet1_breed_canvas = self.create_text(
            393.0,
            138.0,
            anchor="nw",
            text="Aspin \n",
            fill="#000000",
            font=("Inter Bold", 16 * -1),
            state="hidden"
        )
        pet1_age_canvas = self.create_text(
            393.0,
            156.0,
            anchor="nw",
            text="2 year old",
            fill="#000000",
            font=("Inter SemiBold", 12 * -1),
            state="hidden"
        )

        pet2_name_canvas = self.create_text(
            393.0,
            215.0,
            anchor="nw",
            text="FIONA, Female",
            fill="#AD206C",
            font=("Inter Bold", 16 * -1),
            state="hidden"
        )
        pet2_breed_canvas = self.create_text(
            393.0,
            229.0,
            anchor="nw",
            text="Aspin \n",
            fill="#000000",
            font=("Inter Bold", 16 * -1),
            state="hidden"
        )
        pet2_age_canvas = self.create_text(
            393.0,
            248.0,
            anchor="nw",
            text=" 3½ year old ",
            fill="#000000",
            font=("Inter SemiBold", 12 * -1),
            state="hidden"
        )

        pet3_name_canvas = self.create_text(
            393.0,
            307.0,
            anchor="nw",
            text="LEVIS, Female",
            fill="#AD206C",
            font=("Inter Bold", 16 * -1),
            state="hidden"
        )
        pet3_breed_canvas = self.create_text(
            393.0,
            323.0,
            anchor="nw",
            text="Aspin \n",
            fill="#000000",
            font=("Inter Bold", 16 * -1),
            state="hidden"
        )
        pet3_age_canvas = self.create_text(
            393.0,
            341.0,
            anchor="nw",
            text="4 year old",
            fill="#000000",
            font=("Inter SemiBold", 12 * -1),
            state="hidden"
        )

        pet1_pic_canvas = self.create_image(
            350.0,
            146.0,
            image=self.images["milo"],
            state="hidden"
        )
        pet2_pic_canvas = self.create_image(
            350.0,
            242.0,
            image=self.images["milo"],
            state="hidden"
        )
        pet3_pic_canvas = self.create_image(
            350.0,
            335.0,
            image=self.images["milo"],
            state="hidden"
        )

        next_button = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=self.images["button_10"],
            borderwidth=0,
            highlightthickness=0,
            # command=next_button_clicked,
            relief="flat"
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