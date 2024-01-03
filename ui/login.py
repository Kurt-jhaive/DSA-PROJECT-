import tkinter as tk
from tkinter import messagebox
import pandas as pd
from function_helper import resource_path

class LoginFrame(tk.Canvas):
    def __init__(self, master=None, images=None):
        super().__init__(master, width=820, height=500, bg="#FFFFFF", bd=0, highlightthickness=0, relief="ridge")
        self.place(x=0, y=0)

        # To access the methods of the MainApp class
        self.main_app = master
        
        self.images = images

        self.create_image(190.0, 250.0, image=self.images["image_1"])
        self.create_image(179.0, 221.0, image=self.images["image_2"])

        self.create_text(410.0, 48.0, anchor="nw", text="Login", fill="#000000", font=("Inter SemiBold", 20 * -1))

        self.login_button = tk.Button(self, image=self.images["button_1"], borderwidth=0, highlightthickness=0, command=self.login_button_clicked, relief="flat")
        self.login_button.place(x=410.0, y=326.0, width=159.0, height=39.0)

        self.forgot_password_button = tk.Button(self, bg="#FFFFFF", image=self.images["button_2"], borderwidth=0, highlightthickness=0, command=self.forgot_password_button_clicked, relief="flat", activebackground="#FFFFFF")
        self.forgot_password_button.place(x=658.0, y=267.00010681152344, width=161.62887573242188, height=34.91102600097656)

        entry_bg_1 = self.create_image(592.5, 223.27298736572266, image=self.images["entry_1"])
        self.username_textbox = tk.Entry(self, font=("Inter", 15 * -1), bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.username_textbox.place(x=421.0, y=131.973876953125, width=344.0, height=36.59822082519531)

        entry_bg_2 = self.create_image(592.5, 141.29910278320312, image=self.images["entry_2"])
        self.password_textbox = tk.Entry(self, font=("Inter", 15 * -1), bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, show='*')
        self.password_textbox.place(x=421.0, y=213.0, width=344.0, height=36.59820556640625)

        self.sign_up_button = tk.Button(self, image=self.images["button_3"], borderwidth=0, highlightthickness=0, command=self.sign_up_button_clicked, relief="flat")
        self.sign_up_button.place(x=616.0, y=326.0, width=159.0, height=39.0)

    def login_button_clicked(self):
        entered_username = self.username_textbox.get()
        entered_password = self.password_textbox.get()

        df = pd.read_csv(resource_path("data/profile_data.csv"))    
        user_record = df[(df['username'] == entered_username) & (df['password'] == entered_password)]

        if not user_record.empty:
            # Put the username in a text file
            with open(resource_path("data/current_user.txt"), "w") as file:
                file.write(entered_username)
            messagebox.showinfo("Login Successful", f"Welcome, {entered_username}!")
            self.main_app.show_homepage()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
            #just to test if it works
            self.main_app.show_homepage()

    def sign_up_button_clicked(self):
        self.main_app.show_signup_1()

    def forgot_password_button_clicked(self):
        self.main_app.show_forgetpass()

