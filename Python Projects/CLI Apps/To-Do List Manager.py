import datetime
import heapq


highPriTasks, medPriTasks, lowPriTasks, allTasks = {}, {}, {}, {}
taskNumber = 0
priorityTasks = []
heapq.heapify(priorityTasks)


def add_task():
    task = {}
    task["title"] = input("Enter the task title:\t")
    task["description"] = input("Enter the task description:\t")
    task["status"] = 1     # Incomplete
    task["priority"] = int(input("Enter the task priority: 0 <- High, 1 <- Medium, 2 <- Low:\t"))
    try:
        date = input("Enter the due date and time (YYYY MM DD):\t")
        year, month, day = map(int, date.split())
        if input("Would you like to enter the time? y or n:\t") == 'y':
            time = input("Enter the time (HH MM SS):\t")
            hour, minute, second = map(int, time.split())
        else:
            hour, minute, second = 0, 0, 0
        task["duedate"] = (year, month, day, hour, minute, second)
    except ValueError:
        print("Invalid date or time format!")
        return
    
    global taskNumber
    allTasks[taskNumber] = task
    if task["priority"] == 0:
        highPriTasks[taskNumber] = task
    elif task["priority"] == 1:
        medPriTasks[taskNumber] = task
    else:
        lowPriTasks[taskNumber] = task    

    pri = (task["priority"], task["duedate"], taskNumber)
    heapq.heappush(priorityTasks, pri)

    taskNumber += 1


def next_task():
    try:
        task = heapq.heappop(priorityTasks)
    except:
        print("There are no tasks/All tasks are completed")
        return

    print("\nThe task with the highest priority is:")
    print("Task ID[" + str(task[2]) + "]: ", allTasks[task[2]])

    heapq.heappush(priorityTasks, task)

    
def remove_task(task_id):
    try:
        priorityTasks.remove((allTasks[task_id]["priority"], allTasks[task_id]["duedate"], task_id))
        heapq.heapify(priorityTasks)
        print("The task has been removed")
    except:
        print("Task not found")
        return
    
    if allTasks[task_id]["priority"] == 0:
        del highPriTasks[task_id]
    elif allTasks[task_id]["priority"] == 1:
        del medPriTasks[task_id]
    else:
        del lowPriTasks[task_id]

    del allTasks[task_id]

    
def list_tasks():
    print("\n0: High Priority Tasks")
    for task_id, task in highPriTasks.items():
        if task["status"]:
            print("Task ID[" + str(task_id) + "]: ", task)
    print("\n1: Medium Priority Tasks")
    for task_id, task in medPriTasks.items():
        if task["status"]:
            print("Task ID[" + str(task_id) + "]: ", task)
    print("\n2: Low Priority Tasks")
    for task_id, task in lowPriTasks.items():
        if task["status"]:
            print("Task ID[" + str(task_id) + "]: ", task)


def mark_complete(task_id):
    if task_id not in allTasks:
        print("The task does not exist")
        return
    
    if allTasks[task_id]["status"] == 0:
        print("The task has already been completed")
        return 
    else:
        allTasks[task_id]["status"] = 0
        print("The task is marked as completed")

        if allTasks[task_id]["priority"] == 0:
            del highPriTasks[task_id]
        elif allTasks[task_id]["priority"] == 1:
            del medPriTasks[task_id]
        else:
            del lowPriTasks[task_id]

        priorityTasks.remove((allTasks[task_id]["priority"], allTasks[task_id]["duedate"], task_id))
        heapq.heapify(priorityTasks)


while True:
    print("\n\n\nTASK MANAGER: Enter your choice")
    choice = int(input("1. Add task, 2. Find most important task, 3. Remove Task, 4. List tasks, 5. Mark as completed, 6. Exit\n"))
    if choice == 1:
        add_task()
    elif choice == 2:
        next_task()
    elif choice == 3:
        task_id = int(input("Enter the task_id to be removed:\t"))
        remove_task(task_id)
    elif choice == 4:
        list_tasks()
    elif choice == 5:
        task_id = int(input("Enter the task_id to be marked as completed:\t"))
        mark_complete(task_id)
    elif choice == 6:
        exit()
    else:
        print("Invalid choice, enter the choice again\n")