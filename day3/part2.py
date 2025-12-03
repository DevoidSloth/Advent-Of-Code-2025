with open('input.txt', 'r') as f:
    nums = f.read().splitlines()

total = 0
    
for num in nums:
    l = list(map(int, list(str(num))))
    start_idx = 0
    nums_remaining = 12
    selected_nums = []
    while nums_remaining > 0:
        l_sub = l[start_idx:len(l)-nums_remaining+1]
        selected_nums.append(max(l_sub))
        start_idx = start_idx + l[start_idx:].index(max(l_sub)) +1
        nums_remaining-=1

    total += (int(str(''.join(list(map(str, selected_nums))))))

print(total)