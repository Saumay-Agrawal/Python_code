'''Dictionaries.'''

DC = {'Batman': 'Bruce Wayne', 'Superman': 'Clark Kent', 'Flash': 'Barry Allen'}
Marvel = {'Spiderman': 'Peter Parker', 'Ironman': 'Tony Stark'}

print(DC)
print(Marvel)
print('-'*20)

for hero, identity in DC.items():
    print('%s is %s.' % (identity, hero))
for hero, identity in Marvel.items():
    print('%s is %s.' % (identity, hero))
print('-'*20)

