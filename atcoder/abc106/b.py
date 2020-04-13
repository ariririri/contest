N = int(input())

def factorize(x):
    results = []
    for i in range(1, x+1):
        if i*i == x:
            results.append(i)
            break
        if i*i > x:
            break
        else:
            if x % i == 0:
                results.append(i)
                results.append(x // i)
    return results

ans = 0
for i in range(1, N+1, 2):
    if len(factorize(i)) == 8:
        ans += 1
print(ans)