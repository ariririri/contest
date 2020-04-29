N = int(input())

old_t = 0
old_x = 0
old_y = 0

for _ in range(N):
    t, x, y = list(map(int, input().split()))
    rest_t = t - old_x
    diff = abs(x - old_x) + abs(y - old_y)
    if (rest_t < diff) or (old_t - t + old_x - x + old_y -y) % 2 != 0:
        print("No")
        exit()
    old_t = t
    old_x = x
    old_y = y

print("Yes")


