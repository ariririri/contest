N = int(input())
As = list(map(int, input().split()))

sums = []
_sum = 0
for a in As:
    _sum += a
    sums.append(_sum)
for k in range(1,N+1):
    ans = sums[k-1]
    for j in range(0, N-k):
        ans = max(sums[j+k] - sums[j], ans)
    print(ans)


