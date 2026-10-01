class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year 
    def describe(self):
        return f" The car is made by {self.make} and it is {self.model} model from the year {self.year}"

c1 = Car("hyundai", "Aura",2022)
c2 = Car("hyundai", "i20",2021)
c3 = Car("Suzuki", "Alto",2012)

print(c1.describe())
print(c2.describe())
print(c3.describe())