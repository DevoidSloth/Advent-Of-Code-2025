with open('input.txt', 'r') as f:
    grid = f.read().splitlines()

for line in range(len(grid)):
    grid[line] = list(grid[line])

total = 0

for y, line in enumerate(grid):
    for x, c in enumerate(line):
        count = 0
        directions = [(0,1), (0, -1), (1, 0), (-1, 0), (1,1), (1,-1), (-1, 1), (-1, -1)]
        if(c == "@"):
            for direction in directions:
                if(0 <= y + direction[0] < len(grid) and 0 <= x+direction[1] < len(line)):
                    if(grid[y+direction[0]][x+direction[1]] == "@"):
                        count+=1
            if count < 4:
                total += 1
print(total)
            
    