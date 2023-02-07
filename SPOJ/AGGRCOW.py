import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    n, c = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        a.append(int(input()))
    a.sort()
    lo = 0; hi = 10**9
    ans = 0

    while lo <= hi:
        mid = (hi + lo) // 2
        count = 1; left = 0
        for i in range(1, n):
            if a[i] - a[left] >= mid:
                count += 1
                left = i
        if count >= c:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(ans)
