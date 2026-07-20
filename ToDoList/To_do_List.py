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


