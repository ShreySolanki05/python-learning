from library import Lib

library = Lib()
library.load_from_file("library_records.json")

flag = True 
while flag:
    print("Choices : 1) Add Book 2) Remove Book 3) Register Member 4) Issue Book 5) Return Book 6) Search Books 7) View Books 8) View Members 9) View most popular book 10) Quit ")
    try:
        a = int(input("Enter your choice index : "))
    except ValueError:
        print("enter a numeric value")
        continue    
    if a == 1:
        t = input("enter book title ").strip()
        auth = input("enter author name ").strip()
        library.add_book(t,auth)
        library.save_to_file("library_records.json")

    elif a == 2:
        t = input("enter book title ").strip()
        library.remove_book(t)
        library.save_to_file("library_records.json")

    elif a == 3:
        n = input("enter member name ").strip()
        mem_id = input("enter member id ").strip()
        library.register_member(n,mem_id)
        library.save_to_file("library_records.json")

    elif a == 4:
        t = input("enter book title ").strip()
        mem_id = input("enter member id ").strip()
        library.issue_book(t,mem_id)
        library.save_to_file("library_records.json")

    elif a == 5:
        t = input("enter book title ").strip()
        mem_id = input("enter member id ").strip()
        library.return_book(t,mem_id)
        library.save_to_file("library_records.json")

    elif a == 6:
        k = input("enter keyword ").strip()
        library.search_books(k)

    elif a == 7:
        library.view_books()

    elif a == 8:
        library.view_members()

    elif a == 9:
        library.most_borrowed_book()
        
    elif a == 10:
        flag = False

    else:
        print("please enter a valid choice ")