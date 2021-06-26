# Question 2.18

import numpy
import math

pi = numpy.pi
print(str(pi))
theta = (2 * pi) / 17
print(theta)
counter = 1
end = 16
x = 1
end += x
sum = 0

for k in range (counter, end, x):
    square = x ** 2
    sum += math.cos(square * theta)
    x += 1

print(sum)

