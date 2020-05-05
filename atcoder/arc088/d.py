S = input()
l = len(S)
if l % 2 == 0:
    ans = l // 2
    after_half = l//2
    before_half = after_half - 1
    s = S[l//2]
    for i in range(l//2):
        if S[before_half] == S[after_half] and S[before_half] == s:
            ans += 1
            before_half -= 1
            after_half += 1
        else:
            break
if l % 2 == 1:
    ans = l // 2 
    after_half = l//2
    before_half = after_half
    s = S[l//2]
    for i in range(l//2 + 1):
        if S[before_half] == S[after_half] and S[before_half] == s:
            ans += 1
            before_half -= 1
            after_half += 1
        else:
            break

print(ans)
