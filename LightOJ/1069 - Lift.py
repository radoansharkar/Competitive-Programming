t = int(input())

for i in range(t):
    me, lift = [int(x) for x in input().split()]

    if me < lift:
        x = lift - me
        res = 3 + 5 + 3 + (me * 4) + 3 + 5 + (x * 4)
    else:
        x = me - lift
        res = 3 + 5 + 3 + (me * 4) + 3 + 5 + (x * 4)
    
    print(f"Case {i+1}: {res}")
    
