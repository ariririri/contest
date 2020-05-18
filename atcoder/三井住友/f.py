T1, T2 = list(map(int, input().split()))
A1, A2 = list(map(int, input().split()))
B1, B2 = list(map(int, input().split()))

a, b = A1 * T1, A2 * T2
c, d = B1 * T1, B2 * T2

if a + b == c+ d:
    print("infinity")
    exit()
if a + b < c+d:
    a,b,c,d = c,d,a,b
if a > c:
    print(0)
    exit()
else:
    num = 0
    if (c-a) % (a+b-c-d)  == 0:
        num = 1
    print((c-a-1) // (a+b-c-d) * 2+num+1)
