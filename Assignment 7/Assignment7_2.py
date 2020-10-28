'''
Tessa Vu
Dr. Edgar
GEOG 1180-001
22 October 2020

Assignment 7_2
'''

# Snowbird is a popular ski resort and attracts skiers from all over the world. In this assignment, we would like to know the slope of a ski run at Snowbird. "Top" is the start point of the ski run and "bottom" is the end of the ski run.

import math

# Data format [x,y,elevation] in meters.
top = [445373.59,4490238.66,3339] # Start (first set).
bottom = [444445.75,4492463.02,2472] # End (second set).

# Please retrieve x, y, and z coordinates using list index.
top_x = top[0] # Assign variables to each element of the coordinates.
top_y = top[1]
top_z = top[2]

bottom_x = bottom[0]
bottom_y = bottom[1]
bottom_z = bottom[2]

# Please calculate horizontal distance.
horizontalDistance = math.sqrt(((bottom_x - top_x) ** 2) + ((bottom_y - top_y) ** 2))

# Please calculate elevation change.
elevationChange = bottom_z - top_z

print (horizontalDistance, "is the horizontal distance.") # Horizontal distance must be positive, implying rightward motion.
print (elevationChange, "is the elevation change.") # Elevation change must be negative, implying downward motion.

# Please calculate slope.
slope = horizontalDistance/elevationChange

# Convert the slope into degrees.
degreeSlope = math.degrees(math.atan(slope))

print (slope, "is the slope.") # Slope must be negative, implying downward motion.
print (degreeSlope, "is the degree slope.") # Degree slope must be negative, implying downward motion.