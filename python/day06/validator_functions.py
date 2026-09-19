def is_valid_age(age):
    return age > 0 and age <= 120
def is_valid_email(email):
    return "@" in email and "." in email
def is_strong_password(password):
    if len(password) >= 8:
        for char in password:
            if char.isdigit():
                return True
        return False
    else:
        return False

age = int(input("enter age "))
if is_valid_age(age):
    print("Valid age")
else:
    print("Invalid age")

email = input("Email :- ")
if is_valid_email(email):
    print("Valid email")
else:
    print("Invalid email")

password = input("Password :- ")
if is_strong_password(password):
    print("Strong password ! You can continue")
else:
    print("Weak password ! You need to think of a stronger password and try again.")
