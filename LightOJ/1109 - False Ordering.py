import sys, math
input = sys.stdin.readline

def divisor_count(n):
    return len([x for x in range(1, n + 1) if n % x == 0])

a = []
for i in range(1, 1001):
    a.append([divisor_count(i), i])

a = sorted(a, key=lambda row: (row[0], -row[1]))
for i in range(int(input())):
    temp = int(input())
    print(f"Case {i + 1}: {a[temp - 1][1]}")
