with open('secret.txt', 'r') as file:
    secret_data = file.read().splitlines()
    
dp = 50
n = 0

for line in secret_data:
    num = 1 if line[0] == "R" else -1    
    delta = int(line[1:])*num
    dp += delta  
    if(dp-delta == 0 and abs(delta) >= 100):
        n += int(abs(delta) // 100)
    elif(dp == 0):
        n += 1+ int(abs(delta) // 100)
    elif(dp<0 and dp - delta != 0):    
        n += int(1 + abs(dp) // 100)
    elif(dp >= 100):
        n += dp // 100
    
    dp %= 100

print(n)