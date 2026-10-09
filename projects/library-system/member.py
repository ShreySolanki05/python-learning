class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, title):
        self.borrowed_books.append(title)

    def return_book(self, title):
        if title in self.borrowed_books:
            self.borrowed_books.remove(title)
        else:
            print("This book title doesen't exist ")
    def to_dict(self):
        return {"name": self.name, "member_id": self.member_id,"borrowed_books" : self.borrowed_books}