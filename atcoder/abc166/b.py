N, K = list(map(int, input().split()))

nums = [0] * N

for i in range(K):
    d = int(input())
    As = list(map(int, input().split()))
    for a in As:
        nums[a-1] += 1

ans = 0
for num in nums:
    if num == 0:
        ans += 1
print(ans)