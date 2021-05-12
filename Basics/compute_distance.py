import math
point1 = input("Input first point x,y: ")
point2 = input("Input second point x,y: ")

point1 = tuple(point1.split(','))
point2 = tuple(point2.split(','))

xtotal = float(point2[0]) - float(point1[0])
xsquared = xtotal ** 2
ytotal = float(point2[1]) - float(point1[1])
ysquared = ytotal ** 2
total = xsquared + ysquared
print(total)
distance = math.sqrt(total)

print(distance)