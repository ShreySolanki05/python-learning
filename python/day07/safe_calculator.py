def ask():
    try :
        a = int(input("enter first number "))
        b = int(input("enter second number "))
        return a , b
    except ValueError:
        print("Enter valid number")
        return ask()

c , d = ask()

op = input("enter the operator")

if op == "+":
   print(c + d)

elif op == "-":
    print(c-d)

elif op == "*":
    print(c*d)

elif op == "/":
    try:
        print(c/d)
    except ZeroDivisionError:
        print("number cannot be divided by zero")

else:
    print("enter valid operator")
 