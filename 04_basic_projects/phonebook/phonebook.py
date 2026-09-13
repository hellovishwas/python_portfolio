choice=0
name=[]
phone=[]
l=['1','2','3','4','5']
while(choice!='5'):
    print("------------Phonebook Menu---------------")
    print('1.Add contact')
    print("2.Dispay contact")
    print("3.Delete contact")
    print('4.search contact')
    print("5.Exit")
    print("------------------------------------------")
    choice=input("Enter your choice:")
    if choice=="1":
        nm=input("Enter your name:")
        ph=int(input('Enter your number:'))
        if ph in phone:
             print("this no. is already saved ")
        
        else:
            phone.append(ph)
            name.append(nm)
    elif choice=='2':
        for i in range (len(name)):

            print("name = %s and phone number = %d"% (name[i] , phone[i]))
    elif choice=='3':
        nm=input("Enter name for delete:")
        if nm not in name:
             print("This contact is not available")
        else:
             i=name.index(nm) 
             name.pop(i)
             phone.pop(i)
             print("record deleted succesfully")
                
           
    elif choice=='4':
                nm=input("Enter name for search:")
                if nm not in name:
                    print("This contact is not available")
             
                for i in range (len(name)):
                    if name[i]==nm:
                        print(f"contact no. of {nm} is:{ph}" )           
    elif choice not in l:
        print("Invalid choice")       



        