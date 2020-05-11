S = input()
T = input()
for i,s in enumerate(S):
    if s != T[i]:
        print("No")
        exit()
print("Yes")
exit()