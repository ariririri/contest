N, K = list(map(int, input().split()))
a = list(map(int, input().split()))


ans = 10 ** 11
for  i in range(2 ** N):
    if bin(i).count("1") != K:
        continue
    max_height = 0
    height_num = 0
    for j in range(N):
        if i >> j & 1:
            if a[j] <= max_height:
                height_num += (max_height + 1 - a[j])
                max_height += 1
            else:
                max_height = a[j]
        else:
            max_height = max(max_height, a[j])
    ans = min(ans, height_num)

print(ans)