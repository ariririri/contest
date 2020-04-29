from sys import stdin
input = stdin.readline

N, M = list(map(int, input().split()))

flag = [0 for _ in range(N)]
#memo = [[0] for i in range(3) for _ in range(N)]
for i in range(M):
    x, y = list(map(int, input().split()))
    flag[x-1] = y

dp = [[0 for i in range(3)] for _ in range(N)]

if flag[0]:
    dp[0][flag[0]-1] = 1
else:
    dp[0][0] = 1
    dp[0][1] = 1
    dp[0][2] = 1

for i in range(1, N):
    if flag[i]:
        x = flag[i]
        for j in range(3):
            if j != x-1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][(j+1)%3] + dp[i-1][(j+2) % 3]
                if dp[i-1][j] != 0 and i == 2:
                    dp[i][j] -= dp[i-2][j]
                elif i >= 3 and dp[i-1][j] * dp[i-2][j] != 0:
                    dp[i][j] -= dp[i-3][(j+1)%3] + dp[i-3][(j+2) % 3]
    else:
        for j in range(3):
            dp[i][j] = dp[i-1][j] + dp[i-1][(j+1)%3] + dp[i-1][(j+2) % 3]
            if dp[i-1][j] != 0 and i == 2:
                dp[i][j] -= dp[i-2][j]
            elif i >= 3 and dp[i-1][j] * dp[i-2][j] != 0:
                dp[i][j] -= dp[i-3][(j+1)%3] + dp[i-3][(j+2) % 3]

print(sum(dp[-1]) % 10000)