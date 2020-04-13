N = int(input())
import math

a = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        b = math.gcd(i, j)
        for k in range(1, N+1):
            a += math.gcd(b, k)
print(a)