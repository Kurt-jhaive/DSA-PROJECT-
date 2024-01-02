import tkinter as tk

class AdoptFrame1(tk.Canvas):
    def __init__(self, master=None, images=None):
        super().__init__(
            master,
            bg="#FFFFFF",
            height=500,
            width=820,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.images = images
        self.place(x=0, y=0)

        self.create_image(409.0, 79.0, image=self.images["image_1"])

        # Display Name Canvas
        display_name_canvas = self.create_text(
            115.0,
            58.0,
            anchor="nw",
            text="Marie Cris Edusma",
            fill="#FFFFFF",
            font=("Inter SemiBold", 14 * -1, "bold")
        )

        # Profile Location
        profile_location = self.create_text(
            115.0,
            77.0,
            anchor="nw",
            text="Taguig City",
            fill="#FFFFFF",
            font=("Inter SemiBold", 12 * -1, "bold")
        )

        button_1 = tk.Button(
            self,
            bg="#F19FB5",
            image=self.images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat",
            activebackground="#F19FB5",
        )
        button_1.place(x=65.0, y=55.0, width=44.103515625, height=43.0)

        self.create_image(425.0, 140.0, image=self.images["image_2"])

        self.create_image(111.0, 158.0, image=self.images["image_3"])

        back_button = tk.Button(
            self,
            image=self.images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=self.back_button_clicked,
            relief="flat"
        )
        back_button.place(x=535.0, y=407.0, width=112.89242553710938, height=39.0)

        next_button = tk.Button(
            self,
            image=self.images["button_3"],
            borderwidth=0,
            highlightthickness=0,
            command=self.next_button_clicked,
            relief="flat"
        )
        next_button.place(x=657.0, y=407.0, width=112.89242553710938, height=39.0)

        self.create_image(216.0, 435.0, image=self.images["image_4"])

        self.create_image(603.0, 367.0, image=self.images["image_5"])

        self.create_image(216.0, 367.0, image=self.images["image_6"])

        self.create_image(603.0, 295.0, image=self.images["image_7"])

        self.create_image(216.0, 295.0, image=self.images["image_8"])

        self.create_image(603.0, 221.0, image=self.images["image_9"])

        self.create_image(216.0, 221.0, image=self.images["image_10"])

        # tk.Entry widgets
        self.create_entry_widgets()

    def create_entry_widgets(self):
        entry_params = [
            (58.0, 216.0, 315.0),
            (445.0, 216.0, 315.0),
            (58.0, 289.0, 315.0),
            (445.0, 289.0, 315.0),
            (58.0, 359.0, 315.0),
            (445.0, 359.0, 315.0),
            (58.0, 429.0, 315.0),
        ]

        for x, y, width in entry_params:
            entry_widget = tk.Entry(
                self,
                font=("Inter", 15 * -1),
                bd=0,
                bg="#FFFFFF",
                fg="#000716",
                highlightthickness=0,
            )
            entry_widget.place(x=x, y=y, width=width, height=23)

    def back_button_clicked(self):
        print("Back button clicked")

    def next_button_clicked(self):
        print("Next button clicked")
    
    def hide_frame(self):
        self.place_forget()

    def show_frame(self):
        pass
        # self.place(x=0, y=0)

