dp1 = int(input('dp1: '))
p1 = []
for i in range(0,dp1+1):
    p1.append(int(input('list item: ')))
    print(p1)

print(p1.reverse())

dp2 = int(input('dp2: '))
p2 = []
for i in range(0,dp2+1):
    p2.append(int(input('list item: ')))
    print(p2)
p1 = p1.reverse()
print(p1)

sum = p1 + p2
print(sum.reverse())
