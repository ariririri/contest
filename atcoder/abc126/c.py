N, K = list(map(int, input().split()))
val = 1
num = 0
ans = 0

x = 1
while x < K:
    x = 2 * x

for i in range(N):
    target = N - i
    tmp = val
    while tmp * target < K:
        num += 1
        tmp = 2 * tmp
    val = tmp
    ans += x // tmp
print('{:.10g}'.format(ans / (N * x)))


