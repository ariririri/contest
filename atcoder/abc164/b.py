a,b,c,d = list(map(int, input().split()))

i = 0
while True:
    if i % 2 == 0:
        c = c - b
    else:
        a = a - d
    if a <= 0:
        print("No")
        exit()
    if c <= 0:
        print("Yes")
        exit()
    i += 1