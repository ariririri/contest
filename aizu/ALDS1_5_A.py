n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

flag = [False for _ in range(q)]
value_dict = {}

for i in range(2 ** n):
    a = 0
    for j in range(n):
        if i >> j & 1:
            a += A[j]
            value_dict[a] = 1
    
for b in M:
    if b in value_dict:
        print("yes")
    else:
        print("no")

