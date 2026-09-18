notdone = True
phonebook = {}
while notdone:
    a = input("Enter name :- ")
    
    if a == "done":
        notdone = False
        break
    b = int(input("Enter number :- "))
    phonebook[a]=b
        
print(phonebook)
d = input("Enter the name you want to inquire about :- ")
print(phonebook.get(d,"not found"))