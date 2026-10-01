class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner 
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount 
    def withdraw(self, amount): 
        if amount <= self.balance:
            self.balance -= amount

        else:
            print("Insufficient balance ")
    def get_balance(self):
        return self.balance

b1 = BankAccount("ss", 25000000)
print(b1.get_balance())
b1.withdraw(30000000)
print(b1.get_balance())
b1.withdraw(300000)
print(b1.get_balance())
b1.deposit(44444)
print(b1.get_balance())
        