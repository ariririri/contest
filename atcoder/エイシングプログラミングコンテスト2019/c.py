import sys
H,W =list(map(int, input().split()))
S = [list(input()) for i in range(H)]
sys.setrecursionlimit(1000000)

black_visited_flag = [[False] * W for _ in range(H)] 

other_color = {".": "#", "#":'.'}

def dfs(i,j, color):
    num = 0
    black_num = 0
    #import IPython;IPython.embed()
    if i != 0:
        if S[i-1][j] == other_color[color] and not visit_flag[i-1][j]:
            visit_flag[i-1][j] = True
            _num, _black_num = dfs(i-1, j, other_color[color])
            num += _num
            black_num += _black_num
            if other_color[color] == "#":
                black_num += 1
                black_visited_flag[i-1][j] = True
            else:
                num += 1
    if i != H-1:
        if S[i+1][j] == other_color[color] and not visit_flag[i+1][j]:
            visit_flag[i+1][j] = True
            _num, _black_num = dfs(i+1, j, other_color[color])
            num += _num
            black_num += _black_num
            if other_color[color] == "#":
                black_num += 1
                black_visited_flag[i+1][j] = True
            else:
                num += 1
    if j != 0:
        if S[i][j-1] == other_color[color] and not visit_flag[i][j-1]:
            visit_flag[i][j-1] = True
            _num, _black_num = dfs(i, j -1, other_color[color])
            num += _num
            black_num += _black_num
            if other_color[color] == "#":
                black_num += 1
                black_visited_flag[i][j-1] = True
            else:
                num += 1
    if j != W-1:
        if S[i][j+1] == other_color[color] and not visit_flag[i][j+1]:
            visit_flag[i][j+1] = True
            _num, _black_num = dfs(i, j+1, other_color[color])
            num += _num
            black_num += _black_num
            if other_color[color] == "#":
                black_num += 1
                black_visited_flag[i][j+1] = True
            else:
                num += 1
    return num, black_num



ans = 0
visit_flag = [[False] * W for _ in range(H)] 
for i, row in enumerate(S):
    for j, val in enumerate(row):
        if black_visited_flag[i][j] or S[i][j] == ".":
            continue
        num, black_num = dfs(i,j, "#")
        ans += (num * black_num)

print(ans)
    