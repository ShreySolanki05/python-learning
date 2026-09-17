done = False
nums = []
while not done:
    a = input("Enter number :- ")
    if a == "done":
        done = True
        break
    else:
        nums.append(int(a))
mini = nums[0]
maxi = nums[0]    

for n in nums:
    
    if n > maxi:
        maxi = n
    if n < mini:
        mini = n

print(f"""
max = {maxi}
min = {mini} """)
    