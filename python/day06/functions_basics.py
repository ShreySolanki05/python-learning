def square(n):
    return n*n

def is_even(n):
    return n % 2 == 0
def greet(name, greeting="Hello"):
    return f"{greeting} {name} , how are you doing ? "

print(square(8))
print(is_even(27))
print(greet("raz"))
print(greet("raz","hola"))