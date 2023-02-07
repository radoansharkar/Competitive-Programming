import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    print(f"Case {_ + 1}: {sum([int(x) for x in input().split()])}")
