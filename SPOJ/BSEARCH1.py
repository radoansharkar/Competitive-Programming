import sys, math
input = sys.stdin.readline

n, q = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

d = {}
for i in range(n):
    if a[i] not in d:
        d[a[i]] = i
		
for i in range(q):
    x = int(input())
    if x in d:
        print(d[x])
    else:
        print(-1)
