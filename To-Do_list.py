#Simple To-Do List Application

Todo_list = []

def show_menu():
    print("\n1. View To-Do List\n2. Add Task\n3. Remove Task\n4. Exit")

def view_tasks():
    if Todo_list:
        for i, task in enumerate(Todo_list, 1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")

def add_task():
    task = input("Enter a new task: ")
    Todo_list.append(task)
    print("Task added.")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(Todo_list):
            Todo_list.pop(task_num - 1)
            print("Task removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Thank you!")
        break
    else:
        print("Invalid option.")
