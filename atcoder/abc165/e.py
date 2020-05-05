n, m = list(map(int, input().split()))

for i in range(1, m+1):
    if i % 2 == 0:
        print(i//2, i// 2 + m + 1 - i)
    else:
        print(n - i//2, n - i//2 - (m + 1 - i))
