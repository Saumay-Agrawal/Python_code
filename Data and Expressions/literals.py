print(1.5e200 * 2.0e210)
## prints inf (infinity), arithmetic overflow

print(1.0e-300 / 1.0e100)
## prints 0.0, arithmetic underflow

print(3*(1/3)== 1.0)
## false its 0.99..

print(1/3+1/3+1/3 == 1)
##

print(format(12/5, '.2f'))
print(format(2**100, '.6e'))
print(format(13567.789, ',.2f'))

## in terms of binary code string numbers occupy more space than decimal number.
## eg 124, decimal = 1byte, string = 3 bytes
print(chr(65))
print(ord('A'))

## examples of string formatting
print(format('Hello','<20')) # left allignment
print(format('Hello', '>20')) # right allignment
print(format('Hello', '^20')) # centre allignment
print(format(' ', '30')) # string of blank characters
print('Hello',format('.', '.<30'),'Have a nice day.')

# implicit line joining - matching brackets
# explicit line joining - backslash (\)
