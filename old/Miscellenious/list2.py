cities = {}
city = ' '
while city != '':
    city = input('Enter city: ')
    status = input('Enter status (visited/unvisited): ')
    cities[city] = status

print('These cities are visited:')
for i, j in cities.items():
    if j == 'visited':
        print(i)

print('These cities are not visited:')
for i, j in cities.items():
    if j == 'unvisited':
        print(i)
