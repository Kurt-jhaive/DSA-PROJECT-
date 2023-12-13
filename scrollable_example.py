import tkinter as tk

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

root = tk.Tk()
root.title("Scrollable Entry Group")

# Create a canvas with a vertical scrollbar
canvas = tk.Canvas(root, height=200)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Add some entry widgets to the frame
for i in range(20):
    entry = tk.Entry(frame)
    entry.pack(pady=5)

# Bind the mousewheel event to the canvas
canvas.bind_all("<MouseWheel>", on_mousewheel)

# Update the scroll region
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
