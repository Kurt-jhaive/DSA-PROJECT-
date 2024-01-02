import tkinter as tk
from ui.login import LoginFrame
from ui.adopt_1 import AdoptFrame1
from ui.adopt_2 import AdoptFrame2
from ui.adopt_3 import AdoptFrame3
from ui.adopt_4 import AdoptFrame4
from ui.adopt_5 import AdoptFrame5
from ui.adopt_6 import AdoptFrame6
from ui.donate import DonateFrame
from ui.favorites import FavoritesFrame
from ui.feedback import FeedbackFrame
from ui.forgetpass import ForgetPassFrame
from ui.homepage import HomepageFrame
from ui.privacy_1 import PrivacyFrame1
from ui.privacy_2 import PrivacyFrame2
from ui.privacy_3 import PrivacyFrame3
from ui.register import RegisterFrame
from ui.signup_1 import SignupFrame1
from ui.signup_2 import SignupFrame2
from ui.terms_1 import TermsFrame1
from ui.terms_2 import TermsFrame2
from ui.adopt_thankyou import AdoptThankyouFrame
from ui.donate_thankyou import DonateThankyouFrame
from ui.signup_thankyou import SignupThankyouFrame
from image_loader import *

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        x = (self.winfo_screenwidth() - 820) // 2
        y = (self.winfo_screenheight() - 500) // 2

        self.title("Main App")
        self.geometry(f"820x500+{x}+{y}")
        self.resizable(False, False)

        self.current_frame = None  # Initialize current_frame attribute

        # Set the protocol for the window close event
        self.protocol("WM_DELETE_WINDOW", self.destroy_window)
        
        self.login = LoginFrame(self, homepage=self.show_homepage, signup=self.show_signup_1, forget_pass=self.show_forgetpass, images=load_login_images())
        self.login.grid(row=0, column=0)


    def destroy_window(self):
        if tk.messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.destroy()

    def change_display(self, frame_class):
        # Destroy the current frame if exists
        if self.current_frame:
            self.current_frame.destroy()

        # Create and display the new frame
        if frame_class == AdoptFrame1:
            self.current_frame = frame_class(self, images=load_adopt_images())
        elif frame_class == AdoptFrame2:
            self.current_frame = frame_class(self, images=load_adopt_2_images())
        elif frame_class == AdoptFrame3:
            self.current_frame = frame_class(self, images=load_adopt_3_images())
        elif frame_class == AdoptFrame4:
            self.current_frame = frame_class(self, images=load_adopt_4_images())
        elif frame_class == AdoptFrame5:
            self.current_frame = frame_class(self, images=load_adopt_5_images())
        elif frame_class == AdoptFrame6:
            self.current_frame = frame_class(self, images=load_adopt_6_images())
        elif frame_class == DonateFrame:
            self.current_frame = frame_class(self, images=load_donate_images())
        elif frame_class == FavoritesFrame:
            self.current_frame = frame_class(self, images=load_favorites_images(), pets=load_pets())
        elif frame_class == FeedbackFrame:
            self.current_frame = frame_class(self, images=load_feedback_images())
        elif frame_class == ForgetPassFrame:
            self.current_frame = frame_class(self, images=load_forgetpass_images())
        elif frame_class == HomepageFrame:
            self.current_frame = frame_class(self, images=load_homepage_images())
        elif frame_class == PrivacyFrame1:
            self.current_frame = frame_class(self, images=load_privacy_1_images())
        elif frame_class == PrivacyFrame2:
            self.current_frame = frame_class(self, images=load_privacy_2_images())
        elif frame_class == PrivacyFrame3:
            self.current_frame = frame_class(self, images=load_privacy_3_images())
        elif frame_class == RegisterFrame:
            self.current_frame = frame_class(self, images=load_register_images())
        elif frame_class == SignupFrame1:   
            self.current_frame = frame_class(self, images=load_signup_1_images())
        elif frame_class == SignupFrame2:
            self.current_frame = frame_class(self, images=load_signup_2_images())
        elif frame_class == TermsFrame1:
            self.current_frame = frame_class(self, images=load_terms_1_images())
        elif frame_class == TermsFrame2:
            self.current_frame = frame_class(self, images=load_terms_2_images())
        elif frame_class == AdoptThankyouFrame:
            self.current_frame = frame_class(self, images=load_adopt_thankyou_images())
        elif frame_class == DonateThankyouFrame:
            self.current_frame = frame_class(self, images=load_donate_thankyou_images())
        elif frame_class == SignupThankyouFrame:
            self.current_frame = frame_class(self, images=load_signup_thankyou_images())
        else:
            self.current_frame = frame_class(self)

        self.current_frame.grid(row=0, column=0)

    def show_login(self):
        self.change_display(LoginFrame)

    def show_adopt_1(self):
        self.change_display(AdoptFrame1)

    def show_adopt_2(self):
        self.change_display(AdoptFrame2)

    def show_adopt_3(self):
        self.change_display(AdoptFrame3)
    
    def show_adopt_4(self):
        self.change_display(AdoptFrame4)
    
    def show_adopt_5(self):
        self.change_display(AdoptFrame5)

    def show_adopt_6(self):
        self.change_display(AdoptFrame6)

    def show_donate(self):
        self.change_display(DonateFrame)

    def show_favorites(self):
        self.change_display(FavoritesFrame)
    
    def show_feedback(self):
        self.change_display(FeedbackFrame)
    
    def show_forgetpass(self):
        self.change_display(ForgetPassFrame)
    
    def show_homepage(self):
        self.change_display(HomepageFrame)
    
    def show_privacy_1(self):
        self.change_display(PrivacyFrame1)

    def show_privacy_2(self):
        self.change_display(PrivacyFrame2)
    
    def show_privacy_3(self):
        self.change_display(PrivacyFrame3)
    
    def show_register(self):
        self.change_display(RegisterFrame)
    
    def show_signup_1(self):
        self.change_display(SignupFrame1)
    
    def show_signup_2(self):
        self.change_display(SignupFrame2)
    
    def show_terms_1(self):
        self.change_display(TermsFrame1)
    
    def show_terms_2(self):
        self.change_display(TermsFrame2)
    
    def show_adopt_thankyou(self):
        self.change_display(AdoptThankyouFrame)
    
    def show_donate_thankyou(self):
        self.change_display(DonateThankyouFrame)

    def show_signup_thankyou(self):
        self.change_display(SignupThankyouFrame)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

