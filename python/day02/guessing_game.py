secret = 7
a = int(input("Enter your guess "))
while a != secret:
    
    if a > secret:
        print("Too high")
    else:
        print("Too low")
    a = int(input("Enter your guess "))
print("Correct!")