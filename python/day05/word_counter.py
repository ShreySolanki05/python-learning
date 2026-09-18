a = input("Enter sentence ")
b = a.split()
d = {}
for i in b:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)