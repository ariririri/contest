N, M, X = list(map(int, input().split()))
costs = []
As = []
for i in range(N):
    t = list(map(int, input().split()))
    costs.append(t[0])
    As.append(t[1:])
ans = -1
for i in range(2 ** N):
    tot = [0] * M
    cost = 0
    for j in range(N):
        if i >> j & 1:
            cost += costs[j]
            for k in range(M):
                tot[k] += As[j][k]
        flag = True
        for k in range(M):
            if tot[k] < X:
                flag = False
        if flag:
            if ans < 0:
                ans = cost
            else:
                ans = min(ans, cost)
print(ans)