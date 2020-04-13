N, M = list(map(int, input().split()))
K = [[0 for _ in range(N)] for _ in range(M)]
for i in range(M):
    for x in list(map(int, input().split()))[1:]:
        K[i][x-1] = 1
p = list(map(int, input().split()))

ans = 0
for i in range(2 ** N):
    flag = True
    for m in range(M):
        _sum = 0
        for j in range(N):
            if i >> j & 1:
                _sum += K[m][j]
        if (_sum % 2) != p[m]:
            flag = False
            break
    if flag:
        ans += 1
print(ans)


