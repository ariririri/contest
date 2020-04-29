import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
#A = list(map(int, input().split()))
A = [(a, i) for i, a in enumerate(map(int, input().split()))]
A = sorted(A, reverse=True)

values = []
num_indcies = {}
for i, a in enumerate(A):
    if not a in num_indcies:
        num_indcies[a] = [i]
        values.append(a)
    else:
        num_indcies[a].append(i)

values = sorted(values, reverse=True)
ans = 0
# indexの配列
dp_indices = []
for v in values:
    dp_indices.extend(num_indcies[v])


dp = [[0] * (N+1) for _ in range(N+1)]
for no, (a, pos) in enumerate(A):
    for i in range(no+1):
        j = no - i
        #k = dp_indices[i+j-2]
        #a = A[k]
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + a * (pos -i))
        dp[i][j+1] = max(dp[i][j+1], dp[i][j] + a * abs(pos - (N-1-j)))

ans = 0
for i in range(1, N+1):
    ans = max(ans, dp[i][N-i])
print(ans)



