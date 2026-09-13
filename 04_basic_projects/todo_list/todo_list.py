print("''Be Disciplined''")
def add_task():
    task=input("Enter task:")
    with open("todo.txt","a")as f:
        f.write(task+"\n")
        print("task added!")
def view_tasks():
    with open("todo.txt","r")as f:
        print("Your Tasks:")
        print(f.read())
def clear_tasks():
    with open("todo.txt","w")as f:
        f.write("")
        print("All tasks cleared!")
while True:
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Clear tasks")
    print("4.Exit")
    ch=input("Enter choice")
    if ch==1:
        add_task()
    if ch==2:
        view_tasks()
    if ch==3:
        clear_tasks()
    else:break
    