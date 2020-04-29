N, M = list(map(int, input().split()))

Ts = [int(input()) for _ in range(N)]

values = [0 for j in range(M)]
cloths = [[0 for _ in range(61)] for j in range(M)]
for i in range(M):
    min_t, max_t, p = list(map(int, input().split()))
    for t in range(min_t, max_t+1):
        cloths[i][t] = 1
    values[i] = p

# 服×日
dp = [[0 for _ in range(M)] for _ in range(N)]
for i in range(1, N):
    for j in range(M):
        if cloths[j][Ts[i]]:
            cost = 0
            for k in range(M):
                if cloths[k][Ts[i-1]]:
                    cost = max(cost, dp[i-1][k] + abs(values[k] - values[j]))
            dp[i][j] = cost
print(max(dp[-1]))