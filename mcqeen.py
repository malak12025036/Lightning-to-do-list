tasks = []

while True:
    print("\nLIGHTNING MCQUEEN'S TO-DO LIST")
    print("1. Add a task")
    print("2. View my to-do list")
    print("3. Mark a task as done")
    print("4. Remove a task")
    print("5. Quit")

    choice = input("What's the move, champ? ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"task": task, "done": False})
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                if tasks[i]["done"]:
                    status = "[DONE]"
                else:
                    status = "[PENDING]"

                print(str(i + 1) + ". " + status + " " + tasks[i]["task"])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to complete.")
        else:
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + tasks[i]["task"])

            number = int(input("Enter the task number: "))

            if number >= 1 and number <= len(tasks):
                tasks[number - 1]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + tasks[i]["task"])

            number = int(input("Enter the task number to remove: "))

            if number >= 1 and number <= len(tasks):
                removed = tasks.pop(number - 1)
                print("Removed:", removed["task"])
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Good luck in the race, Lightning McQueen!")
        break

    else:
        print("Invalid choice. Try again.")