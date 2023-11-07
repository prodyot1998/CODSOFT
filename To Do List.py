tasks = []
def display_tasks():
    if tasks:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']} - {'Done' if task['is_done'] else 'Not Done'}")
    else:
        print("Your To-Do List is empty.")
def add_task(task_name):
    tasks.append({'task': task_name, 'is_done': False})
    print(f"Task '{task_name}' added to your To-Do List.")
def update_task(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['is_done'] = True
        print(f"Task '{tasks[task_number - 1]['task']}' marked as done.")
    else:
        print("Invalid task number.")
while True:
    print("\nTo-Do List Menu:1. View Tasks 2. Add Task 3. Mark Task as Done 4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        display_tasks()
    elif choice == '2':
        task_name = input("Enter the task name: ")
        add_task(task_name)
    elif choice == '3':
        display_tasks()
        task_number = int(input("Enter the task number to mark as done: "))
        update_task(task_number)
    elif choice == '4':
        print("Exiting the To-Do List.")
        break
    else:
        print("Invalid choice. Please select a valid option.")