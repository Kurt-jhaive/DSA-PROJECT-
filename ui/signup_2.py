import tkinter as tk
from tkinter import Button, Entry, Radiobutton, StringVar, Text, Label
from data_handler import save_input, read_input, append_input   

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

        self.loading_button = Button(
            image=self.images["loading_image"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.loading_button.place(
            x=259.5927734375,
            y=119.0,
            width=324.174560546875,
            height=7.0
        )

        self.text1 = self.create_text(
            273.0,
            231.0,
            anchor="nw",
            text="What purrfect name do you prefer to go by?",
            fill="#000000",
            font=("Inter SemiBold", 16 * -1)
        )

        self.text2 = self.create_text(
            275.0,
            338.0,
            anchor="nw",
            text="This is how your name will appear in the PurffectMatch",
            fill="#7C7C7C",
            font=("Inter", 12 * -1)
        )

        self.text3 = self.create_text(
            205.0,
            186.0,
            anchor="nw",
            text="HEY THERE, FUTURE PURR PARENTS!",
            fill="#000000",
            font=("Inter Bold", 24 * -1)
        )

        self.name_canvas = self.create_image(
            431.0,
            294.0,
            image=self.images["name_image"]
        )
        self.name_textbox = Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="grey",
            highlightthickness=0,
        )
        self.name_textbox.place(
            x=202.0,
            y=280.0,
            width=457.0,
            height=29.0
        )

        # placeholder_text_1= "Your name"
        # self.name_textbox.insert(0, placeholder_text_1)
        # self.name_textbox.bind('<FocusIn>', lambda event: on_entry_click(event, self.name_textbox, placeholder_text_1))
        # self.name_textbox.bind('<FocusOut>', lambda event: on_focus_out(event, self.name_textbox, placeholder_text_1))

        self.back_button_1 = Button(
            bg="#FFFFFF",
            image=self.images["back_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.back_button_1_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )
        self.back_button_1.place(
            x=137.0,
            y=111.0,
            width=9.62713623046875,
            height=16.506439208984375
        )

        self.continue_button_1 = Button(
            image=self.images["continue_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.continue_button_1_clicked,
            relief="flat"
        )
        self.continue_button_1.place(
            x=343.0,
            y=387.0,
            width=159.0,
            height=39.0
        )

        # # ------------next page ----------------
        self.rectangle1 = self.create_rectangle(
            259.5927734375,
            119.0,
            583.767333984375,
            126.0,
            fill="#D9D9D9",
            outline="",
            state="hidden",
        )

        self.rectangle2 = self.create_rectangle(
            259.5927734375,
            119.0,
            480.36370849609375,
            126.0,
            fill="#F19FB5",
            outline="",
            state="hidden",
        )

        self.address_text1 = self.create_text(
            319.0,
            235.0,
            anchor="nw",
            text="Please enter your address?",
            fill="#000000",
            font=("Inter Bold", 16 * -1),
            state="hidden"
        )

        self.address_text2 = self.create_text(
            265.0,
            339.0,
            anchor="nw",
            text="This is how your address will appear in the PurffectMatch",
            fill="#969696",
            font=("Inter", 12 * -1),
            state="hidden"
        )

        self.address_text3 = self.create_text(
            330.0,
            195.0,
            anchor="nw",
            text="MEOW, MARIE!",
            fill="#000000",
            font=("Inter Bold", 24 * -1),
            state="hidden"
        )

        self.address_canvas = self.create_image(
            410.0,
            303.0,
            image=self.images["address_image"],
            state="hidden"
        )
        self.address_textbox = Entry(
            self,
            font=("Inter", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            fg="grey",
            highlightthickness=0,
        )

        # placeholder_text_2= "Your address"
        # self.address_textbox.insert(0, placeholder_text_2)
        # self.address_textbox.bind('<FocusIn>', lambda event: on_entry_click(event, self.address_textbox, placeholder_text_2))
        # self.address_textbox.bind('<FocusOut>', lambda event: on_focus_out(event, self.address_textbox, placeholder_text_2))

        self.continue_button_2 = Button(
            image=self.images["continue_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.continue_button_2_clicked,
            relief="flat"
        )

        self.back_button_2 = Button(
            bg="#FFFFFF",
            image=self.images["back_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.back_button_2_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )

        # ------------last page ----------------
        self.loading_line_button_full = Button(
            image=self.images["loading_image_last"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )

        self.last_text_1 = self.create_text(
            331.0,
            222.0,
            anchor="nw",
            text="MEOW! ARF!",
            fill="#000000",
            font=("Inter Bold", 24 * -1),
            state="hidden"
        )

        self.last_text_2 = self.create_text(
            265.0,
            267.0,
            anchor="nw",
            text="Are you excited to find your perfect match?",
            fill="#000000",
            font=("Inter SemiBold", 16 * -1),
            state="hidden"
        )

        self.back_button_3 = Button(
            bg="#FFFFFF",
            image=self.images["back_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.back_button_3_clicked,
            relief="flat",
            activebackground="#FFFFFF",
        )

        self.yes_button = Button(
            image=self.images["yes_image"],
            borderwidth=0,
            highlightthickness=0,
            command=self.yes_button_clicked,
            relief="flat"
        )

    def back_button_1_clicked(self):
        self.main_app.show_signup_1()
    
    def continue_button_1_clicked(self):
        self.itemconfigure(self.name_canvas, state="hidden")
        self.itemconfigure(self.text1, state="hidden")
        self.itemconfigure(self.text2, state="hidden")
        self.itemconfigure(self.text3, state="hidden")
        self.loading_button.place_forget()
        self.name_textbox.place_forget()
        self.continue_button_1.place_forget()

        #show next 
        self.itemconfigure(self.rectangle1, state="normal")
        self.itemconfigure(self.rectangle2, state="normal")
        self.itemconfigure(self.address_text1, state="normal")
        self.itemconfigure(self.address_text2, state="normal")
        self.itemconfigure(self.address_text3, state="normal")
        self.itemconfigure(self.address_canvas, state="normal")
        self.address_textbox.place(x=182.0, y=289.0, width=457.0, height=29.0)
        self.continue_button_2.place(x=343.0, y=387.0, width=159.0, height=39.0)
        self.back_button_2.place(x=137.0, y=111.0, width=9.62713623046875, height=16.5064697265625)

    def back_button_2_clicked(self):
        self.itemconfigure(self.rectangle1, state="hidden")
        self.itemconfigure(self.rectangle2, state="hidden")
        self.itemconfigure(self.address_text1, state="hidden")
        self.itemconfigure(self.address_text2, state="hidden")
        self.itemconfigure(self.address_text3, state="hidden")
        self.itemconfigure(self.address_canvas, state="hidden")
        self.address_textbox.place_forget()
        self.continue_button_2.place_forget()
        self.back_button_2.place_forget()

        #show previous
        self.itemconfigure(self.name_canvas, state="normal")
        self.itemconfigure(self.text1, state="normal")
        self.itemconfigure(self.text2, state="normal")
        self.itemconfigure(self.text3, state="normal")
        self.loading_button.place(x=259.5927734375, y=119.0, width=324.174560546875, height=7.0)
        self.name_textbox.place(x=202.0, y=280.0, width=457.0, height=29.0)
        self.continue_button_1.place(x=343.0, y=387.0, width=159.0, height=39.0)
        self.back_button_1.place(x=137.0, y=111.0, width=9.62713623046875, height=16.506439208984375)

    def continue_button_2_clicked(self):
        self.itemconfigure(self.rectangle1, state="hidden")
        self.itemconfigure(self.rectangle2, state="hidden")
        self.itemconfigure(self.address_text1, state="hidden")
        self.itemconfigure(self.address_text2, state="hidden")
        self.itemconfigure(self.address_text3, state="hidden")
        self.itemconfigure(self.address_canvas, state="hidden")
        self.address_textbox.place_forget()
        self.continue_button_2.place_forget()

    #show next
        self.itemconfigure(self.last_text_1, state="normal")
        self.itemconfigure(self.last_text_2, state="normal")
        self.loading_line_button_full.place(x=259.5927734375, y=119.0, width=324.4072265625, height=7.0)
        self.yes_button.place(x=327.0, y=355.0, width=159.0, height=39.0)
        self.back_button_3.place(x=137.0, y=111.0, width=9.62713623046875, height=16.5064697265625)

    def back_button_3_clicked(self):
        self.itemconfigure(self.last_text_1, state="hidden")
        self.itemconfigure(self.last_text_2, state="hidden")
        self.loading_line_button_full.place_forget()
        self.yes_button.place_forget()
        self.back_button_3.place_forget()

    #show previous
        self.itemconfigure(self.rectangle1, state="normal")
        self.itemconfigure(self.rectangle2, state="normal")
        self.itemconfigure(self.address_text1, state="normal")
        self.itemconfigure(self.address_text2, state="normal")
        self.itemconfigure(self.address_text3, state="normal")
        self.itemconfigure(self.address_canvas, state="normal")
        self.address_textbox.place(x=182.0, y=289.0, width=457.0, height=29.0)
        self.continue_button_2.place(x=343.0, y=387.0, width=159.0, height=39.0)
        self.back_button_2.place(x=137.0, y=111.0, width=9.62713623046875, height=16.5064697265625)

    def yes_button_clicked(self):
        if not(self.name_textbox.get() and self.address_textbox.get()):
            tk.messagebox.showinfo("Error", "Please fill up all the fields.")
        else:
            self.append_input_data()
            self.main_app.show_login()

    def append_input_data(self):
        append_input(self)

