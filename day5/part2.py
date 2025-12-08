with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

lb_ub_pairs = []
finindex = 0
total = 0
solutions = set()

for line in lines:
    if("-" not in line):
        break
    lbub = (int(line[:line.index('-')]), int(line[line.index('-')+1:]))
    lb_ub_pairs.append(lbub)

def combine_ranges(orig1, orig2, apply1, apply2):
    a = [orig1, orig2]
    upd = False
    if(apply1 < orig1 and apply2 >= orig1):
        a[0] = apply1
        upd = True
    if(apply2 > orig2 and apply1 <= orig2):
        a[1] = apply2 
        upd = True
    return a, upd

updated_ranges = [lb_ub_pairs[0]]

# print(updated_ranges)

did_update = True

idx = 0


while did_update:
    for c in lb_ub_pairs:
        a, upd = combine_ranges(updated_ranges[idx][0], updated_ranges[idx][1], c[0], c[1])
        did_update = did_update or upd
        if(upd):
            updated_ranges[idx] = a
        else:
            updated_ranges.append([c[0], c[1]])
    idx += 1
    idx %= len(updated_ranges) 
    print(updated_ranges)


print(updated_ranges)