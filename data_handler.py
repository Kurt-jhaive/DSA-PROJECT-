import tkinter as tk

def read_input(canvas):
    # Read the inputted data from the file
    with open("data/signup_data.txt", "r") as f:
        inputted_data = f.readlines()

    # Put the data into the Entry widgets
    for widget, data in zip(canvas.winfo_children(), inputted_data):
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)  # Clear existing text
            widget.insert(0, data.strip())  # Insert the data into the Entry widget


def delete_input():
    # Delete the content of the file
    with open("data/signup_data.txt", "w") as f:
        f.write("")