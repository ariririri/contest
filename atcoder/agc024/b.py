N = int(input())
dic = {}
nums = []
for i in range(N):
    num = int(input())
    dic[num] = i+1
    nums.append(num)
ans = 0
l = 0
for i in range(N-1):
    if dic[i+2] < dic[i+1]:
        l = 0
    else:
        l += 1
    ans = max(ans, l)
print(N-ans-1)