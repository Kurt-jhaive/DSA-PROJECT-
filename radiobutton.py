from tkinter import Tk, Radiobutton, IntVar

# Create the main window
root = Tk()
# root.color
# Create an IntVar to store the selected value
x = IntVar()

# Create a Radiobutton without the grey background
single_radio = Radiobutton(
    root,
    variable=x,
    value=1,
    bg="white",
      # Set color to an empty string for no background
    selectcolor="white",  # Set selectcolor to an empty string for no background
    # or use a transparent color like selectcolor="white" for a white background
    # fg="#FB7196"  # You can uncomment this line if you want to set the text color
)

# Pack the Radiobutton
single_radio.pack()

# Start the Tkinter event loop
root.mainloop()
