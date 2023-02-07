import sys, math
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]
b = sorted(a)

pre_a = [0, a[0]]
pre_b = [0, b[0]]

for i in range(1, n):
    pre_a.append(a[i] + pre_a[-1])
    pre_b.append(b[i] + pre_b[-1])

for i in range(int(input())):
    type, l, r = [int(x) for x in input().split()]
    
    if type == 1:
        print(pre_a[r] - pre_a[l - 1])
    else:
        print(pre_b[r] - pre_b[l - 1])
