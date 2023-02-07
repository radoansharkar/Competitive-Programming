import FileIO

import sys, math
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]
m = int(input())

sum = [0] * n
sumsq = [0] * n

sum[0] = a[0]
sumsq[0] = a[0] * a[0]

for i in range(1, n):
    sum[i] = sum[i - 1] + a[i]
    sumsq[i] = sumsq[i - 1] + (a[i] * a[i])

print(sum)
print(sumsq)
for i in range(m):
    u, v = [int(x) for x in input().split()]
    s = sum[v] - sum[u] + a[u]
    sq = sumsq[v] - sumsq[u] + (a[u] * a[u])
    ans = ((s * s) + sq) // 2
    print(ans)