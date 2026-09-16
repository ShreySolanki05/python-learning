n = int(input("enter no "))
count = 0
candidate = 2
while count < n:
    isprime = True
    for i in range(2,candidate):
        if candidate % i == 0:
            isprime = False
            break
        
    if isprime == True:
        print(candidate)
        count = count + 1
    candidate = candidate + 1
    
        


   

    