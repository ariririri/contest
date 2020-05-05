import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import numpy as np
 
N = int(readline())
S = np.array(readline().split(), np.uint64)
T = np.array(readline().split(), np.uint64)
U = np.array(readline().split(), np.uint64)
V = np.array(readline().split(), np.uint64)
 
 
def solve(S, T, U, V):
    A = np.zeros((N, N), np.uint64)
    if N == 1:
        return np.array([[U[0]]], np.uint64)
    all_one_row = (S == 0) & (U == 1)
    all_zero_row = (S == 1) & (U == 0)
    r = np.any(all_zero_row), np.any(all_one_row)
    all_one_col = (T == 0) & (V == 1)
    all_zero_col = (T == 1) & (V == 0)
    c = np.any(all_zero_col), np.any(all_one_col)
    if (c[0] or c[1]) and not (r[0] or r[1]):
        return solve(T, S, V, U).T
    # 確定条件があるなら行にある
    if not (r[0] or r[1]):
        # 確定条件なし。十分均一ならok
        A[1::2, ::2] = 1
        A[::2, 1::2] = 1
        return A
    # 少なくとも行に確定条件がある場合
    if r[0] and r[1]:
        # 列の運命は確定なので、行本位で入れればよい
        A += U[:, None]
        return A
    if r[0]:
        if c[1]:
            return A

import IPython;IPython.embed()