# To Do List --> Task
# 1. Create a Task, 2. List the Tasks, 3. Remove the Task, 4. Save the Tasks into the file 5. Load tasks from file.

#List,tuple,Dict,Set --> List

tasks = []

def display_menu():
    print("-----------To Do List Menu")
    print("1. Add a Task")
    print("2. List the Tasks")
    print("3. Remove a task")
    print("4, Save tasks the file")
    print("5. Load tasks from file")
    print("6. Exit")

def add_task():
    task=input("Enter the new task: ")
    tasks.append(task) # [] list.pop(2) [7,6,8] 1,2,3
    print("Task {Task} is added!")

def list_task(): 
    if len(tasks) == 0:# if tasks is empty
        print("No tasks are available")
    else:
        for i, task in enemurate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task():
    list_task()
    try:
        task_number = int(input("Enter the task number you wanted to remove: "))
        if 1<= task_number <= len(tasks):
            removed_task = tasks.pop(task_number-1)
            print("Task(removed_task) Removed!!")
        else:
            print("Invalid task number")
        except ValueError:
            print("Please enter a valid number.")
    

def save_task_file():
    file_name = input("Enter the file name to save the tasks: ")
    with open(file_name, 'w') as file:
        for task in tasks:
            file.write(task+"\n")
    print(f"Tasks saved to the (file_name)")


def load_task_file():
    file_name = input("Enter the file name to load task from: (please give full path)")
    if os.path.exists(file_name)
       with open(file_name,'r') as file:
           



