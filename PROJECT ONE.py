from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox

window = Tk()
task_list = []  # Initialize an empty list to store tasks

# FOR SETTING THE GUI SCREEN NAME
window.title("TO DO LIST APPLICATION")

# FOR SETTING THE GUI WINDOW SIZE
window.geometry("1000x475")

label_1 = Label(window, text="TO DO LIST TRACKER", relief="solid", font=("arial", 20, "bold"), bg="yellow", fg="red", width=1000)
label_1.pack(pady=3, padx=2)


# FOR UPDATING OUR GUI LIST BOX
def update_l():
    listbox1.delete(0, END)
    for i in task_list:
        listbox1.insert("end", i)

# FUNCTIONS FOR PERFORMING DIFFERENT FUNCTIONALITY IN GUI
def ADDING_TASK():
    task = fn.get()
    if not task.strip():
        tkinter.messagebox.showinfo("ALERT WINDOW", "ENTER TASK FIELD IS EMPTY....")
    else:
        task_list.append(task)
        update_l()
        tkinter.messagebox.showinfo("STATUS WINDOW", "BRAVO :) SUCCESSFULLY ADDED A TASK IN THE LIST!")

def EDIT_TASK():
    if not task_list:
        tkinter.messagebox.showinfo("ALERT WINDOW", "TASK LIST IS EMPTY\nEDITING CAN'T BE DONE AT THE MOMENT...\nYOU CAN TRY AFTER FIRST ADDING SOMETHING TO THE TASK LIST!")
    else:
        selected = listbox1.curselection()
        if not selected:
            tkinter.messagebox.showinfo("ALERT WINDOW", "Please select a task to edit.")
        else:
            task = task_list[selected[0]]
            new_task = jn.get()
            if not new_task.strip():
                tkinter.messagebox.showinfo("ALERT WINDOW", "EDIT TASK FIELD CAN'T BE EMPTY....")
            else:
                task_list[selected[0]] = new_task
                update_l()
                tkinter.messagebox.showinfo("STATUS WINDOW", "BRAVO :) SUCCESSFULLY EDITED THE TASK!")

def DEL_RECENT():
    if not task_list:
        tkinter.messagebox.showinfo("STATUS WINDOW", "The task list is already empty.")
    else:
        deleted_task = task_list.pop()
        update_l()
        tkinter.messagebox.showinfo("STATUS WINDOW", f"BRAVO :) SUCCESSFULLY DELETED '{deleted_task}' FROM THE LIST!")

def DEL_ALL():
    if not task_list:
        tkinter.messagebox.showinfo("STATUS WINDOW", "The task list is already empty.")
    else:
        task_list.clear()
        update_l()
        tkinter.messagebox.showinfo("STATUS WINDOW", "BRAVO :) SUCCESSFULLY DELETED ALL TASKS FROM THE LIST!")

def NUMBER_OF_TASKS():
    N = len(task_list)
    tkinter.messagebox.showinfo("FINAL OUTPUT", f"THE TOTAL NUMBER OF TASKS IS \n{N}")

def SORT_ASCEND():
    if not task_list:
        tkinter.messagebox.showinfo("STATUS WINDOW", "The task list is empty, nothing to sort.")
    else:
        task_list.sort()
        update_l()
        tkinter.messagebox.showinfo("STATUS WINDOW", "BRAVO :) SUCCESSFULLY SORTED THE TASKS IN ASCENDING ORDER!")

def SORT_DESCEN():
    if not task_list:
        tkinter.messagebox.showinfo("STATUS WINDOW", "The task list is empty, nothing to sort.")
    else:
        task_list.sort(reverse=True)
        update_l()
        tkinter.messagebox.showinfo("STATUS WINDOW", "BRAVO :) SUCCESSFULLY SORTED THE TASKS IN DESCENDING ORDER!")

completed_tasks=[]

def MARK_AS_COMPLETE():
    if not task_list:
        tkinter.messagebox.showinfo("ALERT WINDOW", "TASK LIST IS EMPTY\nMARKING AS COMPLETE CAN'T BE DONE AT THE MOMENT...\nYOU CAN TRY AFTER FIRST ADDING SOMETHING TO THE TASK LIST!")
    else:
        selected = listbox1.curselection()
        if not selected:
            tkinter.messagebox.showinfo("ALERT WINDOW", "Please select a task to mark as complete.")
        else:
            task = task_list.pop(selected[0])
            completed_tasks.append(task)
            update_l()
            tkinter.messagebox.showinfo("STATUS WINDOW", "BRAVO :) SUCCESSFULLY MARKED THE TASK AS COMPLETE!")

def SHOW_COMPLETED_TASKS():
    if not completed_tasks:
        tkinter.messagebox.showinfo("ALERT WINDOW", "No completed tasks to display.")
    else:
        tkinter.messagebox.showinfo("COMPLETED TASKS", "\n".join(completed_tasks))



def exist1():
    tkinter.messagebox.showinfo("STATUS WINDOW","EXISTING THE APPLICATION !!!!")
    exit()

