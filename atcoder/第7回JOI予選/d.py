from collections import defaultdict

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
A = sorted(A)
M = int(input())
B = [list(map(int, input().split())) for _ in range(M)]
B = sorted(B)
B_dic = defaultdict(lambda: defaultdict(int))
for b in B:
    B_dic[b[0]][b[1]] = 1
for b in B:
    move_x = b[0] - A[0][0]
    move_y = b[1] - A[0][1]
    true_flag = True
    for a in A[1:]:
        if B_dic[a[0]+move_x][a[1] + move_y] == 0:
            true_flag = False
            break
    if true_flag:
        break

print(move_x, move_y)





