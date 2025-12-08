with open('input.txt', 'r') as f:
    grid = f.read().splitlines()

def print_grid(grid):
    for line in grid:
        print(''.join(line))

for line_idx in range(len(grid)):
    grid[line_idx] = list(grid[line_idx])

splits = 0

for y in range(1, len(grid)):
    line = grid[y]
    for x in range(len(line)):
        above_element = grid[y-1][x]
        if above_element == "S" or above_element == "|":
            if grid[y][x] != "^":
                grid[y][x] = "|"
            else:
                grid[y][x-1] = grid[y][x+1] = "|"
                splits += 1

print_grid(grid)
print(f"Number of splits: {splits}")
        