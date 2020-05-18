import math

a, b ,h ,m = list(map(int, input().split()))

t = 6*m - (30 *h + 0.5 * m)
cos = math.cos(math.radians(t))

print(math.sqrt(a * a + b*b - 2* a* b* cos))