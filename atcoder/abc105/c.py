N = int(input())

ans = ""
i = 0
if N == 0:
    print(0)
    exit()
while N != 0:
    if N % 2 == 0:
        ans = "0" + ans
        N = N // 2
    else:
        ans = "1" + ans
        if i == 1:
            N = (N + 1) // 2
        else:
            N = (N - 1) // 2
    i = 1 - i

print(ans)