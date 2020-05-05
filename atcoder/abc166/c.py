N, M = list(map(int, input().split()))
H = list(map(int, input().split()))
graphs = [[] for i in range(N)]
for i in range(M):
    a, b = list(map(int, input().split()))
    graphs[a-1].append(b-1)
    graphs[b-1].append(a-1)

ans = 0
for i in range(N):
    h = H[i]
    flag = True
    for b in graphs[i]:
        if H[b] >= h:
            flag = False
            break
    if flag:
        ans += 1
print(ans)
        
