from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import random
import string

# Initialize the main window
window = Tk()
window.title("PASSWORD GENERATOR APPLICATION")
window.geometry("630x420")

def exit1():
    window.destroy()

def about():
    tkinter.messagebox.showinfo("ABOUT", '''Hi, this is Shriyansh (the developer).\n
This application is designed to generate secure passwords based on user-defined criteria.
\n\nWe have many features in this application, including generating password, viewing the list, deleting the passwords generated, etc.
\n\nIt also has a user-friendly interface.
''')

def gen(length, numbers, special_chars):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special

    return pwd

# Creating menu bar in the GUI
menu = Menu(window)
window.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="Exit", command=exit1)

subm2 = Menu(menu)
menu.add_cascade(label="ABOUT", menu=subm2)
subm2.add_command(label="GAIN KNOWLEDGE FROM HERE", command=about)

# Title label
label_m = Label(window, text="PASSWORD GENERATOR", width=500, relief="solid", font=("Orbitron", 26, "bold"), bg="BLUE", fg="white")
label_m.pack(pady=6, padx=8)

# Load and display an image
img = Image.open("A:\\TKINTER PYTHON for GUI\\PASSWORD_GEN\\images.png")
photo = ImageTk.PhotoImage(img)
label_x = Label(window, image=photo, relief="solid")
label_x.place(x=300,y=60)

# Length input label and entry
label_1 = Label(window, text="ENTER THE LENGTH", font=("Stencil", 20, "bold"))
label_1.place(x=18,y=60)

ln = StringVar()
entry_1 = Entry(window, textvariable=ln, relief="solid", justify="center", width=22,font=("Arial Rounded MT Bold", 12))
entry_1.place(x=35,y=100)

# Checkboxes for options
checkbox_var = BooleanVar()
checkbox_1 = Checkbutton(window, text="INCLUDE NUMBERS", variable=checkbox_var, font=("Lemon", 13))
checkbox_1.place(x=10,y=150)

checkbox_special_var = BooleanVar()
checkbox_special = Checkbutton(window, text="INCLUDE SPECIAL CHARS", variable=checkbox_special_var, font=("Lemon", 13))
checkbox_special.place(x=10,y=180)

# Text area to display generated passwords
password_container = Text(window, height=10, width=46, font=("Arial Rounded MT Bold", 12),relief="solid")
password_container.place(x=10,y=230)

def generate_password():
    try:
        length = int(ln.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        include_numbers = checkbox_var.get()
        include_special = checkbox_special_var.get()
        password = gen(length, include_numbers, include_special)
        password_container.insert(END, f"Password: {password}\n")
    except ValueError as e:
        tkinter.messagebox.showerror("Input Error","LENGTH FIELD SHOULD BE DIGITS VALUE")

def clear_passwords():
    password_container.delete("1.0", END)

# Buttons for generating and clearing passwords
Button_1 = Button(window, text="GENERATE \nPASSWORD", font=("Cinzel Black", 12, "bold"), relief="solid", command=generate_password,bg="red",fg="white")
Button_1.place(x=500,y=250)

clear_button = Button(window, text="CLEAR", font=("Cinzel Black", 12, "bold"), relief="solid", command=clear_passwords,bg="red",fg="white")
clear_button.place(x=520,y=350)

# Start the main event loop
window.mainloop()
