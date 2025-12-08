import math

with open('input.txt', 'r') as f:
    grid = f.read().splitlines()

line_1_nums = list(map(int, grid[0].split()))
line_2_nums = list(map(int, grid[1].split()))
line_3_nums = list(map(int, grid[2].split()))
line_4_nums = list(map(int, grid[3].split()))
operators= list(grid[4].split())

total = 0    


for i in range(len(line_1_nums)):

    allignment = -1 if math.log10(line_1_nums[i]) > math.log10(line_4_nums[i]) else 1

    if(operators[i] == '*'):
        nums = [line_1_nums[i], line_2_nums[i], line_3_nums[i], line_4_nums[i]]
        print(nums)
        max_digits = int(max([math.log10(n) for n in nums])) + 1
        str_nums = list(map(str, nums))
        new_nums = []
        if allignment == 1:


