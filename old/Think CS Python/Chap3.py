'''Functions'''

var = 70
print(id(var))
print(type(var))

int('32')
#int('Hello')

#A module is a file that contains a collection of related functions grouped together.

import math
x = math.log10(1000) #dot notation
y = math.sin(2*math.pi)
print(x, y)

def threeline():
    newline()
    newline()
    newline()

def newline():
    print() #prints a newline character

threeline()

def threeline():
    def newline():
        print('Nested function')

threeline()
