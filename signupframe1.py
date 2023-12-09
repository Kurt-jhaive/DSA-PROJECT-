from tkinter import *
from tkinter import messagebox
from pathlib import Path
import subprocess
from pathlib import Path


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\signup1_resources\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def sign_up1_back_button_clicked():
    window.withdraw()
    subprocess.Popen(["python", "loginframe.py"])

def sign_up1_next_button_clicked():
    window.withdraw()
    subprocess.Popen(["python", "signupframe2.py"])
def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

# def persistent_input():
#     # check if there is a file called "inputs/login_input.csv"
#     if os.path.exists("inputs/login_input.csv"):
#         # if there is, then read the file using pandas
#         df = pd.read_csv("inputs/login_input.csv")
#         # get the last username and password from the csv file
#         last_username = df['username'].values[-1]
#         last_password = df['password'].values[-1]
#         # put the last username and password into the textboxes
#         username_textbox.insert(0, last_username)
#         password_textbox.insert(0, last_password)
#     else:
#         # get the username and password from the inputted textboxes
#         inputted_username = username_textbox.get()
#         inputted_password = password_textbox.get()

#         # put the username and password into the csv file using pandas
#         df = pd.DataFrame({
#             "username": [inputted_username],
#             "password": [inputted_password]
#         })
#         df.to_csv("inputs/login_input.csv", index=False)

window = Tk()

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the protocol for the window close event
window.protocol("WM_DELETE_WINDOW", close_window)

# Calculate the x and y coordinates for the window to be centered
x = (screen_width - 820) // 2
y = (screen_height - 500) // 2

window.geometry(f"820x500+{x}+{y}")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 820,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    190.0,
    250.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    183.0,
    237.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    594.0,
    395.33442878723145,
    image=entry_image_1
)
password_signup = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
password_signup.place(
    x=419.0,
    y=383.0,
    width=353.0,
    height=34
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    594.0,
    320.66865730285645,
    image=entry_image_2
)
user_name_signup  = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
user_name_signup.place(
    x=419.0,
    y=309.0,
    width=353.0,
    height=34
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    594.0,
    253.52588653564453,
    image=entry_image_3
)
last_name_signup= Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
last_name_signup.place(
    x=419.0,
    y=241.0,
    width=353.0,
    height=34
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    594.0,
    186.0,
    image=entry_image_4
)
middle_name_signup = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
middle_name_signup.place(
    x=419.0,
    y=174.0,
    width=353.0,
    height=34.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    594.0,
    118.70454406738281,
    image=entry_image_5
)
first_name_signup  = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
first_name_signup.place(
    x=419.0,
    y=106.0,
    width=353.0,
    height=34.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
next_button1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up1_next_button_clicked,
    relief="flat"
)
next_button1.place(
    x=665.0,
    y=441.0,
    width=112.89242553710938,
    height=39.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
back_button1 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up1_back_button_clicked,
    relief="flat"
)
back_button1.place(
    x=410.0,
    y=441.0,
    width=112.8924560546875,
    height=39.0
)

canvas.create_text(
    410.0,
    49.0,
    anchor="nw",
    text="Sign Up ",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
