import tkinter as tk
from tkinter import Button, Entry, Radiobutton, StringVar   

class AdoptFrame4(tk.Canvas):
    def __init__(self, master=None, images=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)

        # To access the methods of the MainApp class
        self.main_app = master

        self.images = images

        image_1 = self.create_image(
            289.0,
            139.0,
            image=self.images["image_1"]
        )

        image_2 = self.create_image(
            394.0,
            191.0,
            image=self.images["image_2"]
        )

        image_3 = self.create_image(
            394.0,
            98.0,
            image=self.images["image_3"]
        )

        image_4 = self.create_image(
            394.0,
            289.0,
            image=self.images["image_4"]
        )

        back_button = Button(
            self,
            image=self.images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            command=self.back_button_clicked,
            relief="flat"
        )
        back_button.place(
            x=535.0,
            y=407.0,
            width=112.89242553710938,
            height=39.0
        )

        next_button = Button(
            self,
            image=self.images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=self.next_button_clicked,
            relief="flat"
        )
        next_button.place(
            x=657.0,
            y=407.0,
            width=112.89242553710938,
            height=39.0
        )

        image_5 = self.create_image(
            319.0,
            54.0,
            image=self.images["image_5"]
        )

        image_6 = self.create_image(
            338.0,
            242.0,
            image=self.images["image_6"]
        )

        image_7 = self.create_image(
            285.0,
            348.0,
            image=self.images["image_7"]
        )

        image_8 = self.create_image(
            63.0,
            383.0,
            image=self.images["image_8"]
        )

        image_9 = self.create_image(
            102.0,
            386.0,
            image=self.images["image_9"]
        )

        image_10 = self.create_image(
            181.0,
            383.0,
            image=self.images["image_10"]
        )

        image_11 = self.create_image(
            216.0,
            386.0,
            image=self.images["image_11"]
        )
        question4_textbox = Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        question4_textbox.place(
            x=62.0,
            y=84.0,
            width=665.0,
            height=31.0
        )
        question5_textbox = Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        question5_textbox.place(
            x=62.0,
            y=177.0,
            width=665.0,
            height=31.0
        )
        question6_textbox = Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        question6_textbox.place(
            x=62.0,
            y=274.0,
            width=665.0,
            height=31.0
        )
        # Does everyone in the family support your decision to adopt a pet?
        q8 = StringVar() 

        yes3_radio = Radiobutton(
            self,
            variable=q8,
            value='yes',
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            indicatoron=False,
            image=self.images["dot_image"],
            selectimage=self.images["pink_dot_image"],
        )
        yes3_radio.place(
            x=55,
            y=375
        )
        no3_radio = Radiobutton(
            self,
            variable=q8,
            value='no',
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            indicatoron=False,
            image=self.images["dot_image"],
            selectimage=self.images["pink_dot_image"],
        )
        no3_radio.place(
            x=173,
            y=375
        )
    
    def back_button_clicked(self):
        self.main_app.show_adopt_3()
    
    def next_button_clicked(self):
        self.main_app.show_adopt_5()