import json

file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}


def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file)
    except:
        print("Failed to save.")

def view_tasks(tasks):
    print()
    taks_list = tasks["tasks"]
    if len(taks_list) == 0:
        print("no task to display.")
    else:
        print("Your To-Do list: ")
        for idx, task in enumerate(taks_list):
            status = "[Completed]" if task["complete"] else "[pending]"
            print(f"{idx + 1}. {task['description']} | {status}")


def create_tasks(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Description cannot be empty.")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_number >= len(tasks):
            tasks["tasks"][task_number - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")

def incomplete_task(tasks):
    print()
    tasks_list = tasks["tasks"]
    incomplete_tasks = [task for task in tasks_list if not task["complete"]]
    
    if len(incomplete_tasks) == 0:
        print("No incomplete tasks.")
    else:
        print("Incomplete Tasks:")
        for idx, task in enumerate(incomplete_tasks):
            print(f"{idx + 1}. {task['description']} | [pending]")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            deleted_task = tasks["tasks"].pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task['description']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")

def main():

    tasks = load_tasks()

    while  True:
        print("\nTo-Do List Manager")
        print("1. Veiw Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. View Incomplete Tasks")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            incomplete_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")
main()

