with open('input.txt', 'r') as f:
    grid = f.read().splitlines()

line_1_nums = list(map(int, grid[0].split()))
line_2_nums = list(map(int, grid[1].split()))
line_3_nums = list(map(int, grid[2].split()))
line_4_nums = list(map(int, grid[3].split()))
operators= list(grid[4].split())


print(line_1_nums, line_2_nums, line_3_nums, operators)

total = 0

for i in range(len(line_1_nums)):
    if operators[i] == '+':
        total += line_1_nums[i] + line_2_nums[i] + line_3_nums[i] + line_4_nums[i]
    if operators[i] == '*':
        total += line_1_nums[i] * line_2_nums[i] * line_3_nums[i] * line_4_nums[i]

print(total)