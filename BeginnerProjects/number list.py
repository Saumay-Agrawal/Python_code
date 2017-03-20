num = []
while 1:
    n = int(input('Enter a number: '))
    if n == -1:
        break
    else:
        num.append(n)
print('Max value:', max(num))
print('Sum:', sum(num))
    
