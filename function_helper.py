import sys
import os
from tkinter import messagebox

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def function1():
    print("Function 1 Called!")

def function2():
    print("Function 2 Called!")

def function4():
    print("Function 4 Called!")

def function5():
    print("Function 5 Called!")

