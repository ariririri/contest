n, a, b, c = list(map(int, input().split()))
ss = []
for i in range(n):
    ss.append(input())
ans = []
num_dic = {"A": a,"B": b, "C": c}

for i in range(n):
    s = ss[i]
    if num_dic[s[0]] == 0 and num_dic[s[1]] == 0:
        print("No")
        exit()
    elif num_dic[s[0]] > num_dic[s[1]]:
        num_dic[s[0]] -= 1
        num_dic[s[1]] += 1
        ans.append(s[1])
    elif num_dic[s[0]] < num_dic[s[1]]:
        num_dic[s[0]] += 1
        num_dic[s[1]] -= 1
        ans.append(s[0])
    elif i == n -1:
        ans.append(s[0])
        num_dic[s[0]] -= 1
        num_dic[s[1]] += 1
    elif s[0] in ss[i+1]:
        num_dic[s[0]] += 1
        num_dic[s[1]] -= 1
        ans.append(s[0])
    else:
        num_dic[s[0]] -= 1
        num_dic[s[1]] += 1
        ans.append(s[1])
print("Yes")
for a in ans:
    print(a)
