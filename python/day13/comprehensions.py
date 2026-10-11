numbers = list(range(1, 21))
words = ["apple", "kiwi", "banana", "fig"]
loop_sq = []
for n in numbers:
    loop_sq.append(n*n)
comp_sq = [n*n for n in numbers]
print(loop_sq == comp_sq)

loop_even = []
for n in numbers:
    if n % 2 == 0:
        loop_even.append(n)
comp_even = [ n for n in numbers if n % 2 == 0]
print(loop_even == comp_even)

loop_oddsq = []
for n in numbers:
    if n % 2 != 0:
        loop_oddsq.append(n*n)
comp_oddsq = [n*n for n in numbers if n % 2 != 0]
print(loop_oddsq == comp_oddsq)

loop_len = []
for w in words:
    loop_len.append(len(w))
comp_len = [len(w) for w in words]
print(loop_len == comp_len)