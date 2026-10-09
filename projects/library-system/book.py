class Book:
    def __init__(self, title, author, available=True, times_borrowed=0):
        self.title = title 
        self.author = author 
        self.available = available
        self.times_borrowed = times_borrowed
    def checkout(self):
        if self.available:
            self.available = False
            self.times_borrowed += 1
        else:
            print("It's already checked out")
    def return_book(self):
        self.available = True
    def status(self):
        if self.available:
            return f"{self.title} by {self.author} is available to borrow "
        else:
            return f"{self.title} by {self.author} is currently borrowed by someone else "
    def to_dict(self):
        return {"title": self.title, "author": self.author, "available": self.available , "times_borrowed" : self.times_borrowed}        