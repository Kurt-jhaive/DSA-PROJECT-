import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Entry

class AdoptFrame6(tk.Canvas):
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
            x=535.0,
            y=407.0,
            width=112.89242553710938,
            height=39.0
        )

        submit_button = Button(
            bg="#FFFFFF",
            image=self.images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=self.submit_button_clicked,
            relief="flat"
        )
        submit_button.place(
            x=657.0,
            y=407.0,
            width=125.0,
            height=39.0
        )

        image_1 = self.create_image(
            328.0,
            59.0,
            image=self.images["image_1"]
        )

        image_2 = self.create_image(
            174.0,
            92.0,
            image=self.images["image_2"]
        )

        image_3 = self.create_image(
            174.0,
            190.0,
            image=self.images["image_3"]
        )

        button_3 = Button(
            bg="#FFFFFF",
            image=self.images["button_3"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#FFFFFF",    
        )
        button_3.place(
            x=56.0,
            y=121.0,
            width=338.0,
            height=50.0
        )

        button_4 = Button(
            bg="#FFFFFF",
            image=self.images["button_4"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#FFFFFF",
        )
        button_4.place(
            x=55.0,
            y=213.0,
            width=338.0,
            height=50.0
        )

        image_4 = self.create_image(
            267.0,
            292.0,
            image=self.images["image_4"]
        )

        image_5 = self.create_image(
            64.0,
            324.0,
            image=self.images["image_5"]
        )

        image_6 = self.create_image(
            103.0,
            327.0,
            image=self.images["image_6"]
        )

        image_7 = self.create_image(
            182.0,
            324.0,
            image=self.images["image_7"]
        )

        image_8 = self.create_image(
            216.0,
            327.0,
            image=self.images["image_8"]
        )
        date_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        date_textbox.place(
            x=62.0,
            y=137.0,
            width=317.0,
            height=28.0
        )
        time_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        time_textbox.place(
            x=67.0,
            y=230.0,
            width=317.0,
            height=28.0
        )


        # Will you be able to visit the shelter for the meet-and-greet?
        q11 = StringVar()

        yes6_radio = Radiobutton(
            variable=q11,
            value='yes',
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            indicatoron=False,
            image=self.images["dot_image"],
            selectimage=self.images["pink_dot_image"],
        )
        yes6_radio.place(
            x=56,
            y=316
        )
        no6_radio = Radiobutton(
            variable=q11,
            value='no',
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            indicatoron=False,
            image=self.images["dot_image"],
            selectimage=self.images["pink_dot_image"],
        )
        no6_radio.place(
            x=174,
            y=316
        )

    def back_button_clicked(self):
        self.main_app.show_adopt_5()
    
    def submit_button_clicked(self):
        self.main_app.show_adopt_thankyou()
    
