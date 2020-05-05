A, B, N = list(map(int, input().split()))

num = min(B-1, N)
print((num*A) // B)