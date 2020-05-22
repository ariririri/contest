
import heapq
V, E ,r = list(map(int, input().split()))

INF = 10 ** 15

# ダイクストラのアルゴリズムは
def dijkstra(edges, s):
    d = [INF for x in range(V)]
    d[s] = 0
    que = []
    # 原点からの距離, ノードをpush
    heapq.heappush(que, (0,s))
    while len(que) > 0:
        u_d, u = heapq.heappop(que)
        # 既に最適化されたもの
        if d[u] < u_d:
            continue
        # uへの距離が確定したノード
        for v_d, v in edges[u]:
            # 今よりより距離があれば更新
            if d[v] > d[u] + v_d:
                d[v] = d[u] + v_d
                heapq.heappush(que,(d[v],v))
    return d

cost = [[] for i in range(V)]
#cost[u][v] : 辺uvのコスト(存在しないときはinf この場合は10**10)
for i in range(E):
    x, y, z = map(int,input().split())
    cost[x].append((z, y))
    #cost[y][x] = z
d = dijkstra(cost, r)
for c in d:
    if c == INF:
        print("INF")
    else:
        print(c)