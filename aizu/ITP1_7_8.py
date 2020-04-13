
read_flag = True
while  read_flag:
    x, y = list(map(int, input().split()))
    if x == 0 and y  == 0:
        read_flag = False
        break
    ans = 0
    for i in range(1, y//3 + 1):
        for j in range(i+1, y):
            if j >= y - i -j:
                break
            if y - i - j > x:
                continue
            ans += 1
    print(ans)
        
