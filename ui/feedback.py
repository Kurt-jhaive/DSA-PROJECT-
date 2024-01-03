import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Entry, Text

class FeedbackFrame(tk.Canvas):
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

        display_name_canvas = self.create_text(
            115.0,
            59.0,
            anchor="nw",
            text="Marie Cris Edusma",
            fill="#FFFFFF",
            font=("Inter SemiBold", 14 * -1, "bold")
        )

        profile_location = self.create_text(
            115.0,
            77.0,
            anchor="nw",
            text="Taguig City",
            fill="#FFFFFF",
            font=("Inter SemiBold", 12 * -1, "bold")
        )

        user_button = Button(
            bg = "#F19FB5",
            activebackground= "#F19FB5",
            image=self.images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("user_button clicked"),
            relief="flat"
        )
        user_button.place(
            x=65.0,
            y=55.0,
            width=44.103515625,
            height=43.0
        )

        image_2 = self.create_image(
            412.0,
            145.0,
            image=self.images["image_2"]    
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

        submit_button = Button(
            image=self.images["button_3"],
            borderwidth=0,
            highlightthickness=0,
            command=self.submit_button_clicked,
            relief="flat"
        )
        submit_button.place(
            x=659.0,
            y=421.0,
            width=112.89242553710938,
            height=39.0
        )

        image_3 = self.create_image(
            407.0,
            321.0,
            image=self.images["image_3"]
        )


        feedback_textbox = Text(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            font=("Inter", 12 * -1)
        )
        feedback_textbox.place(
            x=80.0,
            y=275.0,
            width=655.0,
            height=101.0
        )

        filled_star_image = self.images["filled_star"]
        unfilled_star_image = self.images["unfilled_star"]

        # ------------------------------ star buttons ------------------------------
        unfilled_star_button1 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=unfilled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.unfilled_star_button1_clicked,
            relief="flat"
        )
        unfilled_star_button1.place(
            x=289.0,
            y=176.0,
            width=40.0,
            height=41.0
        )
        filled_star_button1 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=filled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.filled_star_button1_clicked,
            relief="flat"
        )

        unfilled_star_button2 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=unfilled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.unfilled_star_button2_clicked,
            relief="flat"
        )
        unfilled_star_button2.place(
            x=335.0,
            y=176.0,
            width=40.0,
            height=41.0
        )
        filled_star_button2 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=filled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.filled_star_button2_clicked,
            relief="flat"
        )

        unfilled_star_button3 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=unfilled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.unfilled_star_button3_clicked,
            relief="flat"
        )
        unfilled_star_button3.place(
            x=382.0,
            y=176.0,
            width=39.0,
            height=41.0
        )
        filled_star_button3 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=filled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.filled_star_button3_clicked,
            relief="flat"
        )

        unfilled_star_button4 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=unfilled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.unfilled_star_button4_clicked,
            relief="flat"
        )
        unfilled_star_button4.place(
            x=427.0,
            y=176.0,
            width=40.0,
            height=41.0
        )
        filled_star_button4 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=filled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.filled_star_button4_clicked,
            relief="flat"
        )

        unfilled_star_button5 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=unfilled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.unfilled_star_button5_clicked,
            relief="flat"
        )
        unfilled_star_button5.place(
            x=474.0,
            y=176.0,
            width=40.0,
            height=41.0
        )
        filled_star_button5 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=filled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.filled_star_button5_clicked,
            relief="flat"
        )

    def back_button_clicked(self):
        self.main_app.show_homepage()

    def submit_button_clicked(self):
        # add the functionality of the submit button here
        self.main_app.show_homepage()
