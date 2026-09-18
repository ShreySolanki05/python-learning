inventory = {}
#choice = ("Add stock","Remove stock","View inventory","Quit")
choice = "0"
while choice != "Quit":
    choice = input("Add stock,Remove stock,View inventory,Quit ")
    if choice == "Add stock":
        a = input("Enter item name:- ")
        b = int(input("Enter item quantity:- "))
        if a in inventory:
            inventory[a] += b
        else:
            inventory[a] = b    
    elif choice == "Remove stock":
        r = input("Enter item you want to remove :- ") 
        ri = int(input("Enter item quantity:- "))
        
        if r in inventory:
                if ri <= inventory[r]:
                    inventory[r] -= ri
                else:
                    print("Item exceeds storage")
        else:
            print("Item doesn't exist")
        
    elif choice == "View inventory":
        for key , value in inventory.items():
            print(f"{key}     {value}")
    elif choice == "Quit":
        break
        
    else:
        print("Enter valid choice ")



