import tkinter as tk

class AdoptFrame2(tk.Canvas):
    def __init__(self, master=None, images=None):
        super().__init__(master, bg="#FFFFFF", height=500, width=820, bd=0, highlightthickness=0, relief="ridge")
        self.images = images
        self.place(x=0, y=0)

        # ------------------------- questionnaire title ------------------------- #
        image_21 = self.create_image(126.0, 47.0, image=self.images["image_21"])

        # ------------------------- first question ------------------------- #
        image_14 = self.create_image(76.0, 82.0, image=self.images["image_14"])
        image_15 = self.create_image(108.0, 124.0, image=self.images["image_15"])
        image_17 = self.create_image(200.0, 122.0, image=self.images["image_17"])
        image_19 = self.create_image(299.0, 122.0, image=self.images["image_19"])

        # ------------------------- second question ------------------------- #
        image_1 = self.create_image(227.0, 161.0, image=self.images["image_1"])
        image_3 = self.create_image(114.0, 196.0, image=self.images["image_3"])
        image_5 = self.create_image(233.0, 196.0, image=self.images["image_5"])
        image_7 = self.create_image(359.0, 196.0, image=self.images["image_7"])
        image_9 = self.create_image(481.0, 198.0, image=self.images["image_9"])
        image_11 = self.create_image(603.0, 196.0, image=self.images["image_11"])
        image_13 = self.create_image(711.0, 196.0, image=self.images["image_13"])

        # ------------------------- third question ------------------------- #
        image_22 = self.create_image(182.0, 237.0, image=self.images["image_22"])
        image_24 = self.create_image(123.0, 273.0, image=self.images["image_24"])
        image_26 = self.create_image(226.0, 273.0, image=self.images["image_26"])
        image_28 = self.create_image(327.0, 273.0, image=self.images["image_28"])
        image_30 = self.create_image(451.0, 273.0, image=self.images["image_30"])

        # ------------------------- fourth question ------------------------- #
        image_31 = self.create_image(614.0, 237.0, image=self.images["image_31"])
        image_33 = self.create_image(615.0, 273.0, image=self.images["image_33"])
        image_35 = self.create_image(723.0, 273.0, image=self.images["image_35"])

        # ------------------------- fifth question ------------------------- #
        image_36 = self.create_image(132.0, 321.0, image=self.images["image_36"])
        image_38 = self.create_image(124.0, 358.0, image=self.images["image_38"])
        image_40 = self.create_image(228.0, 358.0, image=self.images["image_40"])
        image_42 = self.create_image(337.0, 357.0, image=self.images["image_42"])
        image_44 = self.create_image(456.0, 357.0, image=self.images["image_44"])
        image_46 = self.create_image(602.0, 357.0, image=self.images["image_46"])

        # ------------------------- sixth question ------------------------- #
        image_51 = self.create_image(117.0, 399.0, image=self.images["image_51"])
        image_48 = self.create_image(146.0, 438.0, image=self.images["image_48"])
        image_50 = self.create_image(325.0, 438.0, image=self.images["image_50"])

        back_button = tk.Button(image=self.images["button_1"], borderwidth=0, highlightthickness=0, command=self.back_button_clicked, relief="flat")
        back_button.place(x=535.0, y=407.0, width=112.89242553710938, height=39.0)

        next_button = tk.Button(image=self.images["button_2"], borderwidth=0, highlightthickness=0, command=self.next_button_clicked, relief="flat")
        next_button.place(x=657.0, y=407.0, width=112.89242553710938, height=39.0)

        # # ------------------------- RADIO BUTTONS ------------------------- #
        # STATUS
        q1 = tk.StringVar()
        single_radio = tk.Radiobutton(self, variable=q1, value='single', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        single_radio.place(x=54, y=111)

        married_radio = tk.Radiobutton(self, variable=q1, value='married', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        married_radio.place(x=141, y=111)

        others_radio = tk.Radiobutton(self, variable=q1, value='others', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        others_radio.place(x=245, y=111)

        # What prompted you to adopt from PAWS?
        q2 = tk.StringVar()
        friends_radio = tk.Radiobutton(self, variable=q2, value='friends', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        friends_radio.place(x=54, y=185)

        website_radio = tk.Radiobutton(self, variable=q2, value='website', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        website_radio.place(x=173, y=185)

        social_radio = tk.Radiobutton(self, variable=q2, value='social', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        social_radio.place(x=284, y=185)

        family_radio = tk.Radiobutton(self, variable=q2, value='family', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        family_radio.place(x=427, y=185)

        partner_radio = tk.Radiobutton(self, variable=q2, value='partner', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        partner_radio.place(x=545, y=185)

        others2_radio = tk.Radiobutton(self, variable=q2, value='others', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        others2_radio.place(x=656, y=185)

        # What type of building do you live in?
        q3 = tk.StringVar()
        apartment_radio = tk.Radiobutton(self, variable=q3, value='apartment', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        apartment_radio.place(x=54, y=262)

        house_radio = tk.Radiobutton(self, variable=q3, value='house', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        house_radio.place(x=172, y=262)

        condo_radio = tk.Radiobutton(self, variable=q3, value='condo', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        condo_radio.place(x=272, y=262)

        others3_radio = tk.Radiobutton(self, variable=q3, value='others', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        others3_radio.place(x=396, y=262)

        # Do you rent?
        q4 = tk.StringVar()
        yes_radio = tk.Radiobutton(self, variable=q4, value='yes', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        yes_radio.place(x=570, y=262)

        no_radio = tk.Radiobutton(self, variable=q4, value='no', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        no_radio.place(x=681, y=262)

        #Who do you live with?
        q5 = tk.StringVar()
        alone_radio = tk.Radiobutton(self, variable=q5, value='alone', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        alone_radio.place(x=54, y=346)

        spouse_radio = tk.Radiobutton(self, variable=q5, value='spouse', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        spouse_radio.place(x=173, y=346)

        relatives_radio = tk.Radiobutton(self, variable=q5, value='relatives', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        relatives_radio.place(x=273, y=346)

        parents_radio = tk.Radiobutton(self, variable=q5, value='parents', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        parents_radio.place(x=397, y=346)

        roommate_radio = tk.Radiobutton(self, variable=q5, value='roommate', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        roommate_radio.place(x=525, y=346)

        # How old are they?
        q6 = tk.StringVar()
        below_radio = tk.Radiobutton(self, variable=q6, value='below 18', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        below_radio.place(x=54, y=427)

        over_radio = tk.Radiobutton(self, variable=q6, value='over 18', bg="#FFFFFF", activebackground="#FFFFFF", bd=0, indicatoron=False, image=self.images["dot_image"], selectimage=self.images["pink_dot_image"])
        over_radio.place(x=237, y=427)

    def back_button_clicked(self):
        print("back button clicked")

    def next_button_clicked(self):
        print("next button clicked")

    def hide_frame(self):
        print("hide adopt2 frame")

        # hide all the widgets
        for widget in self.winfo_children():
            widget.place_forget()
        
        # hide the radio buttons
        
        self.place_forget()
