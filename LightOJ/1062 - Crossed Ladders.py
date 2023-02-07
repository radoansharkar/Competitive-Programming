import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    x, y, c = [float(x) for x in input().split()]
    xx = x * x
    yy = y * y
    
    def mid_find(d):
        h1 = math.sqrt(yy - d*d)
        h2 = math.sqrt(xx - d*d)
        d = (h1 * h2) / (h1 + h2)
        return d 
    
    lo = 0
    hi = min(x, y)
    mid = (hi + lo) / 2
    cnt = 0
	
    while cnt < 100:
        if mid_find(mid) >= c:
            lo = mid
        else:
            hi = mid
        mid = (hi + lo) / 2
        cnt += 1
    
    print(f"Case {_ + 1}: {mid}")
