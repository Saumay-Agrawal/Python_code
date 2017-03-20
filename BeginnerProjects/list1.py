slist = []
dlist = []

print('Enter the items in son\'s list.')
while 1:
    x = input('Enter an item: ')
    if x == '':
        break
    else:
        slist.append(x)

print('Enter the items in daughter\'s list.')
while 1:
    x = input('Enter an item: ')
    if x == '':
        break
    else:
        dlist.append(x)

sliste = list(slist)
dliste = list(dlist)

print('Items common in both lists:')
for i in slist:
    if i in dlist:
        print(i)
        del(sliste[sliste.index(i)])
        del(dliste[dliste.index(i)])

print('Items remaining in son\'s list:')
for i in range(0,len(sliste)):
    print(sliste[i])

print('Items remaining in daughter\'s list:')
for i in range(0,len(dliste)):
    print(dliste[i])
