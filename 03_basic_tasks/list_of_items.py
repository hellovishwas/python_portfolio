my_list=[]
print("Your list")
print("1.Display items of list\n2.Add new item in list\n3.remove new item in list\n4.Exit")
choice=0
while choice!="4":
    choice=input("Enter your choice:")
    if choice=="1":
        if len(my_list)==0:
            print("There is no items present in this list yet.")
        else:
            j=1
            for i in my_list:
                print(f"{j}. ",i)
                j=j+1
    elif choice=="2":
        a=input("Enter item to add in list:" )
        if a not in my_list:
            my_list.append(a)
            print("New item is successfully added")
        else:print("This item is already present in your list.")
        
    elif choice=="3":
        a=input("Enter item to remove from list:" )
        if a in my_list:
            my_list.remove(a)
            print("New item is successfully removed")
        else:print(f"{a} is not present in your list.")
            
    elif choice=="4":
        print("Have a nice day")
    else:
        print("Invalid input")
        print("Please read instructions carefully")
        print("1.Display items of list\n2.Add new item in list\n3.remove new item in list\n4.Exit")