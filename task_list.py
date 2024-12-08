TASKS = []

def print_commands():
    print("\nTodo List Menu:")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit\n")

def view_tasks():
    if len(TASKS) == 0:
        print("No tasks in the list.\n")
        return
    
    for t in TASKS:
        print(t["id"], t["task"])

def get_choice():
    while True:
        print_commands()

        choice = input("Enter your choice: ")

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice!")
            continue

        return choice

def add_task():
    while True:
        task = input("Enter a new task: ").strip()

        if task == "":
            print("Invalid task!")
            continue

        TASKS.append({
            "id": len(TASKS) + 1,
            "task": task
        })

        return

def remove_task():
    global TASKS

    view_tasks()

    try:
        number = int(input("Enter the task number: "))

        if number not in range(1, len(TASKS) + 1):
            raise ValueError
        
        TASKS = [t for t in TASKS if t["id"] != number]

    except ValueError:
        print("Invalid task number")


def main():
    while True:
        choice = get_choice()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        else:
            break

if __name__ == "__main__":
    main()