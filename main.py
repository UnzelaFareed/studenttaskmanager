
from task_manager import TaskManager

manager = TaskManager()


def main():

    while True:

        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            title = input("Enter task title: ")

            task = manager.add_task(title)

            print("Task added successfully!")
            print("Task ID:", task["id"])

        elif choice == "2":

            tasks = manager.display_tasks()

            if not tasks:
                print("No tasks available.")

            for task in tasks:

                print(
                    task["id"],
                    task["title"],
                    "Completed" if task["completed"] else "Pending"
                )

        elif choice == "3":

            print("Goodbye!")
            break

        else:

            print("Invalid choice!")


if __name__ == "__main__":
    main()
