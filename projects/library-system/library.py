from book import Book
from member import Member
import json

class Lib:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        self.books.append(Book(title,author))

    def register_member(self, name, member_id):
        self.members.append(Member(name,member_id))

    def remove_book(self, title):
        is_found = False
        for book in self.books:
            if title == book.title:    
                self.books.remove(book) 
                is_found = True 
        if not is_found:          
            print("Book unavailable")    

    def search_books(self, keyword):
        is_found = False
        for book in self.books:
            if keyword in book.title  or keyword in book.author:
                print(book.status())
                is_found = True 
        if not is_found:              
            print("no results found")

    def view_books(self):
        for book in self.books:
            print(book.status())

    def view_members(self):
        for member in self.members:
            print(f"member name : {member.name} , member_id : {member.member_id} , borrowed books : {member.borrowed_books}")

    def issue_book(self, title, member_id):
        chosen_book = None
        chosen_member = None
        for book in self.books:
            if book.title == title:
                if book.available:
                    chosen_book = book
                    break
                else: 
                    chosen_book = False
        for member in self.members:
            if member.member_id == member_id:
                chosen_member = member

        if chosen_book and chosen_member:
           chosen_book.checkout()
           chosen_member.borrow_book(chosen_book.title) 
        elif chosen_book is None and chosen_member is not None:
            print("Book not found or unavailable")
        elif chosen_book == False:
            print("book found but is unavailable")
        elif chosen_book is not None and chosen_member is None:
            print("Incorrect member ID")
        else:
            print("Unavailble book and incorrect member id")

    def return_book(self, title, member_id):
        chosen_book = None
        chosen_member = None
        for book in self.books:
            if book.title == title:
                chosen_book = book
                break
        for member in self.members:
            if member.member_id == member_id:
                chosen_member = member
        
        if chosen_book and chosen_member:
            if chosen_book.title in chosen_member.borrowed_books:
                chosen_book.return_book()
                chosen_member.return_book(chosen_book.title)
            else:
                print("this member hasn't borrowed that book")
        else:
            print("either book name is incorrect or wrong member information ")

    def save_to_file(self, filename):
       book_records = []
       member_records = []
       for book in self.books:
           book_records.append(book.to_dict())
       for member in self.members:
           member_records.append(member.to_dict())
       data = {"books" : book_records , "members" : member_records}
       with open(filename,"w") as f:
           json.dump(data,f)
       
    def load_from_file(self, filename):
        try :
            with open(filename,"r") as f:
                a = json.load(f)
                for i in a["books"]:
                    self.books.append(Book(i["title"],i["author"],i["available"],i.get("times_borrowed",0)))
                for i in a["members"]:
                    m = Member(i["name"], i["member_id"])
                    m.borrowed_books = i["borrowed_books"]
                    self.members.append(m)
        except FileNotFoundError:
            pass

    def most_borrowed_book(self):
        try:
            famemaxer = self.books[0]
            for book in self.books:
                if famemaxer.times_borrowed <= book.times_borrowed:
                    famemaxer = book
            if famemaxer.times_borrowed == 0:
               print("no books have yet been issued ")
            else:           
               print(f"Most popular book is {famemaxer.title} with total issues of {famemaxer.times_borrowed}")
        except IndexError:
            print("no books available")
            
                




