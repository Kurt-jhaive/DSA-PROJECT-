import tkinter as tk
from tkinter import Button, Entry, Radiobutton, StringVar, Text, Label

class TermsFrame2(tk.Canvas):
    def __init__(self, master=None, images=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)

        # To access the methods of the MainApp class
        self.main_app = master

        self.images = images 

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

        agree_button = Button(
            image=self.images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=self.agree_button_clicked,
            relief="flat"
        )
        agree_button.place(
            x=659.0,
            y=421.0,
            width=112.89242553710938,
            height=39.0
        )

        image_1 = self.create_image(
            409.0,
            113.0,
            image=self.images["image_1"]
        )

        image_2 = self.create_image(
            408.0,
            304.0,
            image=self.images["image_2"]
        )

    def back_button_clicked(self):
        self.main_app.show_terms_1()

    def agree_button_clicked(self):
        self.main_app.show_homepage()
