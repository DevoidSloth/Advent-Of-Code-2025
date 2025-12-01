import math

with open('secret.txt', 'r') as file:
    secret_data = file.read().splitlines()

total = 50
n=0

for line in secret_data:
    num = 1 if line[0] == "R" else -1
    total = total % 100
    
    for i in range(int(line[1:])):
        total += num
        total = total % 100


        if(total == 0):
            n+=1
        print(total)

print(n)