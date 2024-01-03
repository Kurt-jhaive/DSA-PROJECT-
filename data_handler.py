import tkinter as tk
import json

# def save_input(canvas):
#     # Get all child widgets of the canvas (or the parent widget containing the entry widgets)
#     all_widgets = canvas.winfo_children()

#     # Filter out only the Entry widgets
#     entry_widgets = [widget for widget in all_widgets if isinstance(widget, tk.Entry)]

#     # Get the user input from all entry widgets
#     inputted_data = [widget.get() for widget in entry_widgets]

#     # Check if the file already has content
#     with open("signup_data.txt", "r") as f:
#         has_content = bool(f.read())

#     # Save the inputted data to a file
#     with open("signup_data.txt", "a") as f:
#         # Add a newline if the file already has content
#         if has_content:
#             f.write("\n")
        
#         for data in inputted_data:
#             f.write(data + "\n")

def save_input(canvas):
    # Get all child widgets of the canvas (or the parent widget containing the entry widgets)
    all_widgets = canvas.winfo_children()

    # Filter out only the Entry widgets
    entry_widgets = [widget for widget in all_widgets if isinstance(widget, tk.Entry)]

    # Get the user input from all entry widgets
    inputted_data = {widget.winfo_name().split('!')[-1]: widget.get() for widget in entry_widgets}

    # Load existing data if the file already exists
    try:
        with open("signup_data.json", "r") as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        existing_data = {}

    # Update existing data with the new input
    existing_data.update(inputted_data)

    # Save the combined data to a file
    with open("signup_data.json", "w") as f:
        json.dump(existing_data, f, indent=2)


def append_input(canvas):
    # Get all child widgets of the canvas (or the parent widget containing the entry widgets)
    all_widgets = canvas.winfo_children()

    # Filter out only the Entry widgets
    entry_widgets = [widget for widget in all_widgets if isinstance(widget, tk.Entry)]

    # Get the user input from all entry widgets with user-friendly keys
    inputted_data = {widget.winfo_name().split('!')[-1]: widget.get() for widget in entry_widgets}

    # Load existing data if the file already exists
    try:
        with open("signup_data.json", "r") as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        existing_data = {}

    # Find the last key in the existing data
    last_key = max(existing_data, key=int, default=0)

    # Create new keys by incrementing from the last key
    new_keys = {str(i + int(last_key) + 1): value for i, (key, value) in enumerate(inputted_data.items())}

    # Update existing data with the new input
    existing_data.update(new_keys)

    # Save the combined data to a file
    with open("signup_data.json", "w") as f:
        json.dump(existing_data, f, indent=2)


def read_input(canvas):
    # Read the inputted data from the file
    with open("signup_data.txt", "r") as f:
        inputted_data = f.readlines()

    # Put the data into the Entry widgets
    for widget, data in zip(canvas.winfo_children(), inputted_data):
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)  # Clear existing text
            widget.insert(0, data.strip())  # Insert the data into the Entry widget


def delete_input():
    # Delete the content of the file
    with open("signup_data.txt", "w") as f:
        f.write("")