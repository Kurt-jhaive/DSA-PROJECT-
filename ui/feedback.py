import tkinter as tk
from tkinter import Button, Radiobutton, StringVar, Entry, Text, messagebox
import pandas as pd

class FeedbackFrame(tk.Canvas):
    def __init__(self, master=None, images=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)

        # To access the methods of the MainApp class
        self.main_app = master
        
        self.images = images
        self.ratings = None

        image_1 = self.create_image(
            409.0,
            79.0,
            image=self.images["image_1"]
        )

        self.display_name_canvas = self.create_text(
            115.0,
            59.0,
            anchor="nw",
            text="Marie Cris Edusma",
            fill="#FFFFFF",
            font=("Inter SemiBold", 14 * -1, "bold")
        )

        self.profile_location = self.create_text(
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


        self.feedback_textbox = Text(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            font=("Inter", 12 * -1)
        )
        self.feedback_textbox.place(
            x=80.0,
            y=275.0,
            width=655.0,
            height=101.0
        )

        filled_star_image = self.images["filled_star"]
        unfilled_star_image = self.images["unfilled_star"]

        # ------------------------------ star buttons ------------------------------
        self.unfilled_star_button1 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=unfilled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.unfilled_star_button1_clicked,
            relief="flat"
        )
        self.unfilled_star_button1.place(
            x=289.0,
            y=176.0,
            width=40.0,
            height=41.0
        )
        self.filled_star_button1 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=filled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.filled_star_button1_clicked,
            relief="flat"
        )

        self.unfilled_star_button2 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=unfilled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.unfilled_star_button2_clicked,
            relief="flat"
        )
        self.unfilled_star_button2.place(
            x=335.0,
            y=176.0,
            width=40.0,
            height=41.0
        )
        self.filled_star_button2 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=filled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.filled_star_button2_clicked,
            relief="flat"
        )

        self.unfilled_star_button3 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=unfilled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.unfilled_star_button3_clicked,
            relief="flat"
        )
        self.unfilled_star_button3.place(
            x=382.0,
            y=176.0,
            width=39.0,
            height=41.0
        )
        self.filled_star_button3 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=filled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.filled_star_button3_clicked,
            relief="flat"
        )

        self.unfilled_star_button4 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=unfilled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.unfilled_star_button4_clicked,
            relief="flat"
        )
        self.unfilled_star_button4.place(
            x=427.0,
            y=176.0,
            width=40.0,
            height=41.0
        )
        self.filled_star_button4 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=filled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.filled_star_button4_clicked,
            relief="flat"
        )

        self.unfilled_star_button5 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=unfilled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.unfilled_star_button5_clicked,
            relief="flat"
        )
        self.unfilled_star_button5.place(
            x=474.0,
            y=176.0,
            width=40.0,
            height=41.0
        )
        self.filled_star_button5 = Button(
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            image=filled_star_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.filled_star_button5_clicked,
            relief="flat"
        )

        self.change_profile_display()

    def unfilled_star_button1_clicked(self):
        self.ratings = 1
        print(self.ratings)
        self.unfilled_star_button1.place_forget()
        self.filled_star_button1.place(x=289.0, y=176.0, width=40.0, height=41.0)

    def filled_star_button1_clicked(self):
        self.ratings = 0
        print(self.ratings)
        self.filled_star_button1.place_forget()
        self.filled_star_button2.place_forget()
        self.filled_star_button3.place_forget()
        self.filled_star_button4.place_forget()
        self.filled_star_button5.place_forget()
        self.unfilled_star_button1.place(x=289.0, y=176.0, width=40.0, height=41.0)
        self.unfilled_star_button2.place(x=335.0, y=176.0, width=40.0, height=41.0)
        self.unfilled_star_button3.place(x=382.0, y=176.0, width=39.0, height=41.0)
        self.unfilled_star_button4.place(x=427.0, y=176.0, width=40.0, height=41.0)
        self.unfilled_star_button5.place(x=474.0, y=176.0, width=40.0, height=41.0)

    def unfilled_star_button2_clicked(self):
        self.ratings = 2
        print(self.ratings)
        self.unfilled_star_button2.place_forget()
        self.filled_star_button1.place(x=289.0, y=176.0, width=40.0, height=41.0)
        self.filled_star_button2.place(x=335.0, y=176.0, width=40.0, height=41.0)

    def filled_star_button2_clicked(self):
        self.ratings = 1
        print(self.ratings)
        self.filled_star_button2.place_forget()
        self.filled_star_button3.place_forget()
        self.filled_star_button4.place_forget()
        self.filled_star_button5.place_forget()
        self.unfilled_star_button2.place(x=335.0, y=176.0, width=40.0, height=41.0)
        self.unfilled_star_button3.place(x=382.0, y=176.0, width=39.0, height=41.0)
        self.unfilled_star_button4.place(x=427.0, y=176.0, width=40.0, height=41.0)
        self.unfilled_star_button5.place(x=474.0, y=176.0, width=40.0, height=41.0)

    def unfilled_star_button3_clicked(self):
        self.ratings = 3
        print(self.ratings)
        self.unfilled_star_button3.place_forget()
        self.filled_star_button1.place(x=289.0, y=176.0, width=40.0, height=41.0)
        self.filled_star_button2.place(x=335.0, y=176.0, width=40.0, height=41.0)
        self.filled_star_button3.place(x=382.0, y=176.0, width=39.0, height=41.0)

    def filled_star_button3_clicked(self):
        self.ratings = 2
        print(self.ratings)
        self.filled_star_button3.place_forget()
        self.filled_star_button4.place_forget()
        self.filled_star_button5.place_forget()
        self.unfilled_star_button3.place(x=382.0, y=176.0, width=39.0, height=41.0)
        self.unfilled_star_button4.place(x=427.0, y=176.0, width=40.0, height=41.0)
        self.unfilled_star_button5.place(x=474.0, y=176.0, width=40.0, height=41.0)

    def unfilled_star_button4_clicked(self):
        self.ratings = 4
        print(self.ratings)
        self.unfilled_star_button4.place_forget()
        self.filled_star_button1.place(x=289.0, y=176.0, width=40.0, height=41.0)
        self.filled_star_button2.place(x=335.0, y=176.0, width=40.0, height=41.0)
        self.filled_star_button3.place(x=382.0, y=176.0, width=39.0, height=41.0)
        self.filled_star_button4.place(x=427.0, y=176.0, width=40.0, height=41.0)

    def filled_star_button4_clicked(self):
        self.ratings = 3
        print(self.ratings)
        self.filled_star_button4.place_forget()
        self.filled_star_button5.place_forget()
        self.unfilled_star_button4.place(x=427.0, y=176.0, width=40.0, height=41.0)
        self.unfilled_star_button5.place(x=474.0, y=176.0, width=40.0, height=41.0)

    def unfilled_star_button5_clicked(self):
        self.ratings = 5
        print(self.ratings)
        self.unfilled_star_button5.place_forget()
        self.filled_star_button1.place(x=289.0, y=176.0, width=40.0, height=41.0)
        self.filled_star_button2.place(x=335.0, y=176.0, width=40.0, height=41.0)
        self.filled_star_button3.place(x=382.0, y=176.0, width=39.0, height=41.0)
        self.filled_star_button4.place(x=427.0, y=176.0, width=40.0, height=41.0)
        self.filled_star_button5.place(x=474.0, y=176.0, width=40.0, height=41.0)

    def filled_star_button5_clicked(self):
        self.ratings = 4
        print(self.ratings)
        self.filled_star_button5.place_forget()
        self.unfilled_star_button5.place(x=474.0, y=176.0, width=40.0, height=41.0)

    def back_button_clicked(self):
        self.main_app.show_homepage()

    def submit_button_clicked(self):
        if self.ratings is None or self.feedback_textbox.get("1.0", tk.END).strip() == "":
            messagebox.showerror("Error", "Please rate and provide feedback before submitting.")
        else:
            if self.save_input():
                messagebox.showinfo("Success", "Feedback submitted!")
                self.main_app.show_homepage()
        
    def save_input(self):
        feedback = self.feedback_textbox.get("1.0", tk.END).strip()
        with open("data/current_user.txt", "r") as file:
            current_user = file.read().strip()
        pd.read_csv("data/feedback_data.csv")

        data = pd.DataFrame({
            "username": [current_user],
            "star_ratings": [self.ratings],
            "feedback": [feedback],
        })

        data.to_csv("data/feedback_data.csv", index=False, mode="a", header=False)
        return True

    def change_profile_display(self):
        #read the text file
        with open("data/current_user.txt", "r") as file:
            self.current_user = file.read().strip()
        
        #get the display name of the current user
        df = pd.read_csv("data/profile_data.csv")
        user_row = df[df['username'] == self.current_user]
        display_name = user_row['display_name'].values[0]
        display_location = user_row['address'].values[0]

        #change the display name and location
        self.itemconfigure(self.display_name_canvas, text=display_name)
        self.itemconfigure(self.profile_location, text=display_location)