def handler():
    a = var.get()
    b = var2.get()
    c = var3.get()
    D=fn.get()
    if (a != "NOTHING" and b == "NOTHING" and c == "NOTHING"):
        if a == "ADDING TASK":
            ADDING_TASK()
    elif (a == "CREATE" and b == "UPDATE" and c == "TRACK"):
        tkinter.messagebox.showinfo("ALERT WINDOW", "DON'T PRESS THE ENTER WITHOUT SELECTING ANYTHING")
    
    elif (a == "NOTHING" and b != "NOTHING" and c == "NOTHING"):
        if b == "DELETE RECENTLY ADDED TASK":
            DEL_RECENT()
        elif b == "EDIT TASK":
            EDIT_TASK()
        else:
            DEL_ALL()
    elif (a == "NOTHING" and b == "NOTHING" and c != "NOTHING"):
        if c == "NUMBERS OF TASK ENTERED":
            NUMBER_OF_TASKS()
        elif c == "SORT ASCENDINGLY":
            SORT_ASCEND()
        else:
            SORT_DESCEN()
    elif (a != "NOTHING" and b != "NOTHING" and c != "NOTHING"):
        tkinter.messagebox.showinfo("ALERT WINDOW", "PLEASE SELECT ONE TASK/CHOICE AT A TIME")
   
    else:
        tkinter.messagebox.showinfo("ALERT WINDOW", "ALL CHOICES CAN'T BE NOTHING AT THE SAME TIME")

def about():
    tkinter.messagebox.showinfo("ABOUT WINDOW", "Hi Users!\n\nShriyansh this side.\n\nThis project is created to assist people in completing their day-to-day tasks without missing..\n\nWe have added various features in this, such as:\n\nAdding an event/work\nEditing them\nSorting them\nPerforming certain activities with the tasks.m")

def HELPING():
    tkinter.messagebox.showinfo("HELPING GUIDE WINDOW",'''This project helps you to track with your list.\n\n
IF YOU WANT TO ADD ANY TASK IN YOUR TO DO LIST SIMPLY SELECT ADDING TASK OPTION AND PROCEED.
\n Similarly if you want to delete any data or update Anything just select that option and you may proceed!!!!.
''')

def DISPLAY_L():
    if not task_list:
        tkinter.messagebox.showinfo("TO DO LIST WINDOW", "The task list is empty.")
    else:
        task_list_str = "\n".join(task_list)
        tkinter.messagebox.showinfo("TO DO LIST WINDOW", f"Your current tasks:\n\n{task_list_str}")




#CREATING MENU BAR IN OUR GUI
menu = Menu(window)
window.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="Exit", command=exist1)

subm2=Menu(menu)
menu.add_cascade(label="ABOUT",menu=subm2)
subm2.add_command(label="GAIN KNOWLEDGE FROM HERE!!!",command=about)

subm3=Menu(menu)
menu.add_cascade(label="HELP",menu=subm3)
subm3.add_command(label="HEPLING GUIDE!!!",command=HELPING)

subm4=Menu(menu)
menu.add_cascade(label="DISPLAY DONE TASK",menu=subm4)
subm4.add_command(label="COMPLETED TASK BY YOU :) !!!",command=SHOW_COMPLETED_TASKS)

# FOR SETTING IMAGE IN OUR GUI INTERFACE
img = Image.open("A:\\TKINTER PYTHON for GUI\\PROJECT 1\\to_dp.jpg")
photo = ImageTk.PhotoImage(img)
label_2 = Label(window, image=photo, relief="solid")
label_2.place(x=2, y=45)

#FOR CHOICE AS A HEADING

label_3=Label(text="CHOICE",font=("Algerian",45,"bold"))
label_3.place(x=680,y=45)

Label_5=Label(text="ENTER TASK",font=("arial",13,"bold"))
Label_5.place(x=475,y=100)

fn=StringVar()
entry1=Entry(window,textvar=fn,width=25,relief="solid",justify='center')
entry1.place(x=475,y=125)

Label_4=Label(text="EDIT WITH",font=("arial",13,"bold"))
Label_4.place(x=475,y=160)

jn=StringVar()
entry2=Entry(window,textvar=jn,width=25,relief="solid",justify='center')
entry2.place(x=475,y=185)

Label_5=Label(text="LIST BUCKET",font=("arial",13,"bold"))
Label_5.place(x=510,y=250)

listbox1 = Listbox(window, width=30, height=10,relief="solid", borderwidth=2,justify='center')
listbox1.place(x=475,y=275)
scrollbar = Scrollbar(window, orient=VERTICAL, command=listbox1.yview, relief="solid", borderwidth=2)
scrollbar.place(x=662, y=275, height=165)

listbox1.config(yscrollcommand=scrollbar.set)


# FOR ADDING DROP DOWN FUNCTIONALITY IN OUR GUI INTERFACE
var = StringVar()
list_1 = ["ADDING TASK","NOTHING"]
drop_l = OptionMenu(window, var, *list_1)
var.set("CREATE")
drop_l.config(width=30, relief="solid", borderwidth=1)
drop_l.place(x=680,y=110)

var2 = StringVar()
list_2 = ["DELETE RECENTLY ADDED TASK","DELETE ALL TASK","EDIT TASK","NOTHING"]
drop_2 = OptionMenu(window, var2, *list_2)
var2.set("UPDATE")
drop_2.config(width=30, relief="solid", borderwidth=1)
drop_2.place(x=680,y=188)

var3 = StringVar()
list_3 = ["NUMBERS OF TASK ENTERED","SORT ASCENDINGLY","SORT DECENDINGLY","NOTHING"]
drop_3 = OptionMenu(window, var3, *list_3)
var3.set("TRACK")
drop_3.config(width=30, relief="solid", borderwidth=1)
drop_3.place(x=680,y=304)

button_1 = Button(window, text="ENTER ME !", width=12,fg="white",bg="red",font=("arial",11,"bold"),command=handler,relief="solid")
button_1.place(x=680, y=422)
BUTTON_x=Button(text="MARK AS COMPLETE",command=MARK_AS_COMPLETE,width=18,fg="white",bg="blue",font=("arial",11,"bold"),relief="solid")
BUTTON_x.place(x=815,y=422)

window.mainloop()
