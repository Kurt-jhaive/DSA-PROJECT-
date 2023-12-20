from tkinter import *
from tkinter import messagebox, filedialog
import subprocess
import os
import shutil
import sys


from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\adoption5_frame")

new_file_path = None

# ---------------------------- PATH ------------------------------- #
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def back_button_clicked():
    window.destroy()
    subprocess.Popen(["adoptframe4/adoptframe4.exe"])
def next_button_clicked():
    if save_input():
        window.destroy()
        subprocess.Popen(["adoptframe6/adoptframe6.exe"])

def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

def save_input():
    if not all([q9.get(), q10.get()]):
        messagebox.showerror("Error", "Please fill up all fields.")
        return False
    else:
        messagebox.showinfo("Success", "Please proceed to the next set of questions.")
        inputs = [q9.get(), q10.get()]
        with open(resource_path("../../_internal/data/adopt5_data.txt"), "w") as f:
            f.write('\n'.join(inputs) + '\n')
            f.write(new_file_path + '\n')
        return True
    
def read_input():
    # read the inputted data from the file and display it
    try:
        with open(resource_path("../../_internal/data/adopt5_data.txt"), "r") as f:
            q9.set(f.readline().strip())
            q10.set(f.readline().strip())
            upload_label.configure(text=f.readline().strip())
    except FileNotFoundError:
        with open(resource_path("../../_internal/data/adopt5_data.txt"), "w") as f:
            pass
    
def upload_image_button_clicked():
    global new_file_path
    file_path = filedialog.askopenfilename()

    if file_path:
        # Create a new folder called "uploads" if it doesn't exist
        if not os.path.exists("uploads"):
            os.mkdir("uploads")
            os.system("cd uploads && mkdir adopt_application_images")

        # Get the filename of the selected image
        filename = os.path.basename(file_path)

        # Create a new path to store the image in the "uploads" folder
        new_file_path = os.path.join("uploads/adopt_application_images", filename)

        # Copy the image to the "uploads" folder
        shutil.copy(file_path, new_file_path)

        upload_label.configure(text=f"{filename}")


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
    file=relative_to_assets(resource_path("forms/adoption5_frame/image_1.png")))
image_1 = canvas.create_image(
    143.0,
    53.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption5_frame/image_2.png")))
image_2 = canvas.create_image(
    63.0,
    91.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption5_frame/image_3.png")))
image_3 = canvas.create_image(
    100.0,
    94.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption5_frame/image_4.png")))
image_4 = canvas.create_image(
    181.0,
    91.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption5_frame/image_5.png")))
image_5 = canvas.create_image(
    218.0,
    94.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption5_frame/image_6.png")))
image_6 = canvas.create_image(
    458.0,
    53.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption5_frame/image_7.png")))
image_7 = canvas.create_image(
    358.0,
    92.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption5_frame/image_8.png")))
image_8 = canvas.create_image(
    398.0,
    95.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption5_frame/image_9.png")))
image_9 = canvas.create_image(
    476.0,
    92.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption5_frame/image_10.png")))
image_10 = canvas.create_image(
    510.0,
    95.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption5_frame/image_11.png")))
image_11 = canvas.create_image(
    356.0,
    143.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption5_frame/image_12.png")))
image_12 = canvas.create_image(
    371.0,
    324.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption5_frame/image_13.png")))
image_13 = canvas.create_image(
    196.0,
    229.0,
    image=image_image_13
)

button_image_1 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption5_frame/button_1.png")))
select_files_button= Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=upload_image_button_clicked,
    relief="flat"
)
select_files_button.place(
    x=57.0,
    y=358.0,
    width=165.0,
    height=39.0
)

upload_label = Label(
    bg="#FFFFFF",
    fg="#000000",
    text="",
    font=("Inter", 12 * -1),
)
upload_label.place(
    x=232.0,
    y=358.0,
    width=165.0,
    height=39.0
)


button_image_2 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption5_frame/button_2.png")))
back_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=back_button_clicked,
    relief="flat"
)
back_button.place(
    x=535.0,
    y=407.0,
    width=112.89242553710938,
    height=39.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets(resource_path("forms/adoption5_frame/button_3.png")))
next_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=next_button_clicked,
    relief="flat"
)
next_button.place(
    x=657.0,
    y=407.0,
    width=112.89242553710938,
    height=39.0
)


# Do you have other pets?
q9 = StringVar() 

dot_image = PhotoImage(file=relative_to_assets(resource_path("forms/adoption5_frame/dot.png")))
black_dot_image = PhotoImage(file=relative_to_assets(resource_path("forms/adoption5_frame/black_dot.png")))
black_dot_small_image = PhotoImage(file=relative_to_assets(resource_path("forms/adoption5_frame/black_dot_small.png")))
pink_dot_image = PhotoImage(file=relative_to_assets(resource_path("forms/adoption5_frame/pink_dot.png")))
yes4_radio = Radiobutton(
    variable=q9,
    value="yes",
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    bd=0,
    indicatoron=False,
    image=dot_image,
    selectimage=pink_dot_image,
)
yes4_radio.place(
    x=55,
    y=83
)
no4_radio = Radiobutton(
    variable=q9,
    value="no",
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    bd=0,
    indicatoron=False,
    image=dot_image,
    selectimage=pink_dot_image,
)
no4_radio.place(
    x=173,
    y=83
)
# Have you had pets in the past?
q10 = StringVar()
yes5_radio = Radiobutton(
    variable=q10,
    value="yes",
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    bd=0,
    indicatoron=False,
    image=dot_image,
    selectimage=pink_dot_image,
)
yes5_radio.place(
    x=350,
    y=83
)
no5_radio = Radiobutton(
    variable=q10,
    value="no",
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    bd=0,
    indicatoron=False,
    image=dot_image,
    selectimage=pink_dot_image,
)
no5_radio.place(
    x=468,
    y=83
)

read_input()

window.resizable(False, False)
window.mainloop()
