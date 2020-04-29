import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))

ans = 0
over = 0
down = 0
for i in range(N+1):
    over +=  N  - i
    down += i
    if i >= K-1:
        ans += over - down + 1
print(ans % (10 ** 9 + 7))
