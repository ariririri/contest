S = input()

ans = 0
temp = 0
for x in S:
    if x in ["A", "G", "C", "T"]:
        temp += 1
        ans = max(ans, temp)
    else:
        temp = 0

print(ans)
