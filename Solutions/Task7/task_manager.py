import task_operations

def task_manager():
    while True:
        print("Task Manager")
        print("Add")
        print("Remove")
        print("Update")
        print("View")
        print("Quit")

        choice = input("Enter your choice: ")

        if choice == "Add":
            task_operations.add_task()
        elif choice == "Remove":
            task_operations.remove_task()
        elif choice == "Update":
            task_operations.update_task()
        elif choice == "View":
            task_operations.view_tasks()
        elif choice == "Quit":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    task_manager()
