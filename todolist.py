class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully.")
        else:
            print("Task not found.")

    def mark_task_completed(self, task):
        if task in self.tasks:
            task.completed = True
            print("Task marked as completed.")
        else:
            print("Task not found.")

    def display_tasks(self):
        if len(self.tasks) == 0:
            print("To-Do List is empty.")
        else:
            print("To-Do List:")
            for task in self.tasks:
                status = "Completed" if task.completed else "Pending"
                print(f"Description: {task.description}")
                print(f"Status: {status}")
                print("--------------")

def menu():
    print("To-Do List Menu")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Mark a task as completed")
    print("4. Display all tasks")
    print("5. Quit")

todo_list = ToDoList()

while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        description = input("Enter task description: ")
        task = Task(description)
        todo_list.add_task(task)

    elif choice == '2':
        description = input("Enter task description to remove: ")
        found_task = None
        for task in todo_list.tasks:
            if task.description == description:
                found_task = task
                break

        if found_task:
            todo_list.remove_task(found_task)
        else:
            print("Task not found.")

    elif choice == '3':
        description = input("Enter task description to mark as completed: ")
        found_task = None
        for task in todo_list.tasks:
            if task.description == description:
                found_task = task
                break

        if found_task:
            todo_list.mark_task_completed(found_task)
        else:
            print("Task not found.")

    elif choice == '4':
        todo_list.display_tasks()

    elif choice == '5':
        print("Thank you for using the To-Do List.")
        break

    else:
        print("Invalid choice. Please try again.")
