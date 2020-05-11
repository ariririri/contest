N, M, K = list(map(int, input().split()))

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 998244353
_N = N + 100 # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, _N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

Mpower = [1, M]
lpower = [1, M-1]
for i in range(2, _N + 1):
    Mpower.append((Mpower[-1] * M) % p)
    lpower.append((lpower[-1] * (M-1)) % p)

ans = Mpower[N]
for i in range(K+2, N+1):
    ans = ans - (cmb(N-1, i-1,p)*M *lpower[N-i]) % p
    ans = ans % p

print(ans)