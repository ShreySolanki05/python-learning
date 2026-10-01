class Book:
    def __init__(self, title, author, available=True):
        self.title = title 
        self.author = author 
        self.available = available
    def checkout(self):
        if self.available:
            self.available = False
        else:
            print("It's already checked out")
    def return_book(self):
        self.available = True
    def status(self):
        if self.available:
            return f"{self.title} by {self.author} is available to borrow "
        else:
            return f"{self.title} by {self.author} is currently borrowed by someone else "

b1 = Book("hxh","t")
b2 = Book("ss","dd",False)
b3 = Book("maths","RD",True)
print(b1.status())
print(b2.status())
print(b3.status())
b2.return_book()
print(b2.status())
b3.checkout()
print(b3.status())
b3.checkout()
print(b3.status())