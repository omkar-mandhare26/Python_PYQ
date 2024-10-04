#Chatgpt

import tkinter as tk
import random

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def change_color():
    new_color = random_color()
    root.configure(bg=new_color)
    root.after(1000, change_color)  

root = tk.Tk()
root.title("Color Changing Background")
root.geometry("500x500")

change_color()

root.mainloop()
