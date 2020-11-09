'''
Tessa Vu
Dr. Edgar
GEOG 1180-001
11/02/2020
Assignment 10
'''

# Expected calls for each neighborhood.
call_list = [10,20,34,21,15,6]

# Distance between neighborhoods and potential fire station locations.
dis_array = [[1.1,1.9,2.8,2.4,2.8,3.4],# Distance between location "0" and the neighborhood areas.
          [1.4,1.1,1.8,2.6,2.5,2.8],# Location "1".
          [3.6,2.4,1.3,3.9,2.6,1.6],# Location "2".
          [2.3,2.7,3.4,1.2,1.6,2.6],# Location "3".
          [3.4,2.6,2.2,2.7,1.8,1]] # Location "4".

# Please define a function to calculate the total distance given a sited fire station index (loc_index):
loc_index = [0,1,2,3,4] # List for fire station index.

def calTotalDistance(loc_index, d, a):

    totalDistance = 0
    numNeighborhoods = len(call_list)
    
    for i in range(numNeighborhoods):
        totalDistance = totalDistance + call_list[i] * dis_array[loc_index][i]
    
    print (totalDistance)
    return totalDistance

# Test each location to verify.
calTotalDistance(0,0,0)
calTotalDistance(1,1,1)
calTotalDistance(2,2,2)
calTotalDistance(3,3,3)
calTotalDistance(4,4,4)

# Get the number of potential locations.
numLocation = len(dis_array)
print ("There are", numLocation, "potential locations.")

# Create a list to store the total distances at all scenarios.
allDistances = []

# Please use loop to call the "calTotalDistance" function to get the total travel distances at all scenarios and store them in the "allDistances" list:
loc_index = [0,1,2,3,4]

# For loop below keeps outputting values multiple times in wrong order.
'''for li in loc_index:
    for d in dis_array:
        for a in call_list:
            calTotalDistance(li, d, a)
            allDistances.append(calTotalDistance(li, d, a))'''
            
# For loop below keeps outputting values multiple times in right order.
for li in loc_index:
    calTotalDistance(0,0,0)
    calTotalDistance(1,1,1)
    calTotalDistance(2,2,2)
    calTotalDistance(3,3,3)
    calTotalDistance(4,4,4)
    allDistances.append(calTotalDistance(0,0,0))
    allDistances.append(calTotalDistance(1,1,1))
    allDistances.append(calTotalDistance(2,2,2))
    allDistances.append(calTotalDistance(3,3,3))
    allDistances.append(calTotalDistance(4,4,4))

print(allDistances)

# Please calculate the minimum distance:
minDist = min(allDistances)
print(minDist)

# Print out the minimum distance.
print("The minimum total travel distance is %f miles." %(minDist))

# Please find the index of the fire station that has the minimum distance:
center_index = allDistances.index(206.10000000000002)
print(center_index)

# Print out the index.
print ("The best location for fire station will be sited at location %d" %(center_index))