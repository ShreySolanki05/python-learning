a = ""
done = False
shoppingList = []
count = 0
while not done:
    a = input("Enter item name :- ")
    if a == "done":
        done = True
        break
    else:
        shoppingList.append(a)
        count += 1

for i in range(0,len(shoppingList)):
    print(f"{i+1}    {shoppingList[i]}")

print(F"count = {count}")





