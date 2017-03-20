def digits(n):
    c = 0
    while n != 0:
        c += 1
        n /= 10
    return c


def checkPrime(n):
    f = True
    for i in range(2, n):
        if n % i == 0:
            f = False
            break
    return f


def checkCPrime(n):
    f = True
    x = 10**(digits(n) - 1)
    t = n
    while True:
        if not checkPrime(t):
            f = False
            break
        else:
            t = int(t / 10) + (t % 10) * x
        if t == n:
            break
    return f


n = int(input('Enter a number: '))
if checkCPrime(n):
    print('Circular Prime')
else:
    print('Not a circular prime')