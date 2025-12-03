with open('input.txt', 'r') as f:
    nums = f.read().splitlines()

total = 0    

for num in nums:
    l = list(map(int, list(str(num))))
    n1 = max(l)
    
    if(l.index(n1) != len(l)-1):
        n2 = max(l[l.index(n1)+1:])
    else:
        n1 = max(l[:-1])
        n2 = l[-1]
    
    total +=  n1 * 10 + n2

print(total)
    