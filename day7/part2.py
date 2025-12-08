from functools import lru_cache

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

@lru_cache(maxsize=None)
def trace_paths(row, col, depth=0):
    if row >= len(grid) - 1:
        return 1

    for next_row in range(row + 1, len(grid)):
        line = grid[next_row]

        if col >= len(line):
            return 0

        char = line[col]

        if char == "^":
            left_paths = trace_paths(next_row, col-1, depth+1)
            right_paths = trace_paths(next_row, col+1, depth+1)
            return left_paths + right_paths
        elif char == "|":
            continue
        elif char == ".":
            return 0
    
    return 1


total = trace_paths(0, grid[0].index("S"))

print(f"Number of timelines: {total}")