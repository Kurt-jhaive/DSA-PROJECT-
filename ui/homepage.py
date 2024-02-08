import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Entry, messagebox
import random
import pandas as pd
import asyncio
from threading import Thread
from FlappyPets.src.flappy import Flappy

class HomepageFrame(tk.Canvas):
    def __init__(self, master=None, images=None, pets=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)

        # To access the methods of the MainApp class
        self.main_app = master

        self.images = images
        self.pets = pets
        self.favorites = []
        self.random_pet = None

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
            command=self.favorites_button_clicked,
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
            command=self.hamburger_menu_clicked,
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
        self.close_hamburger_menu = Button(
            bg="#FFFFFF",
            image=self.images["button_4"],
            borderwidth=0,
            highlightthickness=0,
            command=self.close_hamburger_menu_clicked,
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
            command=self.home_button_clicked,
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
            command=self.register_button_clicked,
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
            command=self.donate_button_clicked,
            relief="flat",
            activebackground="#F19FB5",
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

        button_9 = Button(
            bg="#F19FB5",
            image=self.images["button_9"],
            borderwidth=0,
            highlightthickness=0,
            command=self.user_profile_button_clicked,
            relief="flat",
            activebackground="#F19FB5",
        )
        button_9.place(
            x=65.0,
            y=64.0,
            width=34.0,
            height=36.0
        )

        self.ekis_button = Button(
            bg="#FFFFFF",
            image=self.images["button_10"],
            borderwidth=0,
            highlightthickness=0,
            command=self.ekis_button_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )
        self.ekis_button.place(
            x=621.0,
            y=123.0,
            width=42.0,
            height=43.0
        )

        self.pet_name  = self.create_text(
            582.0,
            176.0,
            anchor="nw",
            text="MILO, 1",
            fill="#000000",
            font=("Inter", 22 * -1, "bold")
        )

        self.pet_pic = self.create_image(
            448.0,
            307.0,
            image=self.pets["milo"]["picture"]
        )

        self.pet_desc = self.create_image(
            674.0,
            288.0,
            image=self.pets["milo"]["description"]
        )

        self.pet_quote = self.create_image(
            673.0,
            399.0,
            image=self.pets["milo"]["quote"]
        )

        self.pet_full_desc = self.create_image(
            664.0,
            309.0,
            image=self.pets["milo"]["full_desc"],
            state="hidden",
        )

        self.add_to_favorites_button = Button(
            bg="#FFFFFF",
            image=self.images["button_11"],
            borderwidth=0,
            highlightthickness=0,
            command=self.add_to_favorites_button_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )
        self.add_to_favorites_button.place(
            x=669.0,
            y=123.0,
            width=43.0,
            height=44.0
        )

        self.description_button = Button(
            bg="#FFFFFF",
            image=self.images["button_12"],
            borderwidth=0,
            highlightthickness=0,
            command=self.description_button_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )
        self.description_button.place(
            x=718.0,
            y=122.0,
            width=46.0,
            height=46.0
        )

        self.close_description_button = Button(
            bg="#FFFFFF",
            image=self.images["button_12"],
            borderwidth=0,
            highlightthickness=0,
            command=self.close_description_button_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )

        adopt_button = Button(
            bg="#FFFFFF",
            image=self.images["button_13"],
            borderwidth=0,
            highlightthickness=0,
            command=self.adopt_button_clicked,
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
            command=lambda: print("account_settings clicked"),
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
        # to change the pet every time the user clicks homepage button
        self.change_pet()

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
        self.ekis_button.lower()
        self.add_to_favorites_button.lower()
        self.description_button.lower()
        self.close_description_button.lower()

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
        self.ekis_button.lift()
        self.add_to_favorites_button.lift()
        self.description_button.lift()
        self.close_description_button.lift()
        
        self.close_hamburger_menu.place_forget()
        self.account_settings.place_forget()
        self.privacy_policy.place_forget()
        self.terms_conditions.place_forget()
        self.give_feedback.place_forget()
        self.log_out.place_forget()      

    def filter_button_clicked(self):
        # show the filter canvas on top of the homepage canvas
        pass
    
    def ekis_button_clicked(self):
        self.itemconfigure(self.pet_desc, state="normal")
        self.itemconfigure(self.pet_quote, state="normal")
        self.itemconfigure(self.pet_full_desc, state="hidden")
        self.close_description_button.place_forget()
        self.change_pet()

    def add_to_favorites_button_clicked(self):
        with open("data/favorites.txt", "r") as file:
            self.favorites = file.read().splitlines()
        
        if self.random_pet in self.favorites:
            messagebox.showinfo("Already added", "This pet is already in your favorites!")
            self.change_pet()
        else:
            self.favorites.append(self.random_pet)

            print("added to favorites", self.random_pet)
            print(self.favorites)

            with open("data/favorites.txt", "w") as file:
                for item in self.favorites:
                    file.write(item + '\n')

            self.change_pet()

    def description_button_clicked(self):
        full_desc = self.pets[self.random_pet]["full_desc"]   
        self.itemconfigure(self.pet_desc, state="hidden")
        self.itemconfigure(self.pet_quote, state="hidden")
        self.itemconfigure(self.pet_full_desc, image=full_desc, state="normal")
        self.close_description_button.place(x=718.0, y=122.0, width=46.0, height=46.0)

    def close_description_button_clicked(self):
        self.itemconfigure(self.pet_full_desc, state="hidden")
        self.itemconfigure(self.pet_desc, state="normal")
        self.itemconfigure(self.pet_quote, state="normal")
        self.close_description_button.place_forget()

    def adopt_button_clicked(self):
        self.main_app.show_adopt_1()

    def flappy_pets_button_clicked(self):
        print("Starting Flappy game...")
        flappy_thread = Thread(target=self.run_flappy_game)
        flappy_thread.start()

    def run_flappy_game(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        flappy_instance = Flappy()
        loop.run_until_complete(flappy_instance.start())

    def change_pet(self):
        if len(self.favorites) == len(self.pets):
            tk.messagebox.showinfo("No more pets", "You have seen all the pets!")
            return
        else:
            self.random_pet = random.choice(list(self.pets.keys()))
            while self.random_pet in self.favorites:
                self.random_pet = random.choice(list(self.pets.keys()))
            
            name = self.pets[self.random_pet]["name"]
            picture = self.pets[self.random_pet]["picture"]
            description = self.pets[self.random_pet]["description"]
            quote = self.pets[self.random_pet]["quote"]

            self.itemconfigure(self.pet_name, text=name)
            self.itemconfigure(self.pet_pic, image=picture)
            self.itemconfigure(self.pet_desc, image=description)
            self.itemconfigure(self.pet_quote, image=quote)
    
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