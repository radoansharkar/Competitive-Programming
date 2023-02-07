import sys, math
input = sys.stdin.readline

t = int(input())

pii = 2 * math.acos(0.0)

for i in range(t):
    n = float(input())
    sqr = (n*2)*(n*2)
    cir = pii*n*n
    ans = (sqr-cir)

    print(f"Case {i+1}:", "{:0.2f}".format(ans))
