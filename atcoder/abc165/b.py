x = int(input())

n = 0
m = 100
while m < x:
    m = (m * 101) // 100
    n += 1
print(n)