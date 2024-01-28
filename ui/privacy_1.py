import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Entry, Text
import pandas as pd

class PrivacyFrame1(tk.Canvas):
    def __init__(self, master=None, images=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)

        # To access the methods of the MainApp class
        self.main_app = master

        self.images = images

        image_1 = self.create_image(
            409.0,
            79.0,
            image=self.images["image_1"]
        )

        self.display_name_canvas = self.create_text(
            115.0,
            58.0,
            anchor="nw",
            text="Marie Cris Edusma",
            fill="#FFFFFF",
            font=("Inter SemiBold", 14 * -1, "bold")
        )

        self.profile_location = self.create_text(
            115.0,
            77.0,
            anchor="nw",
            text="Taguig City",
            fill="#FFFFFF",
            font=("Inter SemiBold", 12 * -1, "bold")
        )

        image_2 = self.create_image(
            404.0,
            145.0,
            image=self.images["image_2"]
        )

        user_button = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            command=self.user_profile_button_clicked,
            relief="flat"
        )
        user_button.place(
            x=65.0,
            y=55.0,
            width=44.103515625,
            height=43.0
        )

        back_button = Button(
            image=self.images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=self.back_button_clicked,
            relief="flat"
        )
        back_button.place(
            x=537.0,
            y=421.0,
            width=112.89242553710938,
            height=39.0
        )

        next_button = Button(
            image=self.images["button_3"],
            borderwidth=0,
            highlightthickness=0,
            command=self.next_button_clicked,
            relief="flat"
        )
        next_button.place(
            x=659.0,
            y=421.0,
            width=112.89242553710938,
            height=39.0
        )

        image_3 = self.create_image(
            400.0,
            206.0,
            image=self.images["image_3"]
        )

        image_4 = self.create_image(
            409.0,
            335.0,
            image=self.images["image_4"]
        )

        self.change_profile_display()

    def user_profile_button_clicked(self):
        pass

    def back_button_clicked(self):
        self.main_app.show_homepage()

    def next_button_clicked(self):
        self.main_app.show_privacy_2()

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
    
