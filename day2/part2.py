import math

with open('input.txt', 'r') as f:
    ranges = f.read().split(",")
    
total = 0

for r in ranges:
    f, t = int(r[:r.index('-')]), int(r[r.index('-')+1:])+1
    for i in range(f,t):
        cutpt = int(math.log10(i) +1) // 2
        slider_len = 1
        slider_pos = 0
        string_num = str(i)
        patterns = set()
        correct = set()
        while slider_len <= cutpt:
            # print(string_num[slider_pos: slider_pos+slider_len], slider_pos, slider_len)
            patterns.add(string_num[slider_pos: slider_pos+slider_len])
            slider_pos += slider_len
            if(slider_pos > len(string_num)-slider_len):
                slider_len+=1
                slider_pos = 0
                if(len(patterns) == 1 and len(string_num) % (slider_len-1) == 0):
                    correct.add(i)
                    # print(i, patterns, slider_len, len(string_num))
                patterns = set()
        for c in correct:
            total += c
            print(c)
    
print(total)