import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Entry

class FavoritesFrame(tk.Canvas):
    def __init__(self, master=None, images=None, pets=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)

        # To access the methods of the MainApp class
        self.main_app = master

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
            command=self.favorites_button_clicked,
            relief="flat"
        )
        favorites_button.place(
            x=705.0,
            y=44.0,
            width=37.0,
            height=35.0
        )

        hamburger_menu = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=self.images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=self.hamburger_menu_clicked,
            relief="flat"
        )
        hamburger_menu.place(
            x=749.0,
            y=45.0,
            width=23.0,
            height=35.0
        )
        self.close_hamburger_menu = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=self.images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=self.close_hamburger_menu_clicked,
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
            command=self.home_button_clicked,
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
            command=self.register_button_clicked,
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
            command=self.donate_button_clicked,
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
            command=self.user_profile_button_clicked,
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
            command=self.adopt_button_clicked,
            relief="flat"
        )
        adopt_button2 = Button(
            bg="#F8CBD7",
            activebackground="#F8CBD7",
            image=self.images["adopt_me"],
            borderwidth=0,
            highlightthickness=0,
            command=self.adopt_button_clicked,
            relief="flat"
        )
        adopt_button3 = Button(
            bg="#F8CBD7",
            activebackground="#F8CBD7",
            image=self.images["adopt_me"],
            borderwidth=0,
            highlightthickness=0,
            command=self.adopt_button_clicked,
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
            command=self.next_button_clicked,
            relief="flat"
        )

        #----------------------- Hamburger Menu------------------
        # HAMBURGER FRAME
        self.pink_menu_rectangle_canvas = self.create_image(
            654.0,
            194.0,
            image=self.images["pink_menu_rectangle"],    
            state="hidden",
        )

        self.account_settings = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["account"],
            borderwidth=0,
            highlightthickness=0,
            command=self.account_settings_button_clicked,
            relief="flat"
        )

        self.privacy_policy = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["privacy"],
            borderwidth=0,
            highlightthickness=0,
            command=self.privacy_button_clicked,
            relief="flat"
        )

        self.terms_conditions = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["terms"],
            borderwidth=0,
            highlightthickness=0,
            command=self.terms_button_clicked,
            relief="flat"
        )

        self.give_feedback = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["feedback"],
            borderwidth=0,
            highlightthickness=0,
            command=self.feedback_button_clicked,
            relief="flat"
        )

        self.log_out = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["logout"],
            borderwidth=0,
            highlightthickness=0,
            command=self.log_out_button_clicked,
            relief="flat"
        )

    def user_profile_button_clicked(self):
        pass
        # self.main_app.show_user_profile()
    
    def home_button_clicked(self):
        self.main_app.show_homepage()

    def register_button_clicked(self):
        self.main_app.show_register()

    def donate_button_clicked(self):
        self.main_app.show_donate()
    
    def favorites_button_clicked(self):
        self.main_app.show_favorites()
    
    # ----------------------- Hamburger Menu Functions------------------
    def hamburger_menu_clicked(self):
        # show the hamburger menu
        self.itemconfigure(self.pink_menu_rectangle_canvas, state="normal")

        self.close_hamburger_menu.place(x=749.0, y=45.0, width=23.0, height=35.0)
        # x=749.0,
        #     y=45.0,
        #     width=23.0,   original is 19 22
        #     height=35.0
        # )
        self.account_settings.place(x=549.0, y=96.0, width=205.0, height=30.0)
        self.privacy_policy.place(x=550.0, y=133.0, width=203.99925231933594, height=32.0)
        self.terms_conditions.place(x=549.0, y=173.0, width=205.0, height=29.0)
        self.give_feedback.place(x=551.0, y=212.0, width=202.0, height=32.291259765625)
        self.log_out.place(x=550.0, y=256.0, width=204.0, height=31.0)

    def account_settings_button_clicked(self):
        pass

    def privacy_button_clicked(self):
        self.main_app.show_privacy_1()

    def terms_button_clicked(self):
        self.main_app.show_terms_1()

    def feedback_button_clicked(self):
        self.main_app.show_feedback()
    
    def log_out_button_clicked(self):
        self.main_app.show_login()
    
    def close_hamburger_menu_clicked(self): 
        # hide the hamburger menu
        self.itemconfigure(self.pink_menu_rectangle_canvas, state="hidden")
        
        self.close_hamburger_menu.place_forget()
        self.account_settings.place_forget()
        self.privacy_policy.place_forget()
        self.terms_conditions.place_forget()
        self.give_feedback.place_forget()
        self.log_out.place_forget()     

    def adopt_button_clicked(self):
        self.main_app.show_adopt_1()

    def next_button_clicked(self):
        self.main_app.show_favorites_2()