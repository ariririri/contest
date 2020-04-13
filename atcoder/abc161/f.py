N = int(input())

if N == 2:
    print(1)
    exit()


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+100):
        if i > temp / i:
            break
        if i * i == temp:
            arr.append(i)
            break
        if temp % i == 0:
            arr.append(i)
            arr.append(temp // i)
    arr.append(n)
    return arr

N_div = factorization(N)
N_1_div = factorization(N-1)


ans = len(N_1_div)
for K in N_div:
    temp = N
    while temp % K == 0:
        temp = temp // K
    if temp % K == 1:
        ans += 1
print(ans)
