import tkinter as tk
from tkinter import *
from tkinter import messagebox
from custom_wordlist import wordlist_generator
from password_strength import password_check
from save_file import save_as_txt

def gui_app():
    def on_submit():
        pw = pw_entry.get()
        name = name_entry.get()
        dob = dob_entry.get()
        pet = pet_entry.get()
        extra = extra_entry.get().split()
        
        password_check(pw)
        wl = wordlist_generator(name, dob, pet, extra)
        save_as_txt(wl)

        messagebox.showinfo("Done", "Analysis and wordlist generation complete!")

    root = tk.Tk()
    root.title("Password Strength & Wordlist Generator")

    tk.Label(root, text="Password").grid(row=0)
    tk.Label(root, text="Name").grid(row=1)
    tk.Label(root, text="DOB").grid(row=2)
    tk.Label(root, text="Pet Name").grid(row=3)
    tk.Label(root, text="Extra Words").grid(row=4)

    pw_entry = tk.Entry(root, width=30)
    name_entry = tk.Entry(root, width=30)
    dob_entry = tk.Entry(root, width=30)
    pet_entry = tk.Entry(root, width=30)
    extra_entry = tk.Entry(root, width=30)

    pw_entry.grid(row=0, column=1)
    name_entry.grid(row=1, column=1)
    dob_entry.grid(row=2, column=1)
    pet_entry.grid(row=3, column=1)
    extra_entry.grid(row=4, column=1)

    tk.Button(root, text="Submit", command=on_submit).grid(row=5, column=0, columnspan=2)

    root.mainloop()
if __name__ == "__main__":
       gui_app()

