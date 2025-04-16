"""
Adding tasks
Viewing tasks
Marking tass as done
Deleting tasks
Saving to a file todo.json
"""

import json
import os

TODO_FILE = "todo.json"


def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def list_tasks(tasks):
    if not tasks:
        print("No tasks found. ")

    for i, task in enumerate(tasks):
        status = 'yes' if task['done'] else 'no'
        print(f"{i+1}. [{status}] {task['task']}")


def add_tasks(tasks):
    task = input("Enter a new task ")
    tasks.append({"task": task, "done": False})
    print("Task added.")


def mark_done(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: "))-1
        tasks[index]["done"] = True
        print("Task marked as done.")

    except (IndexError, ValueError):
        print("Invalid task number  ")


def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to delete "))-1
        removed = tasks.pop(index)
        print("task is Deleted: ")
        task = input("Enter a task to delete ")
        for element in tasks:
            if "Trainee" in element:
                del element
        with open(TODO_FILE, "w") as file:
            json.dump(tasks, file)
    except (IndexError, ValueError):
        print("Invalid tasks number.")


def main():
    tasks = load_tasks()
    while True:
        print("\n ----To-Do List ----")
        print("1. List tasks")
        print("2. Add tasks ")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5 . Exit ")
        choice = input("chose an option: ")

        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            add_tasks(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye! ")
            break
        else:
            print("Invalid choice ")


if __name__ == "__main__":
    main()
