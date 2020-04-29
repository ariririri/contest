R, C = list(map(int, input().split()))

A = []
for i in range(R):
    A.append(list(map(int, input().split())))


ans = 0
for i in range(2 ** R):
    B = []
    burned = 0
    for j in range(R):
        if i >> j & 1:
            B.append([1-a for a in A[j]])
        else:
            B.append(A[j])
    for k in range(C):
        top = 0
        for j in range(R):
            top += B[j][k]
        burned += max(top, R-top)
    ans = max(ans, burned)

print(ans)
        
    
