s = int(input("Enter your score :- "))

if s >= 0 and s <=100:
    if s >= 90:
        print("A")
    elif s >= 80:
        print("B")
    elif s >= 50:
        print("C")
    elif s >=33 :
        print("D")
    else:
        print("F")
else:
    print("Invalid Score")   