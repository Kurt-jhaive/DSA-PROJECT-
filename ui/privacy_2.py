import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Entry, Text

class PrivacyFrame2(tk.Canvas):
    def __init__(self, master=None, images=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)
        self.images = images

        image_1 = self.create_image(
            408.0,
            129.0,
            image=self.images["image_1"]
        )

        image_2 = self.create_image(
            409.0,
            306.0,
            image=self.images["image_2"]
        )

        back_button = Button(
            image=self.images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            # command=back_button_clicked,
            relief="flat"
        )
        back_button.place(
            x=537.0,
            y=421.0,
            width=112.89242553710938,
            height=39.0
        )

        next_button = Button(
            image=self.images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            # command=next_button_clicked,
            relief="flat"
        )
        next_button.place(
            x=659.0,
            y=421.0,
            width=112.89242553710938,
            height=39.0
        )
