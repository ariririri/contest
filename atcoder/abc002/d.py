N, M = list(map(int, input().split()))

rel = [[0 for _ in range(N)] for _ in range(N)]

for i in range(M):
    x, y = list(map(int, input().split()))
    rel[x-1][y-1] = 1
    rel[y-1][x-1] = 1

ans = 0
for i in range(2**N):
    team = []
    flag = True
    for j in range(N):
        if i >> j & 1:
            if len(team) == 0:
                team.append(j)
                continue
            for k in team:
                if rel[k][j] == 0:
                    flag = False
                    break
            team.append(j)
            if not flag:
                break
    if flag:
       ans = max(ans, len(team))

print(ans)

