import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

# 遅い
def rec_binary_search(x, ss):
    len_s = len(ss)
    half = len_s // 2
    if len_s <= 10:
        return int(x in ss)
    if x < ss[half]:
        ss = ss[:half]
    else:
        ss = ss[half:]
    return rec_binary_search(x, ss)

def binary_search(x, ss):
    L = 0
    R = len(ss)
    half = (L+R) // 2
    while L<=R:
        if R-L < 2:
            return int(x in ss[L:R+1])
        if x < ss[half]:
            R = half-1
        elif x > ss[half]:
            L = half + 1
        else:
            return 1
        half = (L+R) // 2

n = int(input())
ss = list(map(int, input().split()))
m = int(input())
ts = list(map(int, input().split()))

ans = 0
for x in ts:
    ans += binary_search(x, ss)

print(ans)