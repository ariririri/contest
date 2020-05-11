import heapq
N, K =list(map(int, input().split()))
graphs = [[] for _ in range(N)]
INF = 10 ** 15

def dijkstra(edges, s):
    d = [INF for x in range(N)]
    d[s] = 0
    que = []
    heapq.heappush(que, (0,s))
    while len(que) > 0:
        u_d,u = heapq.heappop(que)
        if d[u] < u_d:
            continue
        for  v_d,v in edges[u]:
            if d[v] > d[u] + v_d:
                d[v] = d[u] + v_d
                # 重みは引数順にする.
                heapq.heappush(que,(d[v], v))
    return d

for i in range(K):
    line = list(map(int, input().split()))
    if line[0] == 0:
        d = dijkstra(graphs, line[1]-1)
        if d[line[2]-1] == INF:
            print(-1)
        else:
            print(d[line[2]-1])
    else:
        _, s, e, v = line
        graphs[s-1].append((v, e-1))
        graphs[e-1].append((v, s-1))