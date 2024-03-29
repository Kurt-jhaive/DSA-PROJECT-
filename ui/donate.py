import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Entry
import pandas as pd 
import asyncio
from threading import Thread
from FlappyPets.src.flappy import Flappy

class DonateFrame(tk.Canvas):
    def __init__(self, master=None, images=None):
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
            command=self.favorites_button_clicked,
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
            command=self.hamburger_menu_clicked,
            relief="flat"
        )
        hamburger_menu.place(
            x=749.0,
            y=42.0,
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

        self.display_name_canvas = self.create_text(
            105.0,
            66.0,
            anchor="nw",
            text="Marie Cris Edusma",
            fill="#FFFFFF",
            font=("Inter SemiBold", 14 * -1, "bold")
        )

        self.profile_location = self.create_text(
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
            image=self.images["button_5"],
            borderwidth=0,
            highlightthickness=0,
            command=self.register_button_clicked,
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

        flappy_pets_button = Button( 
            bg="#F19FB5",
            image = self.images["flappypets"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#F19FB5",
            command=self.flappy_pets_button_clicked
        )

        flappy_pets_button.place(
            x=95.0,
            y=302.0,
            width=120.0,
            height=30.0
        )

        button_7 = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["button_7"],
            borderwidth=0,
            highlightthickness=0,
            command=self.user_profile_button_clicked,
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
            command=self.submit_button_clicked,
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
        self.contactnumber_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.contactnumber_textbox.place(
            x=567.0,
            y=125.0,
            width=194.0,
            height=30
        )
        self.address_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.address_textbox.place(
            x=318.0,
            y=186.0,
            width=443.0,
            height=28
        )
        self.email_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.email_textbox.place(
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

        self.change_profile_display()

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
        self.contactnumber_textbox.lower()
        self.address_textbox.lower()
        self.email_textbox.lower()

        self.close_hamburger_menu.place(x=750.0, y=49.0, width=19.0, height=22.0)
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
        self.contactnumber_textbox.lift()
        self.address_textbox.lift()
        self.email_textbox.lift()
                
        self.close_hamburger_menu.place_forget()
        self.account_settings.place_forget()
        self.privacy_policy.place_forget()
        self.terms_conditions.place_forget()
        self.give_feedback.place_forget()
        self.log_out.place_forget()      
    
    def submit_button_clicked(self):
        self.main_app.show_donate_thankyou()
    
    def flappy_pets_button_clicked(self):
        print("Starting Flappy game...")
        flappy_thread = Thread(target=self.run_flappy_game)
        flappy_thread.start()

    def run_flappy_game(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        flappy_instance = Flappy()
        loop.run_until_complete(flappy_instance.start())

    def change_profile_display(self):
        #read the text file
        with open("data/current_user.txt", "r") as file:
            self.current_user = file.read().strip()
        
        #get the display name of the current user
        df = pd.read_csv("data/profile_data.csv")
        user_row = df[df['username'] == self.current_user]
        display_name = user_row['display_name'].values[0]
        display_location = user_row['address'].values[0]

        #change the display name and location
        self.itemconfigure(self.display_name_canvas, text=display_name)
        self.itemconfigure(self.profile_location, text=display_location)
