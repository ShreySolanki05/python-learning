def get_stats(numbers):
    return sum(numbers) , max(numbers) , min(numbers) , sum(numbers)/len(numbers)
total , maxi , mini , average = get_stats([2,3,6,8,12,9,1,4,7])
print(f"""sum = {total}
max = {maxi}
min = {mini}
average = {average} """)