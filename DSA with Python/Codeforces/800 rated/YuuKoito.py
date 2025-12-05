import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    known = []

    # Collect all known values next to -1 blocks
    for i in range(n):
        if a[i] != -1:
            if i > 0 and a[i-1] == -1:
                known.append(a[i])
            if i < n-1 and a[i+1] == -1:
                known.append(a[i])

    # If no known neighbors → all can be 0
    if not known:
        k = 0
    else:
        mn = min(known)
        mx = max(known)
        k = (mn + mx) // 2

    # Replace all -1 by k
    for i in range(n):
        if a[i] == -1:
            a[i] = k

    # Compute maximum adjacent difference
    diff = 0
    for i in range(n - 1):
        diff = max(diff, abs(a[i+1] - a[i]))

    print(diff, k)
    print(*a)
