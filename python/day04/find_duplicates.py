data = [4, 8, 2, 8, 5, 4, 9, 2, 2]
list1 = []
for i in range(0,len(data)):
    
    a = data.count(data[i])
    if a > 1:
        if data[i] in list1:
            continue
        else:
            list1.append(data[i])
    
print(list1)
    

    

    




        

