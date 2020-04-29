import numpy as np
N = int(input())

S = list(map(int, input().split()))
T = list(map(int, input().split()))
U = list(map(int, input().split()))
V = list(map(int, input().split()))

max_inp = max(max(U), max(V))
max_ord = 0
n = 1
for i in range(66):
    if n > max_inp:
        break
    else:
        max_ord += 1
        n = n * 2

bit = np.zeros(N, dtype=int) 
ans = np.zeros((N, N), dtype=int) 
for i, s in enumerate(S):
    if s == 1:
        bit[i] = 2 ** max_ord - U[i]
    else:
        bit[i] = U[i]
    ans[i] = s
for j, v in enumerate