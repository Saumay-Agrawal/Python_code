num = 10
k = num

print(id(num))
print(id(k))

k = 30
print(id(k))

name = input('Enter the name: ')
age = int(input('Age: '))
gpa = float(input('GPA: '))
print(name)
print(age)
print(gpa)

# to check if given identifier is a keyword
print('exit' in dir(___builtins__))