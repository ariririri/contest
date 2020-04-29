import sys
import numpy as np
input = sys.stdin.readline
 
S = input().strip()
l = len(S)
dp = np.zeros((l, 2019), dtype=int)
for i in range(l):
    s = int(S[i])
    for j in range(2019):
        k = (10 * j + s) % 2019
        dp[i][k] = dp[i-1][j]
    dp[i][s] += 1
 
print(dp[:, 0].sum())