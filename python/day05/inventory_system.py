import json
def load_expenses(filename):
    try :
        with open(filename,"r") as f:
            a = json.load(f)
            return a
    except FileNotFoundError:
        return []
def save_expenses(filename, data):
    with open(filename,"w") as f:
        json.dump(data,f)
def add_expense(expenses):
    a = input("Enter item ")
    b = float(input("Enter amount "))
    c = input("Enter category ")
    d = {"item" : a , "amount" : b , "category" : c}
    expenses.append(d)
    save_expenses("expenses.json", expenses)

def view_expenses(expenses):
    for i in range(0,len(expenses)):
        print(f"{i+1}  {expenses[i]['item']} - {expenses[i]['amount']} - {expenses[i]['category']}")

def delete_expense(expenses):
    view_expenses(expenses)
    try:
        a = int(input("enter the index you want to remove "))
        expenses.pop(a-1)
        save_expenses("expenses.json", expenses)
    except(ValueError,IndexError):
        print("invalid value ")
    
def total_spending(expenses):
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    print("total spending = ", total)

def category_wise_spending(expenses):
    totals = {}
    for i in expenses:
        if i["category"] in totals:
            totals[i["category"]] += i["amount"]
        else:
            totals[i["category"]] = i["amount"]
    print(totals)

def edit_expense(expenses):
    view_expenses(expenses)
    flag = 1
    try:
            a = int(input("enter index you want to edit "))
            b = input("Do you want to edit amount / category / both ")
            if b == "amount":
                c = float(input("enter the new amount "))
                expenses[a-1]["amount"] = c
            elif b == "category":
                 c = input("enter the new category ")
                 expenses[a-1]["category"] = c
            elif b == "both":
                c = float(input("enter the new amount "))
                d = input("enter the new category ")
                expenses[a-1]["amount"] = c
                expenses[a-1]["category"] = d
            else: 
                print("Invalid choice") 
                flag = 0 
    except(ValueError,IndexError):
            print("invalid value ")
            flag = 0
    if flag == 1:
        save_expenses("expenses.json",expenses)
        
expenses = load_expenses("expenses.json")
flag = True 
while flag:
    print("Choices : 1) Add 2) View 3) Delete 4) Total 5) Category totals 6) Edit 7) Quit ")
    a = int(input("Enter your choice index : "))
    if a == 1:
        add_expense(expenses)
    elif a == 2:
        view_expenses(expenses)
    elif a == 3:
        delete_expense(expenses)
    elif a == 4:
        total_spending(expenses)
    elif a == 5:
        category_wise_spending(expenses)
    elif a== 6:
        edit_expense(expenses)
    elif a == 7:
        flag = False
        break
    else:
        print("Please enter a valid choice ")
