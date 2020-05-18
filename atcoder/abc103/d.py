N, M = list(map(int,input().split()))

lists = []
for i in range(M):
    lists.append(list(map(int,input().split())))
lists.sort(key=lambda x: x[1])
ans = 0
min_b = 0
for a, b in lists:
    if min_b <= a:
        min_b = b
        ans += 1
print(ans)
    



