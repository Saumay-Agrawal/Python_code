"""This program prints following patterns as per the value of n given by
the user."""

n = int(input('Enter the value for n: '))

while type(n) != int:
    n = int(input('Enter the value for n: '))

print('Pattern 1:')
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*', end='')
    print()

print('Pattern 2:')
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print('*', end='')
    print()

print('Pattern 3:')
for i in range(1,n+1):
    for j in range(1,i):
        print(' ', end='')
    for j in range(1, n-i+2):
        print('*', end='')
    print()

print('Pattern 4:')
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*', end='')
    for j in range(1, n-i+1):
        print(' ', end='')
    print()
