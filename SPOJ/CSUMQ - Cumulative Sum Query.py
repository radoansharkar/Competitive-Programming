import sys, math
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]

pre_a = [0, a[0]]

for i in range(1, n):
    pre_a.append(a[i] + pre_a[-1])

for i in range(int(input())):
    l, r = [int(x) for x in input().split()]
    
    print(pre_a[r + 1] - pre_a[l])
