from collections import defaultdict
N, W = list(map(int, input().split()))

values = []
weights = []

max_w = 0
weight_value_dict = defaultdict(int)
for i in range(N):
    v, w = list(map(int, input().split()))
    weight_value_dict[w] = max(v, weight_value_dict[w])
    values.append(v)
    weights.append(w)
# import IPython;IPython.embed()

dp = [0 for i in range(W+1)]

for j in range(1, W+1):
    for weight, val in weight_value_dict.items():
        if j < weight:
            continue
        else:
            dp[j] = max(dp[j], dp[j-weight] + val)
print(dp[W])