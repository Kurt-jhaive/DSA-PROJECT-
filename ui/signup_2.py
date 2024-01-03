import tkinter as tk
from tkinter import Button, Entry, Radiobutton, StringVar, Text, Label

class SignupFrame2(tk.Canvas):
    def __init__(self, master=None, images=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)

        # To access the methods of the MainApp class
        self.main_app = master  

        self.images = images

        title_canvas = self.create_image(
            404.0,
            98.0,
            image=self.images["purrfect_image"]
        )

        loading_button = Button(
            image=self.images["loading_image"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        loading_button.place(
            x=259.5927734375,
            y=119.0,
            width=324.174560546875,
            height=7.0
        )

        text1 = self.create_text(
            273.0,
            231.0,
            anchor="nw",
            text="What purrfect name do you prefer to go by?",
            fill="#000000",
            font=("Inter SemiBold", 16 * -1)
        )

        text2 = self.create_text(
            275.0,
            338.0,
            anchor="nw",
            text="This is how your name will appear in the PurffectMatch",
            fill="#7C7C7C",
            font=("Inter", 12 * -1)
        )

        text3 = self.create_text(
            205.0,
            186.0,
            anchor="nw",
            text="HEY THERE, FUTURE PURR PARENTS!",
            fill="#000000",
            font=("Inter Bold", 24 * -1)
        )

        name_canvas = self.create_image(
            431.0,
            294.0,
            image=self.images["name_image"]
        )
        name_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="grey",
            highlightthickness=0,
        )
        name_textbox.place(
            x=202.0,
            y=280.0,
            width=457.0,
            height=29.0
        )

        # placeholder_text_1= "Your name"
        # name_textbox.insert(0, placeholder_text_1)
        # name_textbox.bind('<FocusIn>', lambda event: on_entry_click(event, name_textbox, placeholder_text_1))
        # name_textbox.bind('<FocusOut>', lambda event: on_focus_out(event, name_textbox, placeholder_text_1))

        back_button_1 = Button(
            bg="#FFFFFF",
            image=self.images["back_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.back_button_1_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )
        back_button_1.place(
            x=137.0,
            y=111.0,
            width=9.62713623046875,
            height=16.506439208984375
        )

        continue_button_1 = Button(
            image=self.images["continue_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.continue_button_1_clicked,
            relief="flat"
        )
        continue_button_1.place(
            x=343.0,
            y=387.0,
            width=159.0,
            height=39.0
        )

        # # ------------next page ----------------
        rectangle1 = self.create_rectangle(
            259.5927734375,
            119.0,
            583.767333984375,
            126.0,
            fill="#D9D9D9",
            outline="",
            state="hidden",
        )

        rectangle2 = self.create_rectangle(
            259.5927734375,
            119.0,
            480.36370849609375,
            126.0,
            fill="#F19FB5",
            outline="",
            state="hidden",
        )

        address_text1 = self.create_text(
            319.0,
            235.0,
            anchor="nw",
            text="Please enter your address?",
            fill="#000000",
            font=("Inter Bold", 16 * -1),
            state="hidden"
        )

        address_text2 = self.create_text(
            265.0,
            339.0,
            anchor="nw",
            text="This is how your address will appear in the PurffectMatch",
            fill="#969696",
            font=("Inter", 12 * -1),
            state="hidden"
        )

        address_text3 = self.create_text(
            330.0,
            195.0,
            anchor="nw",
            text="MEOW, MARIE!",
            fill="#000000",
            font=("Inter Bold", 24 * -1),
            state="hidden"
        )

        address_canvas = self.create_image(
            410.0,
            303.0,
            image=self.images["address_image"],
            state="hidden"
        )
        address_textbox = Entry(
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="grey",
            highlightthickness=0,
        )

        # placeholder_text_2= "Your address"
        # address_textbox.insert(0, placeholder_text_2)
        # address_textbox.bind('<FocusIn>', lambda event: on_entry_click(event, address_textbox, placeholder_text_2))
        # address_textbox.bind('<FocusOut>', lambda event: on_focus_out(event, address_textbox, placeholder_text_2))

        continue_button_2 = Button(
            image=self.images["continue_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.continue_button_2_clicked,
            relief="flat"
        )

        back_button_2 = Button(
            bg="#FFFFFF",
            image=self.images["back_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.back_button_2_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )

        # ------------last page ----------------
        loading_line_button_full = Button(
            image=self.images["loading_image_last"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )

        last_text_1 = self.create_text(
            331.0,
            222.0,
            anchor="nw",
            text="MEOW! ARF!",
            fill="#000000",
            font=("Inter Bold", 24 * -1),
            state="hidden"
        )

        last_text_2 = self.create_text(
            265.0,
            267.0,
            anchor="nw",
            text="Are you excited to find your perfect match?",
            fill="#000000",
            font=("Inter SemiBold", 16 * -1),
            state="hidden"
        )

        back_button_3 = Button(
            bg="#FFFFFF",
            image=self.images["back_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.back_button_3_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )

        yes_button = Button(
            image=self.images["yes_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.yes_button_clicked,
            relief="flat"
        )

    def back_button_1_clicked(self):
        self.main_app.show_signup_1()
    
    def continue_button_1_clicked(self):
        pass
        # add the functionality of going to the next form

    def back_button_2_clicked(self):
        pass 
        # add the functionality of going back to the previous form
    
    def continue_button_2_clicked(self):
        pass
        # add the functionality of going to the next form   
    
    def back_button_3_clicked(self):
        pass
        # add the functionality of going back to the previous form

    def yes_button_clicked(self):
        pass
        # add the functionality of going to the next form