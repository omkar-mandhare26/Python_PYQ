# gpt
import tkinter as tk
import random
import string

def generate_password():
    password = ''.join(random.choices(string.ascii_letters, k=7))
    
    result_label.config(text=f"Generated Password: {password}")

root = tk.Tk()
root.title("Random Password Generator")

generate_button = tk.Button(root, text="Refresh Password", command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

generate_password()

root.mainloop()
