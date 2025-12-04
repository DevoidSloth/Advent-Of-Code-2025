import time
with open('input.txt', 'r') as f:
    grid = f.read().splitlines()

for line in range(len(grid)):
    grid[line] = list(grid[line])

ti = time.time()
total = 0
removed_pos = []
removed = 1
while removed > 0:
    removed = 0
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
                    removed += 1
                    removed_pos.append((x,y))
                    
        for nx, ny in removed_pos:
            grid[ny][nx] = "."

    total += removed

tf = time.time()
print(total, f"Time to complete:  {tf-ti}s")