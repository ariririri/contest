N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

def get_loop_num(start, last):
    x = start
    loops = [start]
    for i in range(K):
        x = A[x-1]
        loops.append(x)
        if x == last:
            return loops

loop_check = [False] * N
loop_check[0] = True
x = 1
for i in range(K):
    new_x = A[x-1]
    if loop_check[new_x-1]:
        start = new_x
        last = x
        loops = get_loop_num(start, last)
        l = (K-i-1) % len(loops)
        print(loops[l])
        exit()
    else:
        loop_check[new_x-1] = True
        x = new_x
print(x)