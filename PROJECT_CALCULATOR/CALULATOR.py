from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import pandas as pd
import os

window = Tk()
window.title("CALCULATOR APPLICATION")
window.geometry("400x405")

n1 = IntVar()
n2 = IntVar()

# BASIC FUNCTIONS
def addition():
    a = n1.get()
    b = n2.get()
    result = a + b
    tkinter.messagebox.showinfo("OUTPUT WINDOW", f"ADDITION OF ENTERED NUMBERS IS,\n{result}")
    return result

def subtraction():
    a = n1.get()
    b = n2.get()
    result = a - b
    tkinter.messagebox.showinfo("OUTPUT WINDOW", f"SUBTRACTION OF ENTERED NUMBERS IS,\n{result}")
    return result

def multiplication():
    a = n1.get()
    b = n2.get()
    result = a * b
    tkinter.messagebox.showinfo("OUTPUT WINDOW", f"MULTIPLICATION OF ENTERED NUMBERS IS,\n{result}")
    return result

def division():
    try:
        a = n1.get()
        b = n2.get()
        if b == 0:
            tkinter.messagebox.showinfo("ALERT WINDOW", "ENTERED NUMBERS CAN'T BE ZERO")
            return
        result = a / b
        tkinter.messagebox.showinfo("OUTPUT WINDOW", f"DIVISION OF ENTERED NUMBERS IS,\n{result}")
        return result
    except ZeroDivisionError:
        tkinter.messagebox.showinfo("ALERT WINDOW", "Cannot divide by zero.")
        return None

def exit1():
    window.destroy()

def about():
    tkinter.messagebox.showinfo("ALERT WINDOW", '''HI, SHRIYANSH THIS SIDE( THE_DEVELOPER )\n
This calculator application can perform basic calculations like addition, subtraction, multiplication, and division.
\nIt also has the ability to save the history of calculations that were performed by the user earlier.
\nThe application provides a user-friendly graphical interface built using Tkinter, making it easy to use and interact with.
It is a versatile tool that can be used for quick calculations and keeping track of calculation history.
''')

def insertexcel(a, b, comm, result):
    # Ensure filename ends with .csv
    filename = f1.get().strip()+".csv"
    if not filename:
        tkinter.messagebox.showinfo("ALERT WINDOW", "DATA IS NOT BEING SAVED! \n\nSINCE FILE_NAME NOT GIVEN BY THE USER.")
        return
    else:
        dict_1 = {"1st": [a], "2nd": [b], "OPERA": [comm], "RES": [result]}
        df = pd.DataFrame(dict_1)
        if os.path.exists(filename):
            df.to_csv(filename, index=False, mode='a', header=False)
        else:
            df.to_csv(filename, index=False, mode='w', header=True)
        tkinter.messagebox.showinfo("OUTPUT WINDOW", "DATA SAVED SUCCESSFULLY!")
 

def his():
    # Ensure filename ends with .csv
    file_path = f1.get().strip()+'.csv'
    
    try:
        sr = pd.read_csv(file_path)
        # Check if the DataFrame is empty
        if sr.empty:
            tkinter.messagebox.showinfo("ALERT WINDOW", f"File '{file_path}' is empty.")
        else:
            data_str = sr.to_string(index=False, col_space=15,)  # Convert DataFrame to string with column space
            data_str = '\n\n'.join([line + ' ' * 5 for line in data_str.split('\n')])
            tkinter.messagebox.showinfo("HISTORY WINDOW", f"THE CALCULATION STORE IN   {file_path}    IS:- \n\n{data_str}")
            
    except FileNotFoundError:
        tkinter.messagebox.showinfo("ALERT WINDOW", f"File '{file_path}' not found.")
    except pd.errors.EmptyDataError:
        tkinter.messagebox.showinfo("ALERT WINDOW", f"File '{file_path}' is empty.")
    except Exception as e:
        tkinter.messagebox.showinfo("ALERT WINDOW", f"An error occurred: {str(e)}")

