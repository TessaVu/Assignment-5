'''
Tessa Vu
Dr. Edgar
GEOG 1180-001
26 October 2020
Assignment 9
'''

import math

# Define the number of households with children in Sugarhouse:
p_s = 4089
# Define the attractiveness of Primary Children's Hospital:
p_pc = 4.9
# Define the attractiveness of the Miracle Network Hospital:
p_mn = 4.7

# Define the distances between Sugarhouse and the hospitals:
distance1 = 5.1 # Distance between Sugarhouse and Primary Children's Hospital.
distance2 = 5.9 # Distance between Sugarhouse and Miracle Network Hospital.

# Calculate the interaction between Sugarhouse and the hospitals:
interaction1 = ((1 * p_s * p_pc)/(distance1 ** 2)) # Interaction between Sugarhouse and Primary Children's Hospital.
interaction2 = ((1 * p_s * p_mn)/(distance2 ** 2)) # Interaction between Sugarhouse and Miracle Network Hospital.

# Print the spatial interaction values:
print(interaction1, "is the amount of interaction between Sugarhouse and Primary Children's Hospital.")
print(interaction2, "is the amount of interaction between Sugarhouse and Miracle Network Hospital.")

# Define the distance between two hospitals:
distance3 = 4.7

# Calculate the breaking point between these two hospitals.
# i.e. The point at which a household would tend to go to one hospital over the other.
breaking_point = ((distance3)/(1 + (math.sqrt(p_mn/p_pc))))

#Print the breaking point location: 
print(breaking_point, "is the breaking point location.")