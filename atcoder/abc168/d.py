from collections import deque


def main():
    N, M = list(map(int, input().split()))
    graphs = [[] for i in range(N)]
    for i in range(M):
        a, b = list(map(int, input().split()))
        graphs[a-1].append(b-1)
        graphs[b-1].append(a-1)

    INF = 100000000

    distance = [INF for i in range(N)]
    visited = [False] * N
    #    distance = [[None]*field_x_length]*field_y_length
    visited[0] = True
    distance[0] = 0

    def bfs():
        queue = deque([0])
        distance[0] = 0

        while queue:
            x = queue.popleft()
            for y in graphs[x]:
                if visited[y]:
                    continue
                else:
                    distance[y] = x
                    visited[y] = True
                    queue.append(y)
        return distance

    d = bfs()
    for i in range(N):
        if not visited[i]:
            print("No")
            exit()
    print("Yes")
    for i in range(1, N):
        print(d[i]+1)

if __name__ == "__main__":
    main()