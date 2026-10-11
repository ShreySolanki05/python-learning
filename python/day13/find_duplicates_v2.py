data = [4, 8, 2, 8, 5, 4, 9, 2, 2]
seen = set()
duplicate = set()
for d in data:
    if d in seen:
        duplicate.add(d)
    else:
        seen.add(d)

print(f"duplicate values are {sorted(duplicate)}")

''' def save_to_file(self, filename):
       book_records = []
       member_records = []
       for book in self.books:
           book_records.append(book.to_dict())
       for member in self.members:
           member_records.append(member.to_dict())
       data = {"books" : book_records , "members" : member_records}
       with open(filename,"w") as f:
           json.dump(data,f)'''