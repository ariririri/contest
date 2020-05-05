X = int(input())

if X == 1:
    print(0, -1)
    exit()

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

def solve(num, X):
    a = 1
    for i in range(1, X+1):
        if (i * 100) ** 5 - (i * 100 - num) ** 5 >= X:
            break
    max_a = 100 * i
    a = max_a - 99
    while a <= max_a:
        if (a) ** 5 - (a -num) ** 5 == X:
            return True, a, a - num
        a += 1
    return False, 0, 0

arr = make_divisors(abs(X))
for num in arr:
    if (num - X) % 5:
        continue
    flag, a, b = solve(num , X)
    if flag:
        print(a, b)
        exit()
    #flag, a, b = solve(-num , X)
    #if flag:
    #    print(a, b)
    #    exit()