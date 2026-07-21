task = []

def addTask():
    ta = input("Enter a Task: ")
    task.append(ta)
    print("Task added successfully!\n")

def viewTasks():
    if len(task) == 0:
        print("No tasks available.\n")
    else:
        print(" Your Tasks :-")
        for i, t in enumerate(task, start=1):
            print(f"{i}.{t}")
        print()

def DeleteTask():
    if len(task) == 0:
        print("No task to delete.\n")
        return

    viewTasks()
    task_num = int(input("Enter task number to delete: "))

    if 1 <= task_num <= len(task):
        remove_task = task.pop(task_num - 1)
        print(f"{remove_task}, deleted Successfully!\n")
    else:
        print("Invalid task number\n")

def EditTask():
    if len(task) == 0:
        print("No tasks available.\n")
        return

    viewTasks()
    task_num = int(input("Enter a task number to edit: "))

    if 1 <= task_num <= len(task):
        new_task = input("Enter a new task: ")
        task[task_num - 1] = new_task
        print("Updated Successfully!\n")
    else:
        print("Invalid task number!\n")


while True:
    print("*** TO DO LIST ***")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Edit Task")
    print("5. Exit")

    ch = input("Enter your choice : ")

    if ch == "1":
        addTask()
    elif ch == "2":
        viewTasks()
    elif ch == "3":
        DeleteTask()
    elif ch == "4":
        EditTask()
    elif ch == "5":
        print("Exit !")
        break
    else:
        print("Invalid choice !\n")