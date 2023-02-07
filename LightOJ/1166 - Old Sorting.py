import sys
input = sys.stdin.readline

def minSwap(arr, n):
    ans = 0
    temp = arr.copy()
    h = {}
    temp.sort()

    for i in range(n):
        h[arr[i]] = i
         
    init = 0
    for i in range(n):
        if (arr[i] != temp[i]):
            ans += 1
            init = arr[i]
            arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]
            h[init] = h[temp[i]]
            h[temp[i]] = i
             
    return ans

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(f"Case {_ + 1}: {minSwap(a, n)}")
