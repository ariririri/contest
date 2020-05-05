K = int(input())
a, b = list(map(int, input().split()))

if ( (a-1) // K - b // K) < 0:
    print("OK")
else:
    print("NG")