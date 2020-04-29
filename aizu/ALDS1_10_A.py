n = int(input())

fibs = [0 for _ in range(n+1)]
checks = [False for _ in range(n+1)]

def fib(k):
    if k == 0:
        return 1
    elif k == 1:
        return 1
    elif checks[k]:
        return fibs[k]
    else:
        fibs[k] = fib(k-1) + fib(k-2)
        checks[k] = True
        return fibs[k]

print(fib(n))


