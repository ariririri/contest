N, M = list(map(int, input().split()))

points = []
ans = 0
for i in range(N):
    points.append(list(map(int, input().split())))

for j in range(M):
    for k in range(M):
        temp = 0
        for i in range(N):
            temp += max(points[i][j], points[i][k])
        ans = max(ans, temp)

print(ans)