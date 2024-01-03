import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Entry, Text

class PrivacyFrame3(tk.Canvas):
    def __init__(self, master=None, images=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)

        # To access the methods of the MainApp class
        self.main_app = master

        self.images = images

        image_1 = self.create_image(
            409.0,
            129.0,
            image=self.images["image_1"]
        )

        image_2 = self.create_image(
            407.0,
            287.0,
            image=self.images["image_2"]    
        )

        back_button = Button(
            image=self.images["button_1"],
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

        submit_button = Button(
            image=self.images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=self.i_agree_button_clicked,
            relief="flat"
        )
        submit_button.place(
            x=659.0,
            y=421.0,
            width=112.89242553710938,
            height=39.0
        )

        image_3 = self.create_image(
            423.0,
            380.0,
            image=self.images["image_3"]
        )
    
    def back_button_clicked(self):
        self.main_app.show_privacy_2()
    
    def i_agree_button_clicked(self):
        self.main_app.show_homepage()