# A beginner-friendly, well-commented, and structured To-Do List application.

# The tasks will be stored in a file named "tasks.txt" in the same directory.
# Each task is stored on a new line.
# A completed task is marked with a "[DONE]" prefix.

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

def add_task(tasks):
    """
    Adds a new task to the list.
    """
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def view_tasks(tasks):
    """
    Views all tasks with their status.
    """
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "DONE" if task.startswith("[DONE]") else "Pending"
            task_description = task[7:] if task.startswith("[DONE]") else task
            print(f"{i + 1}. [{status}] {task_description}")

def update_task(tasks):
    """
    Updates or edits an existing task.
    """
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_num - 1] = new_task
            save_tasks(tasks)
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def mark_task_completed(tasks):
    """
    Marks a task as completed.
    """
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] = "[DONE] " + tasks[task_num - 1]
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """
    Deletes a task.
    """
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            save_tasks(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """
    The main function of the To-Do List application.
    """
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update or edit an existing task")
        print("4. Mark a task as completed")
        print("5. Delete a task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_task_completed(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Exiting the program. Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
