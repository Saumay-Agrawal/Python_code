def check(n):
    s = set()
    for i in n:
        x = set()
        for j in n:
            if j == i:
                x |= {n.index(j)}
        s.add(frozenset(x))

print(check('12321'))
        
