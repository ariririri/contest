N = int(input())
A = list(map(int, input().split()))

num_dic = {}

ans = 0
for i, a in enumerate(A):
    if (i - a) in num_dic:
        ans += num_dic[i-a]
    if a + i in num_dic:
        num_dic[a+i] += 1
    else:
        num_dic[a+i] = 1
print(ans)
