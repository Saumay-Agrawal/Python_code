def checkiso(m, n):
    f = True
    for i,j in zip(m,n):
        for x,y in zip(m,n):
            if i==x and j!=y:
                f = False
                break
    return f
