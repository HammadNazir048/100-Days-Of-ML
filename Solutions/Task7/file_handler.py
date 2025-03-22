open("tasks.txt", "a").close()

def read_tasks():
    with open("tasks.txt", "r") as file:
        return file.readlines()

def write_tasks(tasks):
    with open("tasks.txt", "w") as file:
        file.writelines(tasks)
