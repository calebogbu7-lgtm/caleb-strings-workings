tasks = []
while True:
    print("**. About the app")
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")
    print("4. Mark task as Done")
    print("5. Delete task")
    choice = input("type_number: ")
    if choice == "3":
        print("goodbye")
        break
    elif choice == "1":
        task = input("enter your task:").strip()
        if len(task) == 0:
            print("task is empty")
        else:
            tasks.append({"name": task, "status": "yet to accomplish"})
            print("task added!")
    elif choice == "2":
        if len(tasks) == 0:
            print("no_task_to_preview")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. Task:{tasks[i]['name']} - {tasks[i]['status']}")
    elif choice == "4":
        if len(tasks) == 0:
            print("no_task_to_mark")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. Task:{tasks[i]['name']} - {tasks[i]['status']}")
            while True:
                task_number = input("deed_task_number (or 0 to go back): ")
                if task_number == "0":
                    break
                try:
                    tasks[int(task_number)-1]["status"] = "done"
                except:
                    print("invalid task number, try again")
    elif choice == "5":
        if len(tasks) == 0:
            print("no_task_to_delete")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. Task:{tasks[i]['name']} - {tasks[i]['status']}")
            while True:
                task_number = input("number_of_task_to_delete (or 0 to go back): ")
                if task_number == "0":
                    break
                try:
                    del tasks[int(task_number)-1]
                except:
                    print("invalid task number, try again")
    elif choice == "**":
        print("this is a simple to do list app. that shows you a menu where you can add tasks, view everything on your list, mark tasks as done, delete tasks you don't need anymore, or exit the program. It keeps looping back to the menu after every action, so you can manage your whole list in one sitting, and it won't crash or break if you accidentally type something invalid — it just tells you and lets you try again.")
    else:
        print("invalid input please choose a number from the above list")