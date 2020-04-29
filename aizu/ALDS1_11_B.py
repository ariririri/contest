n = int(input())
trees = [[]]
for i in range(n):
    edges = []
    s = list(map(int, input().split()))
    num = s[1]
    if s[1] != 0:
        edges = s[2:2+num]
    trees.append(edges)

d = [0] * (n+1)
f = [0] * (n+1)


def dfs(x, i=0):
    for y in trees[x]:
        if d[y] != 0:
            continue
        d[y] = i
        i += 1
        i = dfs(y, i)
    f[x] = i
    i += 1
    return i


i = 1
for j in range(1, n+1):
    if d[j] != 0:
        continue
    else:
        d[j] = i
        i += 1
    i = dfs(j, i)
for i in range(1, n+1):
    print(i, d[i], f[i])