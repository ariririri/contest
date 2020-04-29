from collections import defaultdict
import queue
N = int(input())

d = defaultdict(lambda: defaultdict(int))
for i in range(N-1):
    u, v, w = list(map(int, input().split()))
    d[u-1][v-1] = w
    d[v-1][u-1] = w
for i in range(N):
    if len(d[i]) == 1:
        start = i
        break

visited = [False for _ in range(N)]
visited[start] = True
all_length =  [0 for _  in range(N)]
q = queue.Queue()
q.put(start)
while not q.empty():
    i = q.get()
    for v, w in d[i].items():
        if not visited[v]:
            q.put(v)
            visited[v] = True
            all_length[v] = all_length[i] + w
for length in all_length:
    print(length % 2)


