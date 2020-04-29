n, m = list(map(int, input().split()))

cs = list(map(int, input().split()))
_max = 10 ** 1000

dp = [_max for _ in range(n+1)]
dp[1] = 1
dp[0] = 0

for i in range(2, n+1):
    for c in cs:
        if i-c >= 0:
            dp[i] = min(dp[i], dp[i-c]+1)

print(dp[n])
 