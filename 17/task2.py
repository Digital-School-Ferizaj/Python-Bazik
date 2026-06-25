import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do App")
        self.master.geometry("300x400")

        self.tasks = []
        self.done_tasks = []

        # Calendar
        self.calendar = ttk.Calendar(self.master, firstweekday="sunday")
        self.calendar.pack(fill="both", expand=True)

        # Task Entry
        self.task_entry = tk.Entry(self.master)
        self.task_entry.pack(pady=10)

        # Add Task Button
        self.add_task_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        # Show Done Tasks Button
        self.show_done_tasks_button = tk.Button(self.master, text="Show Done Tasks", command=self.show_done_tasks)
        self.show_done_tasks_button.pack()

        # Task List
        self.task_list = tk.Listbox(self.master)
        self.task_list.pack(fill="both", expand=True)
        self.update_task_list()

        # Mark as Done Button
        self.mark_as_done_button = tk.Button(self.master, text="Mark as Done", command=self.mark_as_done)
        self.mark_as_done_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        date = self.calendar.selection_get()
        if task in [task_info[0] for task_info in self.tasks]:
            messagebox.showerror("Error", "Task with this name already exists.")
            return
        if date < str(datetime.datetime.now().date()):
            messagebox.showerror("Error", "Cannot add task for past date.")
            return
        self.tasks.append((task, date))
        self.update_task_list()
        self.save_tasks()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, f"{task[0]} - {task[1]}")

    def mark_as_done(self):
        selected_task = self.task_list.get(self.task_list.curselection())
        if not selected_task:
            messagebox.showerror("Error", "Please select a task to mark as done.")
            return
        task, date = selected_task.split(" - ")
        self.tasks.remove((task, date))
        self.done_tasks.append((task, date))
        self.update_task_list()
