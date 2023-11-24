tasks = []


def add_task(task):
    tasks.append(task)
    print("Task added: " + task)


def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")


def mark_completed(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index] += " (Completed)"
        print("Task marked as completed: " + tasks[task_index])
    else:
        print("Invalid task index")


def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print("Task deleted: " + deleted_task)
    else:
        print("Invalid task index")


while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task index to mark as completed: ")) - 1
        mark_completed(task_index)
    elif choice == "4":
        task_index = int(input("Enter the task index to delete: ")) - 1
        delete_task(task_index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
