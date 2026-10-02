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

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate 

    def add_interest(self):
        self.deposit(self._balance * self.interest_rate)
s = SavingsAccount("Randy",4000)
print(s.get_balance())
s.add_interest()
print(s.get_balance())