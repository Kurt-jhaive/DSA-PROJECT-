import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Entry, messagebox
import pandas as pd
import asyncio
from threading import Thread
from FlappyPets.src.flappy import Flappy

class FavoritesFrame(tk.Canvas):
    def __init__(self, master=None, images=None, pets=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)

        # To access the methods of the MainApp class
        self.main_app = master

        self.images = images
        self.pets = pets
        self.favorites = []

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

        self.rectangle_1 = self.create_image(
            540.0,
            147.0,
            image=self.images["pink_rectangle"],
            state="hidden"
        )
        self.rectangle_2 = self.create_image(
            540.0,
            242.0,
            image=self.images["pink_rectangle"],
            state="hidden"
        )
        self.rectangle_3 = self.create_image(
            540.0,
            335.0,
            image=self.images["pink_rectangle"],
            state="hidden"
        )

        self.adopt_button1 = Button(
            bg="#F8CBD7",
            activebackground="#F8CBD7",
            image=self.images["adopt_me"],
            borderwidth=0,
            highlightthickness=0,
            command=self.adopt_button_clicked,
            relief="flat"
        )
        self.adopt_button2 = Button(
            bg="#F8CBD7",
            activebackground="#F8CBD7",
            image=self.images["adopt_me"],
            borderwidth=0,
            highlightthickness=0,
            command=self.adopt_button_clicked,
            relief="flat"
        )
        self.adopt_button3 = Button(
            bg="#F8CBD7",
            activebackground="#F8CBD7",
            image=self.images["adopt_me"],
            borderwidth=0,
            highlightthickness=0,
            command=self.adopt_button_clicked,
            relief="flat"
        )

        self.pet1_name_canvas = self.create_text(
            393.0,
            122.0,
            anchor="nw",
            text="MILO, Male",
            fill="#AD206C",
            font=("Inter Bold", 16 * -1),
            state="hidden"
        )
        self.pet1_breed_canvas = self.create_text(
            393.0,
            138.0,
            anchor="nw",
            text="Aspin \n",
            fill="#000000",
            font=("Inter Bold", 16 * -1),
            state="hidden"
        )
        self.pet1_age_canvas = self.create_text(
            393.0,
            156.0,
            anchor="nw",
            text="2 year old",
            fill="#000000",
            font=("Inter SemiBold", 12 * -1),
            state="hidden"
        )

        self.pet2_name_canvas = self.create_text(
            393.0,
            215.0,
            anchor="nw",
            text="FIONA, Female",
            fill="#AD206C",
            font=("Inter Bold", 16 * -1),
            state="hidden"
        )
        self.pet2_breed_canvas = self.create_text(
            393.0,
            229.0,
            anchor="nw",
            text="Aspin \n",
            fill="#000000",
            font=("Inter Bold", 16 * -1),
            state="hidden"
        )
        self.pet2_age_canvas = self.create_text(
            393.0,
            248.0,
            anchor="nw",
            text=" 3½ year old ",
            fill="#000000",
            font=("Inter SemiBold", 12 * -1),
            state="hidden"
        )

        self.pet3_name_canvas = self.create_text(
            393.0,
            307.0,
            anchor="nw",
            text="LEVIS, Female",
            fill="#AD206C",
            font=("Inter Bold", 16 * -1),
            state="hidden"
        )
        self.pet3_breed_canvas = self.create_text(
            393.0,
            323.0,
            anchor="nw",
            text="Aspin \n",
            fill="#000000",
            font=("Inter Bold", 16 * -1),
            state="hidden"
        )
        self.pet3_age_canvas = self.create_text(
            393.0,
            341.0,
            anchor="nw",
            text="4 year old",
            fill="#000000",
            font=("Inter SemiBold", 12 * -1),
            state="hidden"
        )

        self.pet1_pic_canvas = self.create_image(
            350.0,
            146.0,
            image=self.images["milo"],
            state="hidden"
        )
        self.pet2_pic_canvas = self.create_image(
            350.0,
            242.0,
            image=self.images["milo"],
            state="hidden"
        )
        self.pet3_pic_canvas = self.create_image(
            350.0,
            335.0,
            image=self.images["milo"],
            state="hidden"
        )

        self.next_button = Button(
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

        self.change_profile_display()
        # to display the favorite pets
        self.copy_favorites_data()
        self.display_favorite_pet()

    def user_profile_button_clicked(self):
        pass
    
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
        self.adopt_button1.lower()
        self.adopt_button2.lower()
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
        self.adopt_button1.lift()
        self.adopt_button2.lift()
        
        self.close_hamburger_menu.place_forget()
        self.account_settings.place_forget()
        self.privacy_policy.place_forget()
        self.terms_conditions.place_forget()
        self.give_feedback.place_forget()
        self.log_out.place_forget()     

    def adopt_button_clicked(self):
        self.main_app.show_adopt_1()

    def next_button_clicked(self):
        self.delete_favorites()
        self.display_favorite_pet()

    def flappy_pets_button_clicked(self):
        print("Starting Flappy game...")
        flappy_thread = Thread(target=self.run_flappy_game)
        flappy_thread.start()

    def run_flappy_game(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        flappy_instance = Flappy()
        loop.run_until_complete(flappy_instance.start())

    def display_favorite_pet(self):
        # read the whole text file of the favorites
        with open("data/temp_favorites.txt", "r") as file:
            self.total_favorites = file.readlines()

        # if there are more than 3 favorites, show the next button
        if len(self.total_favorites) > 3:
            self.next_button.place(  
                x=656.0,
                y=405.0,
                width=112.89242553710938,
                height=39.0
            )
        if len(self.total_favorites) < 3:
            self.next_button.place_forget()

        # read the text file of the favorites and get the first 3 pets if there are 3 pets and below
        with open("data/temp_favorites.txt", "r") as file:
            if len(self.total_favorites) == 0:
                self.favorites = []
                messagebox.showinfo("No Favorites", "You have no favorites yet.")
            if len(self.total_favorites) == 1:
                self.favorites = [file.readline().strip() for _ in range(1)]
            elif len(self.total_favorites) == 2:
                self.favorites = [file.readline().strip() for _ in range(2)]
            elif len(self.total_favorites) > 2:
                self.favorites = [file.readline().strip() for _ in range(3)]

        if len(self.favorites) == 1:
            # show only the first pet
            first_pet = self.favorites[0].split(",")[0]
            name = self.pets[first_pet]["name"]
            breed = self.pets[first_pet]["breed"]
            age = self.pets[first_pet]["age"]
            picture = self.pets[first_pet]["picture"]
            gender = self.pets[first_pet]["gender"]

            self.itemconfigure(self.rectangle_1, state="normal")
            self.itemconfigure(self.pet1_name_canvas, text=f"{name}, {gender}", state="normal")
            self.itemconfigure(self.pet1_breed_canvas, text=breed, state="normal")
            self.itemconfigure(self.pet1_age_canvas, text=age, state="normal")
            self.itemconfigure(self.pet1_pic_canvas, image=picture, state="normal")
            self.adopt_button1.place(
                x=578.0,
                y=131.0,
                width=183.0,
                height=37.0
            )
            # hide the second and third pet
            self.itemconfigure(self.rectangle_2, state="hidden")
            self.itemconfigure(self.rectangle_3, state="hidden")
            self.itemconfigure(self.pet2_name_canvas, state="hidden")
            self.itemconfigure(self.pet2_breed_canvas, state="hidden")
            self.itemconfigure(self.pet2_age_canvas, state="hidden")
            self.itemconfigure(self.pet2_pic_canvas, state="hidden")
            self.itemconfigure(self.pet3_name_canvas, state="hidden")
            self.itemconfigure(self.pet3_breed_canvas, state="hidden")
            self.itemconfigure(self.pet3_age_canvas, state="hidden")
            self.itemconfigure(self.pet3_pic_canvas, state="hidden")
            self.adopt_button2.place_forget()
            self.adopt_button3.place_forget()
        elif len(self.favorites) == 2:
            # show the first pet and the second pet
            first_pet = self.favorites[0].split(",")[0]
            name = self.pets[first_pet]["name"]
            breed = self.pets[first_pet]["breed"]
            age = self.pets[first_pet]["age"]
            picture = self.pets[first_pet]["picture"]
            gender = self.pets[first_pet]["gender"]

            self.itemconfigure(self.rectangle_1, state="normal")
            self.itemconfigure(self.pet1_name_canvas, text=f"{name}, {gender}", state="normal")
            self.itemconfigure(self.pet1_breed_canvas, text=breed, state="normal")
            self.itemconfigure(self.pet1_age_canvas, text=age, state="normal")
            self.itemconfigure(self.pet1_pic_canvas, image=picture, state="normal")
            self.adopt_button1.place(
                x=578.0,
                y=131.0,
                width=183.0,
                height=37.0
            )

            second_pet = self.favorites[1].split(",")[0]
            name = self.pets[second_pet]["name"]
            breed = self.pets[second_pet]["breed"]
            age = self.pets[second_pet]["age"]
            picture = self.pets[second_pet]["picture"]
            gender = self.pets[second_pet]["gender"]

            self.itemconfigure(self.rectangle_1, state="normal")
            self.itemconfigure(self.rectangle_2, state="normal")
            self.itemconfigure(self.pet2_name_canvas, text=f"{name}, {gender}", state="normal")
            self.itemconfigure(self.pet2_breed_canvas, text=breed, state="normal")
            self.itemconfigure(self.pet2_age_canvas, text=age, state="normal")
            self.itemconfigure(self.pet2_pic_canvas, image=picture, state="normal")
            self.adopt_button2.place(
                x=578.0,
                y=225.0,
                width=183.0,
                height=37.0
            )

            # hide the third pet
            self.itemconfigure(self.rectangle_3, state="hidden")
            self.itemconfigure(self.pet3_name_canvas, state="hidden")
            self.itemconfigure(self.pet3_breed_canvas, state="hidden")
            self.itemconfigure(self.pet3_age_canvas, state="hidden")
            self.itemconfigure(self.pet3_pic_canvas, state="hidden")
            self.adopt_button3.place_forget()
        elif len(self.favorites) == 3:
            # show the first pet, second pet, and third pet
            first_pet = self.favorites[0].split(",")[0]
            name = self.pets[first_pet]["name"]
            breed = self.pets[first_pet]["breed"]
            age = self.pets[first_pet]["age"]
            picture = self.pets[first_pet]["picture"]
            gender = self.pets[first_pet]["gender"]

            self.itemconfigure(self.rectangle_1, state="normal")
            self.itemconfigure(self.pet1_name_canvas, text=f"{name}, {gender}", state="normal")
            self.itemconfigure(self.pet1_breed_canvas, text=breed, state="normal")
            self.itemconfigure(self.pet1_age_canvas, text=age, state="normal")
            self.itemconfigure(self.pet1_pic_canvas, image=picture, state="normal")
            self.adopt_button1.place(
                x=578.0,
                y=131.0,
                width=183.0,
                height=37.0
            )

            second_pet = self.favorites[1].split(",")[0]
            name = self.pets[second_pet]["name"]
            breed = self.pets[second_pet]["breed"]
            age = self.pets[second_pet]["age"]
            picture = self.pets[second_pet]["picture"]
            gender = self.pets[second_pet]["gender"]

            self.itemconfigure(self.rectangle_1, state="normal")
            self.itemconfigure(self.rectangle_2, state="normal")
            self.itemconfigure(self.pet2_name_canvas, text=f"{name}, {gender}", state="normal")
            self.itemconfigure(self.pet2_breed_canvas, text=breed, state="normal")
            self.itemconfigure(self.pet2_age_canvas, text=age, state="normal")
            self.itemconfigure(self.pet2_pic_canvas, image=picture, state="normal")
            self.adopt_button2.place(
                x=578.0,
                y=225.0,
                width=183.0,
                height=37.0
            )

            third_pet = self.favorites[2].split(",")[0]
            name = self.pets[third_pet]["name"]
            breed = self.pets[third_pet]["breed"]
            age = self.pets[third_pet]["age"]
            picture = self.pets[third_pet]["picture"]
            gender = self.pets[third_pet]["gender"]

            self.itemconfigure(self.rectangle_1, state="normal")
            self.itemconfigure(self.rectangle_2, state="normal")
            self.itemconfigure(self.rectangle_3, state="normal")
            self.itemconfigure(self.pet3_name_canvas, text=f"{name}, {gender}", state="normal")
            self.itemconfigure(self.pet3_breed_canvas, text=breed, state="normal")
            self.itemconfigure(self.pet3_age_canvas, text=age, state="normal")
            self.itemconfigure(self.pet3_pic_canvas, image=picture, state="normal")
            self.adopt_button3.place(
                x=578.0,
                y=316.0,
                width=183.0,
                height=37.0
            )
    
    def delete_favorites(self):
        with open("data/temp_favorites.txt", "r") as file:
            lines = file.readlines()

        new_lines = lines[3:]

        with open("data/temp_favorites.txt", "w") as file:
            file.writelines(new_lines)
    
    def copy_favorites_data(self):
        with open("data/favorites.txt", "r") as file:
            lines = file.readlines()
        with open("data/temp_favorites.txt", "w") as file:
            file.writelines(lines)
        
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
