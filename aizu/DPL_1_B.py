N, W = list(map(int, input().split()))

values = []
weights = []

for i in range(N):
    v, w = list(map(int, input().split()))
    values.append(v)
    weights.append(w)

dp = [[0 for i in range(W+1)] for j in range(N+1)]

for i in range(1, N+1):
    for j in range(1, W+1):
        w = weights[i-1]
        v = values[i-1]

        if j >= w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j- w] + v)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][W])