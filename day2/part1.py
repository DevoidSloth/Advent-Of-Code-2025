import math

with open('input.txt', 'r') as f:
    ranges = f.read().split(",")
    
total = 0

for r in ranges:
    f, t = int(r[:r.index('-')]), int(r[r.index('-')+1:])+1
    for i in range(f,t):
        cutpt = int(math.log10(i) +1) // 2
        if(str(i)[:cutpt] == str(i)[cutpt:]):
            print(i)
            total += i
    
print(total)