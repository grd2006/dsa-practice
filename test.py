n = int(input())
coins = list(map(int, input().split()))
for i in range(n):
    for j in range(i + 1, n):
        if coins[i] < coins[j]:
            coins[i], coins[j] = coins[j], coins[i]
total = sum(coins)
mysum = 0
count = 0
for coin in coins:
    mysum += coin
    count += 1
    if mysum > total - mysum:
        break
print(count)