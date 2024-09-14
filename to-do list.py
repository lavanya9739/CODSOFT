import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        # Entry widget for adding tasks
        self.task_entry = tk.Entry(self.root, width=35)
        self.task_entry.pack(pady=10)

        # Add Task Button
        self.add_task_btn = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_btn.pack(pady=5)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Buttons to mark task as completed and delete task
        self.complete_task_btn = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_task_btn.pack(pady=5)

        self.delete_task_btn = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_btn.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def complete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.tasks[task_index]['completed'] = True
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "No task selected!")

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(task_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "No task selected!")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = task['task'] + (" [Completed]" if task['completed'] else "")
            self.task_listbox.insert(tk.END, task_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
    
