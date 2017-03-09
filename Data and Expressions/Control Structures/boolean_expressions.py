print('a'<'b')
print('A'<'b')
print('12'>'9')

# membership operators
print(10 in (10,20,30))
print(10 not in (10,20,30))

print(10<=15<=20)
# python automatically makes it 10<=15 and 15<=20

# operator precedence
# **
# -
# *, /, //, %
# + -
# > < >= <= == !=
# not
# and
# or

# short circuit(lazy) evaluation
# for logical and,if first value is false, rest is not checked
# for logical or, if first value is true, rest is not checked

# logically equivalent boolean expressions
# x < y -> not(x >=y)
