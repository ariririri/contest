from sys import stdin
input = stdin.readline

q = int(stdin.readline())

def solve():
    xs = input()
    ys = input()
    len_x = len(xs)-1
    len_y = len(ys)-1
    # [i,j]までで一番長い数値とする
    dp = [0] * (len_x+1)
    memo = [0] * (len_x+1)

    for j in range(len_y):
        yj = ys[j]
        # 参照コピーにならない
        memo = dp[:]
        for i in range(len_x):
            if xs[i] == yj:
                dp[i+1] = memo[i] + 1
            elif dp[i+1] < dp[i]:
                dp[i+1] = dp[i]
    return dp[len_x]


ret = [ solve() for i in range(q)]
print(*ret, sep="\n")