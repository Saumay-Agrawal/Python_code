'''This program takes two points in 2D cartesian plane. It then uses these points
to find the other two vertices of the square that can be formed using these points.'''

def vardata(var):
    print(var, 'is', type(var))

def distance(point1, point2):
    '''take two two-element tuples of format (x, y) where x and y are integers
    and returns distance between these points.'''
    d = ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)**0.5
    return float(format(d, '.2f'))

def verticeFinder(point, length):
    '''Takes a point tuple of format (x, y) and an integer lenght value.'''
    vardata(point)
    vardata(length)
    diagonal = float(format(length*1.414, '.2f'))
    vardata(diagonal)
    sidelength = (length-0.01, length, length+0.01)
    vardata(sidelength)
    diagonallength = (diagonal-0.01, diagonal, diagonal+0.01)
    vardata(diagonallength)
    for i in range(point[0]-int(length), point[0]+int(length)):
        for j in range(point[1]-int(length), point[1]+int(length)):
            if distance((i, j), point) in sidelength and distance((i, j), point) in diagonallength:
                return (i, j)

p1 = (int(input('x1 = ')), int(input('y1 = ')))
p2 = (int(input('x2 = ')), int(input('y2 = ')))
vardata(p1)
vardata(p2)
d = distance(p1, p2)
vardata(d)
print('Length of side = ', d)
print('p3 = ', verticeFinder(p1, d))
print('p4 = ', verticeFinder(p2, d))
