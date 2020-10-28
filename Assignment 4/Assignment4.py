# Tessa Vu
# Dr. Edgar
# GEOG 1180-001
# 01 October 2020

# Assignment 4: Identifying Neighbors

# Write a script to identify all the blue points that are within 536,000 meters of the red point, store them in a list, print out their IDs, and print the total number of point neighbors.

import math

# [ID, X coordinate, Y coordinate]
blue_points = [[30, 536254.99137, 3659453.06343],
[33, 536721.584912, 3659162.97207],
[50, 535807.099324, 3659576.92825],
[112, 536827.131371, 3657913.01245],
[117, 536473.254082, 3659433.57702],
[120, 536196.9844, 3658713.72722],
[127, 536387.547701, 3658527.70015],
[133, 537397.838429, 3659554.48657],
[144, 537715.931243, 3658625.59997],
[164, 538367.648437, 3658867.34288],
[172, 537112.662366, 3657921.28957],
[173, 536418.315024, 3658715.47946],
[209, 538096.28422, 3658514.93514],
[211, 538077.87716, 3658138.39337],
[223, 536220.396985, 3659243.54161],
[242, 536102.087002, 3658703.61054],
[244, 536968.755886, 3659409.42857],
[246, 535996.903591, 3658705.08691],
[275, 538078.165429, 3659022.35547],
[303, 535999.885405, 3658521.91524]]

# [ID, X coordinate,Y coordinate]
red_point = [1, 1073706.744,3658967.925]

neighbors = []
for point in blue_points:
    if (math.sqrt(((point[1] - red_point[1]) ** 2) + ((point[2] - red_point[2]) ** 2)) < 536000):
        neighbors.append(point)
        print(point[0])

print("The red point has", len(neighbors), "neighbors.")