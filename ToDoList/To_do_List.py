task = []

def addTask():
    ta= input("Enter a Task :")
    task.append(ta)
    print("Task added successfully!")

def viewTasks():
    if len(task) == 0 :
        print("No tasks available.\n")
    else : 
        print(" Your Tasks :-")
        for i, task in enumerate(task,start=1):
            print(f"{1}.{task}")
        print()
def DeleteTask() :
    if len(task) == 0:
        print("No task to delete.\n")
        return
    
    viewTasks()
    task_num = int(input("Enter task number to delete:"))
    
    if 1<= task_num <= len(task):
        remove_task = task.pop(task_num - 1)
        print(f"{remove_task} , delete Successfully!\n")
    else :
        print("Invalid task number")





while True:
    print("*** TO DO LIST ***")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")


    ch = input("Enter your choice")

    if ch == "1" :
        addTask()
    
    elif ch == "2" :
        viewTasks()
    elif ch == "3":
        DeleteTask()


