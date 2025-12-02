with open('secret.txt', 'r') as file:
    secret_data = file.read().splitlines()
    
dp = 50
n = 0

for line in secret_data:
    num = 1 if line[0] == "R" else -1
    dp += int(line[1:])*num % 100
    dp %= 100
    if(dp < 0):
        dp += 100
    if(dp==0): 
        n+=1

print(n)