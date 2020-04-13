N = int(input())
S = list(input())

R = []
G = []
B = []
r = 0
g = 0
b = 0
for i, s in enumerate(S):
    if s == "R":
        r += 1
    elif s == "G":
        g += 1
    else:
        b += 1
    R.append(r)
    G.append(g)
    B.append(b)

ans = 0
for i in range(N-1):
    if S[i] == "R":
        for j in range(i+1, N):
            #print("i", i, "j", j, ans)
            #print(S[i], S[j])
            if S[j] == "G":
                if 2*j - i < N and S[2*j - i] == "B":
                    ans += (B[N-1] - B[j] - 1)
                else:
                    ans += (B[N-1] - B[j])
            if S[j] == "B":
                if 2*j - i < N and S[2*j - i] == "G":
                    ans += (G[N-1] - G[j] - 1)
                else:
                    ans += (G[N-1] - G[j])
    if S[i] == "G":
        for j in range(i, N):
            if S[j] == "R":
                if 2*j - i < N and S[2*j - i] == "B":
                    ans += (B[N-1] - B[j] - 1)
                else:
                    ans += (B[N-1] - B[j])
            if S[j] == "B":
                if 2*j - i < N and S[2*j - i] == "R":
                    ans += (R[N-1] - R[j] - 1)
                else:
                    ans += (R[N-1] - R[j])
    if S[i] == "B":
        for j in range(i, N):
            if S[j] == "G":
                if 2*j - i < N and S[2*j - i] == "R":
                    ans += (R[N-1] - R[j] - 1)
                else:
                    ans += (R[N-1] - R[j])
            if S[j] == "R":
                if 2*j - i < N and S[2*j - i] == "G":
                    ans += (G[N-1] - G[j] - 1)
                else:
                    ans += (G[N-1] - G[j])
print(ans)


