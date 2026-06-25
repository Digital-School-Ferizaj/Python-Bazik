from tkinter import *
from tkinter import messagebox
from datetime import date, datetime
from tkcalendar import Calendar
import os


root = Tk()
root.title("Task Managment")
root.config(bg="#223441")
root.resizable(width=False, height=False)

#Create two main containers
left_frame = Frame(root, bg="#223441", width=400, height=500)
right_frame = Frame(root, bg="#223441", width=400, height=500)

#Layout the main containers
left_frame.grid(row=0, column=0, pady=20, padx=20)
right_frame.grid(row=0, column=1, pady=20, padx=20)

#Listbox
lb = Listbox(
    left_frame,
    width=25,
    height =15,
    borderwidth=0,
    selectmode=SINGLE,
    font=("Times", 18),
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none"
    )
lb.grid(row=0, column=0)


input_field = Entry(
    right_frame,
    font=('times', 15),
    width=25
    )

input_field.grid(row=0, column=0, sticky=W, pady=5)

cal = Calendar(right_frame, selectmode= "day")
cal.grid(row=1, column=0, sticky=W, pady=5)

today = date.today()


#This function creates a new task and it stores it in a file
def newTask():
    filesize = os.path.getsize("tasks.txt")
    task_name = input_field.get()
    if task_name != "":
        lb.insert(END, task_name)
        input_field.delete(0, "end")
        with open("tasks.txt", "a") as file:
            if filesize == 0:
                file.write(task_name + "," +cal.get_date())
            else:
                file.write("\n" + task_name + "," +cal.get_date())
    else:
        messagebox.showwarning("Warning", "Please write task name")


def deleteTask():
    #write all taks that dont match with
    #the task selected to a new file
    with open("tasks.txt", "r") as input:
        with open("temp.txt", "w") as output:
            #iterate all lines from file
            for line in input:
                #if text matches then dont write
                current_task = line.split(",")
                if current_task[0] != lb.get(ANCHOR):
                    output.write(line)

    lb.delete(ANCHOR)
    #replace file with original name
    os.replace("temp.txt", "tasks.txt")

    #remove the last blank line of the tasks file  
    with open("task.txt", "r") as f:
        data = f.read()
        with open("temp.txt", "w") as w:
            w.write(data[:-1])

    os.replace("temp.txt", "tasks.txt")

def getTasks():
    list_tasks = []
    with open("tasks.txt") as file:
        for line in file:
            line = line.rstrip("\n")
            current_task = line.split(",")
            task_date = datetime.strptime(current_task[1], "%m/%d/%y").date()
            current_task[1] = task_date
            list_tasks.append(current_task)
    return list_tasks

tasks =getTasks()

for item in tasks:
    lb.insert(END, item[0])



def checkDaysLeft():
    with open("tasks.txt") as file:
        for line in file:
            current_task = line.slpit(",")
            if current_task[0] == lb.get(ANCHOR):
                current_task_date_stripped = current_task[1].strip("\n")
                task_date = datetime.strptime(current_task_date_stripped, "%m/%d/%y").date()
                time_between = str(task_date - today)
                number_of_days = time_between.split(" ")
                messagebox.showwarning("Warning", "You have "+number_of_days[0]+" days left to finish this task")


        
addTask_btn = Button(
    right_frame,
    text='Add Task',
    font=('times 14'),
    width=20,
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.grid(row=2, column=0, sticky=W, pady=5)

delTask_btn = Button(
    right_frame,
    text='Delete Task',
    font=('times 14'),
    width=20,
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.grid(row=3, column=0, sticky=W, pady=5)

CheckDays_btn = Button(
    right_frame,
    text='Check days left',
    font=('times 14'),
    width=20,
    bg='#008CBA',
    padx=20,
    pady=10,
    command=checkDaysLeft
)
CheckDays_btn.grid(row=4, column=0, sticky=W, pady=5)

root.mainloop()





















    
