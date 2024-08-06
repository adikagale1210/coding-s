import os
import json

class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Incomplete"
        return f"[{self.task_id}] {self.title}: {self.description} ({status})"

def add_task(tasks, title, description):
    task_id = len(tasks) + 1
    task = Task(task_id, title, description)
    tasks.append(task)

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        print(task)

def mark_task(tasks, task_id, completed=True):
    for task in tasks:
        if task.task_id == task_id:
            if completed:
                task.mark_complete()
            else:
                task.mark_incomplete()
            break

def delete_task(tasks, task_id):
    tasks[:] = [task for task in tasks if task.task_id != task_id]

def save_tasks(tasks, filename='tasks.txt'):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)

def load_tasks(filename='tasks.txt'):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            for task_data in tasks_data:
                task = Task(task_data['task_id'], task_data['title'], task_data['description'])
                if task_data['completed']:
                    task.mark_complete()
                tasks.append(task)
    return tasks

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Mark Task as Incomplete")
        print("5. Delete Task")
        print("6. Save and Exit")
        print("7. Exit without Saving")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(tasks, title, description)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as complete: "))
            mark_task(tasks, task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as incomplete: "))
            mark_task(tasks, task_id, completed=False)
        elif choice == '5':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks, task_id)
        elif choice == '6':
            save_tasks(tasks)
            break
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
