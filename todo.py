def show_tasks(tasks):
    if not tasks:
        print("\n📋 Your to-do list is empty!")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "⬜"
            print(f"  {i}. {status} {task['name']}")
    print()


def main():
    tasks = []
    print("Welcome to your To-Do List! 🎉")

    while True:
        print("What would you like to do?")
        print("  1. Add a task")
        print("  2. Mark a task as done")
        print("  3. Remove a task")
        print("  4. View all tasks")
        print("  5. Quit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter task name: ").strip()
            if name:
                tasks.append({"name": name, "done": False})
                print(f"✅ Added: '{name}'")
            else:
                print("⚠️  Task name can't be empty.")

        elif choice == "2":
            show_tasks(tasks)
            if tasks:
                try:
                    num = int(input("Enter task number to mark as done: "))
                    if 1 <= num <= len(tasks):
                        tasks[num - 1]["done"] = True
                        print(f"✅ Marked '{tasks[num - 1]['name']}' as done!")
                    else:
                        print("⚠️  Invalid number.")
                except ValueError:
                    print("⚠️  Please enter a number.")

        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                try:
                    num = int(input("Enter task number to remove: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"🗑️  Removed: '{removed['name']}'")
                    else:
                        print("⚠️  Invalid number.")
                except ValueError:
                    print("⚠️  Please enter a number.")

        elif choice == "4":
            show_tasks(tasks)

        elif choice == "5":
            print("👋 Goodbye! Stay productive!")
            break

        else:
            print("⚠️  Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
