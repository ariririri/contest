S = input()


if 0 < int(S[:2]) <= 12 and  0 < int(S[2:]) <= 12:
    print("AMBIGUOUS")
elif (int(S[:2]) > 12 or int(S[:2]) == 0) and 0 < int(S[2:]) <= 12:
    print("YYMM")
elif 0 < int(S[:2]) <= 12 and (int(S[2:]) > 12 or int(S[2:]) == 0):
    print("MMYY")
else:
    print("NA")