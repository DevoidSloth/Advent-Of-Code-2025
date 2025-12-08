with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

lb_ub_pairs = []
finindex = 0
total = 0
solutions = set()

for line in lines:
    if("-" not in line):
        break
    lbub = (int(line[:line.index('-')]), int(line[line.index('-')+1:])+1)
    lb_ub_pairs.append(lbub)

finindex = lines.index("")

for i, line in enumerate(lines[finindex+1:]):
    for pair in lb_ub_pairs:
        if pair[0] <= int(line) <= pair[1]:
            solutions.add(int(line))
    
print(len(solutions))