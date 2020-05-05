import sys
from queue import deque
input = sys.stdin.readline

def main():
    N, Q = list(map(int, input().split()))
    graph = [[] for i in range(N)]
    # 最初にroot pointを定めて:
    # graph構造に大して点を与える...
    for i in range(N-1):
        a, b = list(map(int, input().split()))
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    points = [0] * N
    for _ in range(Q):
        p, x = list(map(int, input().split()))
        points[p-1] += x
    
    visited = [False] * N
    
    nodes = deque([0])

    while nodes:
        node = nodes.pop()
        visited[node] = True
        for _node in graph[node]:
            if visited[_node]:
                continue
            points[_node] += points[node]
            nodes.append(_node)
    
    print(*points)
    
main()