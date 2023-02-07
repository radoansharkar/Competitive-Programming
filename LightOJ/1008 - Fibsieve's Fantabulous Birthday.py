import math

t = int(input())

for i in range(t):
    x = 0; y = 0
    n = int(input())

    sq = math.ceil(math.sqrt(n))
    val = (sq * sq - sq) + 1
    if sq % 2 == 0:
        if n >= val:
            x = sq
            y = (sq * sq - n) + 1
        else:
            x = abs(((sq - 1) * (sq - 1) + 1) - n) + 1
            y = sq
    else:
        if n <= val:
            x = sq
            y = abs(((sq - 1) * (sq - 1) + 1) - n) + 1
        else:
            x = (sq * sq - n) + 1
            y = sq
    
    print(f"Case {i+1}: {abs(x)} {abs(y)}")
