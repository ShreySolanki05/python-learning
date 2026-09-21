done = True
c = ""
while done:
    a = input("enter text ")
    if a == "done":
     done = False
    else:
        c = c + a + "\n"
with open("notes.txt","w") as f:
   f.write(c)
 
            
with open("notes.txt","r") as f:
    b = f.read()
    print(b)


