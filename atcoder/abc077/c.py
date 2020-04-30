import numpy as np

N = int(input())
ts = list(map(int, input().split()))
ms = list(map(int, input().split()))
bs = list(map(int, input().split()))

ts = sorted(ts)
ms = sorted(ms)
bs = sorted(bs)

m_count = np.zeros(N, dtype=int)
i = 0
for j, m in enumerate(ms):
    while i < N and m >= bs[i]:
        i += 1
    m_count[j] = N-i
m_cumcount = np.cumsum(m_count[::-1])[::-1]
#import IPython;IPython.embed()

i = 0
ans = 0
for j, t in enumerate(ts):
    while i < N and t >= ms[i]:
        i += 1
    #print(m_cumcount[j])
    if i == N:
        break
    ans += m_cumcount[i] 
    #np.append(m_count, N-i)
print(ans)

