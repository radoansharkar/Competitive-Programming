import sys, math
from functools import cmp_to_key
input = sys.stdin.readline

class element:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx

def compare(a, b):
    if a.val < b.val:
        return -1
    elif a.val == b.val:
        if a.idx > b.idx:
            return -1
    else:
        return 1

n = int(input())
a = [int(x) for x in input().split()]

arr = []
for i in range(n):
    arr.append(element(a[i], i + 1))

arr = sorted(arr, key = cmp_to_key(compare))

for i in range(len(arr)):
    print(arr[i].idx, end = " ")
