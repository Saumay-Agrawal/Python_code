"""This is the python file meant for testing of all the
   tips given in the online book, Python Tips."""

"""1. *args and **kwargs"""

#
# def test_args_kwargs(n, m, *args, **kwargs):
#     print("n:", n)
#     print("m:", m)
#     for i in args:
#         print("object in args:", i)
#     for i, j in kwargs.items():
#         print("object in args:", i, j)
#
#
# test_args_kwargs(5, 6, 90, 90, 'this is yuck.')
# test_args_kwargs(5, 6, 90, 90, 'this is yuck.', name="Saumay", age="naughty nineteen")

"""2. Debugging"""

# import pdb
#
#
# def make_bread():
#     pdb.set_trace()
#     return "afreen afreen"
#
#
# print(make_bread())


"""3. Map, Filter and Reduce"""
#
# items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x ** 2, items))
# print(squared)
#
#
# def multiply(x):
#     return x * x
#
#
# def add(x):
#     return x + x
#
#
# funcs = [multiply, add]
# for i in range(5):
#     value = list(map(lambda x: x(i), funcs))
#     print(value)
#
# less_than_zero = list(filter(lambda x: x < 0, range(-5, 5)))
# print(less_than_zero)
#
# from functools import reduce
#
# product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
# print(product)

"""5. sets data structure"""

"""6. Ternary Operators"""
# is_fat = True
# state = 'fat' if is_fat else 'fit'
# print('Sam is',state)
#
# is_fat = True
# state = ('fat', 'fit')[is_fat]
# print('Sam is',state)
# # can also be done with lists as the concept of index is being used here.
# # in this implementation tuples/list is first built and then indexing is done.


"""8. Global and return"""
# def addsub(a,b):
#     return (a+b, a-b)
# def muldiv(a,b):
#     return a*b, a/b
# print(addsub(3,4))
# print(muldiv(4,2))

"""9. Mutability"""
# def stack(n,t=[]):
#     t.append(n)
#     print(t)
# stack(1)
# stack(2)
# stack(3)
#
# def elements(n,t=None):
#     if t is None:
#         t = []
#     t.append(n)
#     print(t)
#
# elements(1)
# elements(2)
# elements(3)

