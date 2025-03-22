import file_handler

def add_task():
    task = input("Enter task: ") + "\n"  
    tasks = file_handler.read_tasks()
    tasks.append(task)
    file_handler.write_tasks(tasks)
    print("Task added sucessfully")

def remove_task():
    tasks = file_handler.read_tasks()
    if len(tasks) == 0:
        print("No tasks available!")
        return
    count = 1
    for task in tasks:
        print(count, task)  
        count += 1
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if index >= 0 and index < len(tasks):
            removed_task = tasks[index]
            del tasks[index]
            file_handler.write_tasks(tasks)
            print("Removed:", removed_task)
        else:
            print("Invalid number!")
    except ValueError:
        print("Enter a valid number!")

def update_task():
    tasks = file_handler.read_tasks()
    if len(tasks) == 0:
        print("No tasks to update!")
        return
    count = 1
    for task in tasks:
        print(count, task) 
        count += 1

    try:
        index = int(input("Enter task number to update: ")) - 1
        if index >= 0 and index < len(tasks):
            new_task = input("Enter new task: ") + "\n"
            tasks[index] = new_task
            file_handler.write_tasks(tasks)
            print("Task updated!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Enter a valid number!")

def view_tasks():
    tasks = file_handler.read_tasks()
    if len(tasks) == 0:
        print("No tasks available!")
    else:
        count = 1
        for task in tasks:
            print(count, task) 
            count += 1
