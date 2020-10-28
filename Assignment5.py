# Tessa Vu
# GEOG 1180-001
# Dr. Edgar
# 8 October 2020

# Assignment 5: Calculating Distances Between Utah Counties

# 1) Calculate the Euclidean distance between Salt Lake County and the other counties, and print out the county name and distances. The format for each line should be as follows: "The distance between SALT LAKE and NAME OF COUNTY is XXXX meters."
# 2) Find the minimum and maximum distance between Salt Lake County and the other counties and print out the county names as follows: "Maximum distance is XXX meters, and county is NAME OF COUNTY."
# 3) Include a complete header, and comments where appropriate.

import math

slc_x = 421932.509151 # The X coordinate of the centroid of Salt Lake County.
slc_y = 4502229.11769 # The Y coordinate of the centroid of Salt Lake County.

# The centroid coordinates (in meters) for other counties in Utah.
# Format: county name, x coordinate, y coordinate.

str_counties = 'KANE,421248.077003,4126997.12719;MILLARD,318229.975165,4327038.17395;SANPETE,450311.582705,4358372.7655;CARBON,535286.548662,4388828.93126;UTAH,442922.507375,4441252.65588;CACHE,438164.934916,4619192.03201;SUMMIT,503745.916187,4524184.01594;WASHINGTON,277954.402951,4128934.44837;GRAND,623880.419923,4315675.1777;UINTAH,626223.592603,4442460.96986;TOOELE,319270.590251,4479721.51259;SEVIER,430056.793418,4289103.62028;GARFIELD,460935.241012,4189974.09249;SAN JUAN,605294.515606,4164841.18364;BOX ELDER,326211.275652,4598715.29279;IRON,298574.110588,4192702.51903;WEBER,423471.784425,4569140.26507;EMERY,525940.528322,4316385.26069;RICH,479645.42659,4608899.86246;WASATCH,485711.183527,4464442.98073;BEAVER,304642.75275,4247877.5251;DAGGETT,625788.907604,4527355.62639;DAVIS,406521.343767,4538251.09871;WAYNE,508428.89395,4241934.48456;PIUTE,401491.210781,4243766.28213;MORGAN,451835.27776,4548811.17842;DUCHESNE,548843.456439,4460927.19722;JUAB,347009.389764,4396492.15746'

counties = str_counties.split(";") # Split the string by semi-colon.

distanceList = [] # Empty list to store Euclidean Distances and names in.
for i in counties:
    a = i.split(",") # Split the string by comma.
    name = a[0] # Name of county.
    xnum = float(a[1]) # X-coordinate.
    ynum = float(a[2]) # Y-coordinate.
    
    distance = math.sqrt(((slc_x - xnum) ** 2) + ((slc_y - ynum) ** 2)) # Calculate Euclidean equation.

    print("The distance between SALT LAKE and", name, "is", distance, "meters.")

    distanceList.append([distance, name]) # Add distance and name to the previously created list.
    distanceList.sort() # Sort list from smallest value to largest value.
    
    print(distanceList) # Make sure the list was properly sorted.
    
lowestDistance = distanceList[0][0] # Lowest distance should be the first value after the list was sorted.
lowestDistanceName = distanceList[0][1]

highestDistance = distanceList[-1][0] # Highest distance should be the last value after the list was sorted.
highestDistanceName = distanceList[-1][1]

print("Minimum distance is", lowestDistance, "meters, and county is", lowestDistanceName)
print("Maximum distance is", highestDistance, "meters, and county is", highestDistanceName)