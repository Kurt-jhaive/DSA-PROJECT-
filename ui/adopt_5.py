import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Label

class AdoptFrame5(tk.Canvas):
    def __init__(self, master=None, images=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)

        # To access the methods of the MainApp class
        self.main_app = master

        self.images = images

        image_1 = self.create_image(
            143.0,
            53.0,
            image=self.images["image_1"]
        )

        image_2 = self.create_image(
            63.0,
            91.0,
            image=self.images["image_2"]
        )

        image_3 = self.create_image(
            100.0,
            94.0,
            image=self.images["image_3"]
        )

        image_4 = self.create_image(
            181.0,
            91.0,
            image=self.images["image_4"]
        )

        image_5 = self.create_image(
            218.0,
            94.0,
            image=self.images["image_5"]
        )

        image_6 = self.create_image(
            458.0,
            53.0,
            image=self.images["image_6"]
        )

        image_7 = self.create_image(
            358.0,
            92.0,
            image=self.images["image_7"]
        )

        image_8 = self.create_image(
            398.0,
            95.0,
            image=self.images["image_8"]
        )

        image_9 = self.create_image(
            476.0,
            92.0,
            image=self.images["image_9"]
        )

        image_10 = self.create_image(
            510.0,
            95.0,
            image=self.images["image_10"]
        )

        image_11 = self.create_image(
            356.0,
            143.0,
            image=self.images["image_11"]
        )

        image_12 = self.create_image(
            371.0,
            324.0,
            image=self.images["image_12"]
        )

        image_13 = self.create_image(
            196.0,
            229.0,
            image=self.images["image_13"]
        )

        select_files_button = Button(
            self,
            image=self.images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            command=self.upload_image_button_clicked,
            relief="flat"
        )
        select_files_button.place(
            x=57.0,
            y=358.0,
            width=165.0,
            height=39.0
        )

        upload_label = Label(
            self,
            bg="#FFFFFF",
            fg="#000000",
            text="",
            font=("Inter", 12 * -1),
        )
        upload_label.place(
            x=232.0,
            y=358.0,
            width=165.0,
            height=39.0
        )

        back_button = Button(
            self,
            image=self.images["button_2"],
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
            image=self.images["button_3"],
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

        # Do you have other pets?
        q9 = StringVar() 

        dot_image = self.images["dot_image"]
        pink_dot_image = self.images["pink_dot_image"]

        yes4_radio = Radiobutton(
            self,
            variable=q9,
            value="yes",
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            indicatoron=False,
            image=dot_image,
            selectimage=pink_dot_image,
        )
        yes4_radio.place(
            x=55,
            y=83
        )

        no4_radio = Radiobutton(
            self,
            variable=q9,
            value="no",
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            indicatoron=False,
            image=dot_image,
            selectimage=pink_dot_image,
        )
        no4_radio.place(
            x=173,
            y=83
        )

        # Have you had pets in the past?
        q10 = StringVar()
        yes5_radio = Radiobutton(
            self,
            variable=q10,
            value="yes",
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            indicatoron=False,
            image=dot_image,
            selectimage=pink_dot_image,
        )
        yes5_radio.place(
            x=350,
            y=83
        )

        no5_radio = Radiobutton(
            self,
            variable=q10,
            value="no",
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            indicatoron=False,
            image=dot_image,
            selectimage=pink_dot_image,
        )
        no5_radio.place(
            x=468,
            y=83
        )

    def upload_image_button_clicked(self):
        pass
        # add the functionality of the upload image button here

    def back_button_clicked(self):
        self.main_app.show_adopt_4()

    def next_button_clicked(self):
        self.main_app.show_adopt_6()
