data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
data_set = set()
for d in data:
    data_set.add(d)
print(data_set)
data_list = sorted(data_set)
print(f"sorted list : {data_list}")
print(len(data_set))
x = int(input("enter number to check "))
if x in data_set:
    print(True)
else:
    print(False)

data_set.discard(7)
print(f"new set = {data_set}")
try:
    data_set.remove(7)
except KeyError:
    print("7 isn’t in the set")    
