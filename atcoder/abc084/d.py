Q = int(input())
import numpy as np

n = 10 ** 5
doubel_primes = np.zeros(n+1, dtype=int)
primes_flags = np.zeros(n+1, dtype=bool)
primes_flags[1] = True # Trueはprimeでない.
primes_flags[0] = True # Trueはprimeでない.
#primes_flags[2] = True # Trueはprimeでない.
primes_flags[::2] = True # Trueはprimeでない.
if Q >= 1:
    primes_flags[2] = False
def prime_check(n=100000):
    i = 3
    while i  < n:
        if not primes_flags[i]:
            if not primes_flags[i//2 + 1]:
                doubel_primes[i] = 1
            k = i * i
            while k <= n:
                primes_flags[k] = True
                k += i
        i += 2
        
prime_check(n)
prime_sum = doubel_primes.cumsum()
for _ in range(Q):
    l, r = list(map(int, input().split()))
    print(prime_sum[r] - prime_sum[l-1])

