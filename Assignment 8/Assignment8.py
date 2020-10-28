'''
Tessa Vu
Dr. Edgar
GEOG 1180-001
29 October 2020
Assignment 8
'''

import math

# A polygon can be represented by a list of vertices that define the polygon boundary.
# The first vertex is the same as last vertex to ensure the polygon is closed.
# Each vertex is a an x,y coordinate pair and you can use len(lake) to get the number of vertices.

lake = [(1462537.8085415417, 7714773.8153863065), (1483850.5554694189, 7714103.519260739), (1492453.7117490023, 7676492.494398902), (1433296.5017492222, 7632269.706630001), (1474342.7131918636, 7613636.061691303), (1459562.4727524312, 7599469.180296974), (1472340.5341098325, 7589152.011208071), (1475704.1912844826, 7565341.044431081), (1503662.8316586744, 7552920.58961675), (1533999.3296832552, 7516335.527547815), (1513366.0964262856, 7487885.923154725), (1493414.139804148, 7478893.053065043), (1478241.0029147381, 7485071.064328294), (1479125.6308366503, 7468150.57037752), (1392269.7730696234, 7417555.057852401), (1304070.827377231, 7470920.113871826), (1307468.0023636783, 7488990.342617386), (1271772.9740143633, 7548109.464035865), (1274938.5596869653, 7596242.758232794), (1268543.156614822, 7613454.647969445), (1220050.218526217, 7598742.189265475), (1214038.681371677, 7644712.349465073), (1224868.3510485475, 7680265.98608239), (1199682.27844527, 7788654.1764017325), (1214679.5649980921, 7804090.206301503), (1247166.8288333777, 7786226.184349898), (1307228.9993143699, 7792929.638718439), (1294099.3718246405, 7739442.812950312), (1326015.8490545966, 7701545.713592767), (1356938.5296237392, 7707644.736486907), (1358404.9070426214, 7676141.067471035), (1370827.746202305, 7654642.949474023), (1365772.9930391344, 7639307.849781529), (1378424.2615008252, 7615683.87030972), (1395389.7880219722, 7622292.319095076), (1401978.3923030684, 7639441.772865532), (1387956.6812004386, 7724824.440869526), (1445708.0415660683, 7733214.2804777855), (1462537.8085415417, 7714773.8153863065)]

# Calculating the perimeter of a polygon is the same as calculating the length of a (closed) multiline.
# Please follow the code example from the lecture slides to calculate the boundary length of the lake:

def calculateEucDist(pt1, pt2): # Create a Euclidean Distance function.
    
    # Assign points.
    pt1_x = pt1[0]
    pt1_y = pt1[1]
    pt2_x = pt2[0]
    pt2_y = pt2[1]
    
    eucDist = math.sqrt((pt1_x - pt2_x) ** 2 + (pt1_y - pt2_y) ** 2) # Euclidean Distance formula.
    print("Euclidean Distance:", eucDist) # Print Euclidean Distancce formula to check if values are correct.
    return eucDist

numPt = len(lake) # Count verteces.
print("Perimeter:", numPt) # Print verteces to check if the value is correct.

totalLength = 0
for i in range(numPt - 1):
    pt1 = lake[i]
    pt2 = lake[i + 1]
    
    length = calculateEucDist(pt1, pt2)
    totalLength = totalLength + length
    
print("Total Length:", totalLength) # Print total length to check if values are correct.

# Please follow the code example (trapezoid method) from the lecture slides to calculate the area of the lake:

def calculateTrapeArea(pt1, pt2): # Create a trapezoid area function.
    
    # Assign points.
    pt1_x = pt1[0]
    pt1_y = pt1[1]
    pt2_x = pt2[0]
    pt2_y = pt2[1]
    
    trapeArea = ((pt2_x - pt1_x) * (pt2_y + pt1_y))/2.0 # Trapezoid area formula.
    print("Trapezoid Area:", trapeArea) # Print trapezoid area formula to check if values are correct.
    return trapeArea

numPt = len(lake) # Count verteces.
print("Perimeter:", numPt) # Print verteces to check if the value is correct.

totalArea = 0
for i in range(numPt - 1):
    pt1 = lake[i]
    pt2 = lake[i + 1]
    
    area = calculateTrapeArea(pt1, pt2)
    totalArea = totalArea + area
    
print("Total Area:", totalArea) # Print total area to check if values are correct.

#Please use the length and area to calculate the compactness ratio:
c = math.sqrt((totalArea)/(totalLength ** 2)) # Compactness ratio formula.
print ("Compactness Ratio:", round(c, 2)) # Print compactness ratio to check if the value is correct.

#Please use the length and area to calculate the P2A:
p2a = (totalLength * totalLength)/totalArea # P2A formula.
print ("P2A Ratio:", round(p2a, 2)) # Print P2A to check if the value is correct.

# Now calculate the coordinates of the minimum bounding rectangle.

# Create empty lists to append new values to for x coordinates and y coordinates.
x_coords = []
y_coords = []

#Please use for loop to store all x coordinates in x_coords, and y coordinates in y_coords:

for x in lake:
    pt_x = (x[0])
    x_coords.append(pt_x) # Add to previously created empty list.
    print("X Coordinates:", pt_x) # Print x coordinates to check if values are correct.
    
for y in lake:
    pt_y = (y[1])
    y_coords.append(pt_y) # Add to previously created empty list.
    print("Y Coordinates:", pt_y) # Print y coordinates to check if values are correct.

#Please get the minimum and maximum x and y coordinates:

# Assign minimums and maximums.
min_x = min(x_coords)
min_y = min(y_coords)
max_x = max(x_coords)
max_y = max(y_coords)

# Print minimums and maximums to check if values are correct.
print ("xmin, ymin(", min_x, ",", min_y, ")")
print ("xmax, ymax(", max_x, ",", max_y, ")")