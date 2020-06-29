n, k = map(int, input().split())
coins = []
dp = [0] * 100001
for i in range(n):
    coins.append(int(input()))
    dp[coins[i]] = 1

for i in range(1, k+1):
    for coin in coins:
        if i + coin <= k and dp[i]:
            if not dp[i+coin]:
                dp[i+coin] = dp[i]+1
            else:
                dp[i+coin] = min(dp[i+coin], dp[i]+1)

if dp[k]:
    print(dp[k])
else:
    print(-1)
