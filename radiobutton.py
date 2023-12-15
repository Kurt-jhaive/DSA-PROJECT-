import tkinter as tk

def print_selection():
    print("Selected value:", x.get())

# Create the main window
root = tk.Tk()
root.title("Radiobuttons with String Values")

# Create an StringVar to store the selected value
x = tk.StringVar()

# Create Radiobuttons with string values
radio_button1 = tk.Radiobutton(root, text="Option A", variable=x, value="bruh")
radio_button2 = tk.Radiobutton(root, text="Option B", variable=x, value="Basdf")
radio_button3 = tk.Radiobutton(root, text="Option C", variable=x, value="Casdf")

# Pack the Radiobuttons
radio_button1.pack()
radio_button2.pack()
radio_button3.pack()

# Button to print the selected value
print_button = tk.Button(root, text="Print Selection", command=print_selection)
print_button.pack()

# Start the Tkinter event loop
root.mainloop()
