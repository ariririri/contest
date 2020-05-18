N = int(input())
import math
sin_dic = {}
mod = 1000000007

zero_num = 0
for i in range(N):
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        zero_num += 1
        continue
    if a == 0:
        b = -1
    elif b == 0:
        a = 1
    else:
        c = math.gcd(a, b)
        a, b = a//c, b//c
        if a < 0 and b < 0:
            a, b = -a, -b
        elif a < 0 and b > 0:
            a, b = -a, -b
    if (a,b) in sin_dic:
        sin_dic[(a, b)].append(i)
    else:
        sin_dic[(a, b)] = [i]

ans = 1
skip_dic = {}
for (key, _key) , values in sin_dic.items():
    if (key, _key) in skip_dic:
        continue
    oth_len = 0
    norm_len = 0
    norm_len += len(values)
    if (-key, -_key) in sin_dic:
        norm_len += len(sin_dic[(-key, -_key)])
    if (_key, -key) in sin_dic:
        oth_len += len(sin_dic[(_key, -key)])
    if (-_key, key) in sin_dic:
        oth_len += len(sin_dic[(-_key, key)])

    p = pow(2, oth_len, mod) - 1 + pow(2, norm_len, mod)
    ans = (ans * p) % mod
    skip_dic[(key, _key)] = True
    skip_dic[(-key, -_key)] = True
    skip_dic[(_key, -key)] = True
    skip_dic[(-_key, key)] = True
print((ans-1 + zero_num) % mod)
