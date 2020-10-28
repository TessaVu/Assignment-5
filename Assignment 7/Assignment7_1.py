'''
Tessa Vu
Dr. Edgar
GEOG 1180-001
22 October 2020

Assignment 7_1
'''

# Raquel has four friends and they are taking the same class at the University of Utah. They are each at home and plan to discuss a group assignment at a meeting location that is convenient for everyon. They decide that the centroid of their homes will be a good place for them to meet.

# The format of the locations of these students is [x,y].
locations = [[427016.87,4512645.10],[427233.87,4512762.30],[427785.73,4512812.08],[427464.42,4511229.45],[428449.54,4511184.56]]

sum_x = 0 # Initialize the x coordinate of mean center as 0.
sum_y = 0 # Initialize the y coordinate of mean center as 0.

# Please create a loop to get the summation of x coordinates and y coordinates and assign them to sum_x and sum_y, respectively.

for x in locations:
    pt_x = (x[0]) # Select the x-values from the "locations" list.
    sum_x += float(pt_x) # Add the x-values up.
    print (sum_x)
    
for y in locations:
    pt_y = (y[1]) # Select the y-values from the "locations" list.
    sum_y += float(pt_y) # Add the y-values up.
    print (sum_y)

# Please calculate the mean center by dividing the summation by the number of points.

meanCenter_x = sum_x / 5
meanCenter_y = sum_y / 5
meanCenter = [meanCenter_x, meanCenter_y]

print (meanCenter_x, "is the mean center for the x-values.")
print (meanCenter_y, "is the mean center for the y-values.")
print (meanCenter, "is the mean center.")