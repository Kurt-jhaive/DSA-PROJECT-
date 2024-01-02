import tkinter as tk
from tkinter import Button, Entry, Radiobutton, StringVar, Text, Label

class DonateThankyouFrame(tk.Canvas):
    def __init__(self, master=None, images=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)
        self.images = images 

        image_1 = self.create_image(
            409.0,
            252.0,
            image=images["image_1"]
        )

        continue_button = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            # command=continue_button_clicked,
            relief="flat"
        )
        continue_button.place(
            x=318.0,
            y=376.0,
            width=174.0,
            height=37.0
        )