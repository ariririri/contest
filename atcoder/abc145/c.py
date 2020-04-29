import itertools
import math
N = int(input())

D = []
for i in range(N):
    D.append(list(map(int, input().split())))



l = list(range(N))
total = 0
dist = 0
for i, v in enumerate(itertools.permutations(l, N)):
    total += 1
    old_j = v[0]
    for j in v[1:]:
        dist += math.sqrt((D[j][0] - D[old_j][0]) ** 2 + (D[j][1] - D[old_j][1]) ** 2)

print(dist / total)
 