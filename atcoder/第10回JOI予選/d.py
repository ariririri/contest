from sys import stdin
from collections import defaultdict
input = stdin.readline


N = int(input())
xs = list(map(int, input().split()))
inp = xs[:-1]

totals = []
_tot = 0
for x in xs:
    _tot += x
    totals.append(_tot)
dp = [defaultdict(int) for _ in inp]
dp[0][xs[0]] = 1
for i in range(1, len(inp)):
    for tot, num in dp[i-1].items():
        if tot + xs[i] <= 20:
            dp[i][tot + xs[i]] += num
        if tot - xs[i] >= 0:
            dp[i][tot - xs[i]] += num

print(dp[-1][xs[-1]])

