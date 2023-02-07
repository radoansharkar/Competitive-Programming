import sys, math
input = sys.stdin.readline

q, k = [int(x) for x in input().split()]

d = {}
for i in range(q):
    s, e = [x for x in input().split()]
    if s in d:
        d[s] += int(e)
    else:
        d[s] = int(e)
		
d = dict(sorted(d.items(), key=lambda item: item[1], reverse = True))
print(sum(list(d.values())[:k]))
