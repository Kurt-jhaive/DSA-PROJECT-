import tkinter as tk
from tkinter import Button, Entry, Radiobutton, StringVar, Text, Label

class AdoptThankyouFrame(tk.Canvas):
    def __init__(self, master=None, images=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)

        # To access the methods of the MainApp class
        self.main_app = master  

        self.images = images 

        image_1 = self.create_image(
            409.0,
            252.0,
            image=self.images["image_1"]
        )

        continue_button = Button(
            bg="#F19FB5",
            activebackground="#F19FB5",
            image=self.images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            command=self.continue_button_clicked,
            relief="flat"
        )
        continue_button.place(
            x=318.0,
            y=378.0,
            width=183.0,
            height=37.0
        )
    
    def continue_button_clicked(self):
        self.main_app.show_homepage()