def handler():
    a = n1.get()
    b = n2.get()
    if isinstance(a, str) or isinstance(b, str):
        tkinter.messagebox.showinfo("ALERT WINDOW", "Entered values must be integers. Please type integer values.")
        return
    elif isinstance(a, int) and isinstance(b, int):
        comm = fn.get()
        if comm == "ADD":
            result = addition()
        elif comm == "SUB":
            result = subtraction()
        elif comm == "MULTIPLY":
            result = multiplication()
        elif comm == "DIVIDE":
            result = division()
        else:
            tkinter.messagebox.showinfo("ALERT WINDOW", "Please select an operation.")
            return
        if result is not None:
            insertexcel(a, b, comm, result)
    else:
        tkinter.messagebox.showinfo("ALERT WINDOW", "Entered values must be integers. Please type integer values.")
        return
    
def RUN():
    handler()

f1 = StringVar()

# CREATING MENU BAR IN OUR GUI
menu = Menu(window)
window.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="Exit", command=exit1)

subm3 = Menu(menu)
menu.add_cascade(label="RUN", menu=subm3)
subm3.add_command(label="EXECUTING THE CALCULATION!!!", command=RUN)

subm2 = Menu(menu)
menu.add_cascade(label="ABOUT", menu=subm2)
subm2.add_command(label="GAIN KNOWLEDGE FROM HERE!!!", command=about)

subm4 = Menu(menu)
menu.add_cascade(label="HISTORY", menu=subm4)
subm4.add_command(label="RECENT CALCULATIONS BY YOU :) !!!", command=lambda: his())

# LABELS AND BUTTON
label_1 = Label(window, text="NUMBER CRUNCH", width="320", relief="solid", font=("Stencil", 27, "bold"), fg="white", bg="orange")
label_1.pack(pady=2, padx=5)

label_2 = Label(window, text="FIRST NUMBER\nHERE!", font=("Lemon", 13))
label_2.place(x=18, y=70)
entry_1 = Entry(window, textvar=n1, font=("Sigmar One", 11), relief="solid", justify="center", width=7, borderwidth=2)
entry_1.place(x=46, y=125)

label_3 = Label(window, text="SECOND NUMBER\nHERE!", font=("Lemon", 13))
label_3.place(x=200, y=70)
entry_2 = Entry(window, textvar=n2, font=("Sigmar One", 11), relief="solid", justify="center", width=7, borderwidth=2)
entry_2.place(x=240, y=125)

label_4 = Label(window, text="OPERATIONS", width=11, fg="sky blue", relief="solid", font=("Cooper Black", 20))
label_4.place(x=95, y=195)

LABEL_5 = Label(window, text="FILE NAME HERE: -", font=("Orbitron", 13, "bold"))
LABEL_5.place(x=10, y=306)

f1 = StringVar()
entry_1 = Entry(window, textvariable=f1, width=23, font=("Stencil", 10), relief="solid", borderwidth=2)
entry_1.place(x=200, y=307)

# BUTTON FOR OPERATIONS
fn = StringVar()
button_1 = Radiobutton(window, variable=fn, value="ADD", fg="white", bg="violet", text="ADD\n+", width=4, relief="solid", height=2, font=("Orbitron", 10))
button_1.place(x=10, y=255)

button_2 = Radiobutton(window, variable=fn, value="SUB", text="SUB\n-", width=4, relief="solid", height=2, font=("Orbitron", 10), fg="white", bg="red")
button_2.place(x=95, y=255)

button_3 = Radiobutton(window, variable=fn, value="MULTIPLY", text="MULTIPLY\nX", width=8, height=2, font=("Orbitron", 10), relief="solid", fg="white", bg="grey")
button_3.place(x=180, y=255)

button_4 = Radiobutton(window, variable=fn, value="DIVIDE", text="DIVIDE\n/", width=6, height=2, font=("Orbitron", 10), relief="solid", fg="white", bg="light green")
button_4.place(x=300, y=255)

button_5 = Button(window, fg="white", bg="blue", relief="solid", width=10, text="HIT ME !!!\n:}", command=handler, font=("Wide Latin", 12, "bold"))
button_5.place(x=94, y=340)

window.mainloop()
