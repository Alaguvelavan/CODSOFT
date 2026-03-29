tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task ")
    print("2. View Task ")
    print("3. Mark Task as Done ")
    print("4. Delete Task ")
    print("5. Exit ")

def add_task():
        task = input("Enter task: ")
        tasks.append({ "task":task, "done":False })
        print(f"Task '{task}' added!")

def view_task():
    if not tasks:
        print("No tasks yet!")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status  = "completed" if task["done"] else "inComplete"
        print(f"{index}. {task['task']} [{status}]")


def mark_done(): 
     view_task()
     if not tasks:
          return
     try:
          index = int(input("Enter task number to mark done: ")) - 1
          if 0 <= index < len(tasks):
               tasks[index]["done"] = True
               print("Marked as done!")
          else:
               print("Invalid number!")
     except ValueError:
               print("please enter a valid number.")



def delete_task():
     view_task()
     if not tasks:
          return
     try:
               index = int(input("Enter task number to delete: ")) - 1
               if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    print(f"Deleted task: {removed['task']}")
               else:
                    print("Invalid number!")
     except ValueError:
               print("please enter a valid number.")


while True:
     show_menu()
     select = input("Choose an option (1-5): ")

     if select == '1':
          add_task()

     elif select == '2':
          view_task()
     elif select == '3':
          mark_done()
     elif select == '4':
          delete_task()
     elif select == '5':
          print("Successfully Exited")
          break
     else:
          print("Invalid selected Option. Try again.")




 