def celsius_to_fahrenheit(c):
    return (c * 1.8) + 32
def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8
a = input("Your choice (c or f) ")
if a == "c":
    c = int(input("enter temp "))
    print(celsius_to_fahrenheit(c))
elif a == "f":
    f = int(input("enter temp"))
    print(fahrenheit_to_celsius(f))
else:
    print("invalid choice")