class BankAccount:
    def __init__(self, owner, _balance=0):
        self.owner = owner 
        self._balance = _balance
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Amount should be greater than 0 ") 
    def withdraw(self, amount): 
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance ")
    def get_balance(self):
        return self._balance

b1 = BankAccount("ss", 25000000)
print(b1.get_balance())
b1.withdraw(30000000)
print(b1.get_balance())
b1.withdraw(300000)
print(b1.get_balance())
b1.deposit(44444)
print(b1.get_balance())
b1._balance = -99999
print(b1.get_balance()) #-99999
#as the data inside of the class can be changed outside this proves py does not provide security

