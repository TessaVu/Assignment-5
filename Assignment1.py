# Tessa Vu
# Dr. Edgar
# GEOG 1180-001
# 10 September 2020

# Assignment 1: Calculate Manhattan Distance

import math # Import the math library.

# Beaver County is x1 and y1, Salt Lake County is x2 and y2.

x1 = 271162.223
x2 = 4252186.393
y1 = 422504.192
y2 = 4498778.552

# 1) Please write a script to calculate the Manhattan distance between Salt Lake County and Beaver County and print the distance.

Manhattan_Distance = abs (x1 - x2) + abs(y1 - y2)

print (Manhattan_Distance)

# 2) Please write a script to calculate the Euclidean distance between Salt Lake County and Beaver County and print the distance.

Euclidean_Distance = math.sqrt (((x1 - x2) ** 2)+((y1 - y2) ** 2))

print (Euclidean_Distance)

# 3) Please write a script to compare the Manhattan distance to the Euclidean distance. Print the comparison result.

print (Manhattan_Distance >= Euclidean_Distance) # Is the Manhattan distance greater than the Euclidean distance?

print (Manhattan_Distance <= Euclidean_Distance) # Is the Manhattan distance lesser than the Euclidean distance?

print (Manhattan_Distance == Euclidean_Distance) # Is the Manhattan distance equal to the Euclidean distance?