todo = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo.append(task)
        print("Task added")

    elif choice == "2":
        if not todo:
            print("No tasks")
        else:
            for i in range(len(todo)):
                print(i + 1, ".", todo[i])

    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(todo):
            todo.pop(num - 1)
            print("Task removed")
        else:
            print("Invalid number")

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")
