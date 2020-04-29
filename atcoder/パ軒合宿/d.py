N = int(input())

flags = []
color_nums = []
color_dic = {"B":0, "R":1, "W":2, "#":3}
for _ in range(5):
    _x = input()
    flags.append(list(_x))
for i in range(N):
    color_num = [0] * 4
    for j in range(5):
        c = flags[j][i]
        color_num[color_dic[c]] += 1
    color_nums.append(color_num)



MAX = 10 ** 30

dp = [[MAX for _ in range(3)] for _ in range(N)]

for i in range(3):
    dp[0][i] = 5 - color_nums[0][i]
for i in range(1, N):
    for j in range(3):
        dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + 5 - color_nums[i][j]

print(min(dp[-1]))
#import IPython;IPython.embed()