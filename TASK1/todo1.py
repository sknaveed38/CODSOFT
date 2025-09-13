#output in GUL(graphical user interface) based sk
import tkinter as tk
from tkinter import messagebox

def load_tasks():
    """
    Loads tasks from the tasks.txt file into a list.
    If the file doesn't exist, it will be created.
    """
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """
    Saves the list of tasks to the tasks.txt file.
    """
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        self.tasks = load_tasks()

        self.frame_tasks = tk.Frame(self.root)
        self.frame_tasks.pack(pady=10)

        self.listbox_tasks = tk.Listbox(self.frame_tasks, width=50, height=15, selectmode=tk.SINGLE)
        self.listbox_tasks.pack(side=tk.LEFT)

    
        self.scrollbar_tasks = tk.Scrollbar(self.frame_tasks)
        self.scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox_tasks.config(yscrollcommand=self.scrollbar_tasks.set)
        self.scrollbar_tasks.config(command=self.listbox_tasks.yview)
        
        self.entry_task = tk.Entry(self.root, width=50)
        self.entry_task.pack(pady=10)

        self.frame_buttons = tk.Frame(self.root)
        self.frame_buttons.pack(pady=10)

        self.button_add_task = tk.Button(self.frame_buttons, text="Add Task", command=self.add_task)
        self.button_add_task.pack(side=tk.LEFT, padx=5)

        self.button_delete_task = tk.Button(self.frame_buttons, text="Delete Task", command=self.delete_task)
        self.button_delete_task.pack(side=tk.LEFT, padx=5)

        self.button_mark_completed = tk.Button(self.frame_buttons, text="Mark Completed", command=self.mark_task_completed)
        self.button_mark_completed.pack(side=tk.LEFT, padx=5)

        self.populate_tasks_listbox()

    def populate_tasks_listbox(self):
        """
        Clears and populates the listbox with tasks.
        """
        self.listbox_tasks.delete(0, tk.END)
        for task in self.tasks:
            self.listbox_tasks.insert(tk.END, task)

    def add_task(self):
        """
        Adds a new task from the entry widget to the list.
        """
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            save_tasks(self.tasks)
            self.populate_tasks_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        """
        Deletes the selected task from the list.
        """
        try:
            selected_task_index = self.listbox_tasks.curselection()[0]
            self.tasks.pop(selected_task_index)
            save_tasks(self.tasks)
            self.populate_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_task_completed(self):
        """
        Marks the selected task as completed.
        """
        try:
            selected_task_index = self.listbox_tasks.curselection()[0]
            task = self.tasks[selected_task_index]
            if not task.startswith("[DONE]"):
                self.tasks[selected_task_index] = "[DONE] " + task
                save_tasks(self.tasks)
                self.populate_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
