N, K = list(map(int, input().split()))
S = input()
x = S[K-1]
print(S[:K-1] + x.lower() + S[K:])