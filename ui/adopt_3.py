import tkinter as tk
from tkinter import Button, Entry, Radiobutton, StringVar   

class AdoptFrame3(tk.Canvas):
    def __init__(self, master=None, images=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)
        self.images = images

        image_1 = self.create_image(
            225.0,
            128.0,
            image=self.images["image_1"]
        )

        image_2 = self.create_image(
            394.0,
            171.0,
            image=self.images["image_2"]
        )

        image_3 = self.create_image(
            394.0,
            264.0,
            image=self.images["image_3"]
        )

        image_4 = self.create_image(
            394.0,
            366.0,
            image=self.images["image_4"]
        )

        image_5 = self.create_image(
            253.0,
            53.0,
            image=self.images["image_5"]
        )

        image_7 = self.create_image(
            100.0,
            90.0,
            image=self.images["image_7"]
        )

        image_9 = self.create_image(
            215.0,
            90.0,
            image=self.images["image_9"]
        )

        image_10 = self.create_image(
            341.0,
            221.0,
            image=self.images["image_10"]
        )

        image_11 = self.create_image(
            341.0,
            323.0,
            image=self.images["image_11"]
        )


        back_button = Button(
            self,
            image=self.images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            # command=back_button_clicked,
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
            # command=next_button_clicked,
            relief="flat"
        )
        next_button.place(
            x=657.0,
            y=407.0,
            width=112.89242553710938,
            height=39.0
        )
        question1_textbox = Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        question1_textbox.place(
            x=62.0,
            y=157.0,
            width=665.0,
            height=31.0
        )
        question2_textbox = Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        question2_textbox.place(
            x=62.0,
            y=249.0,
            width=665.0,
            height=31.0
        )
        question3_textbox = Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        question3_textbox.place(
            x=62.0,
            y=351.0,
            width=665.0,
            height=31.0
        )

        # Are any members of your household allergic to animals? 
        q7 = StringVar()

        yes2_radio = Radiobutton(
            self,
            variable=q7,
            value='yes',
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            indicatoron=False,
            image=self.images["dot_image"],
            selectimage=self.images["pink_dot_image"],
        )
        yes2_radio.place(
            x=55,
            y=79
        )
        no2_radio = Radiobutton(
            self,
            variable=q7,
            value='no',
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            indicatoron=False,
            image=self.images["dot_image"],
            selectimage=self.images["pink_dot_image"],
        )
        no2_radio.place(
            x=173,
            y=79
        )


