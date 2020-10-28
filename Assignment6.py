# Tessa Vu
# GEOG 1180-001
# Dr. Edgar
# 15 October 2020

# Assignment 6: Functionizing Assignments 2 & 4

# 1) Assignment 2:
# Please implement a function named "convert_score(os)" which takes the original score as the input, and converts this score into a letter grade based on the conversion rules in Assignment 2. If the conversion is successful, return the letter grade; otherwise, print an error message and return False to indicate the input is invalid. (Reminder: your convert_score(os) function will not generate any output until it is called, which is in the next step.)
# Please write a script that asks the user to input an original score and then calls the convert_score() function to return the user the final grade and print it out to the console. This program only needs to run once, accepting a single original score and printing a single letter grade. A loop is not required for this program. (Hint: input() prompts the user to enter a number and returns the input data as a string variable, this string variable needs to be converted to floating point variable.)

import math # Import math library.

def convert_score(os): # Define the function.
    
    if (94 <= float(os) <= 100): # Create rules for scoring.
        gradeA = "A"
        return gradeA
        
    elif (90 <= float(os) <= 93):
        gradeAminus = "A-"
        return gradeAminus
        
    elif (87 <= float(os) <= 89):
        gradeBplus = "B+"
        return gradeBplus
        
    elif (84 <= float(os) <= 86):
        gradeB = "B"
        return gradeB
        
    elif (80 <= float(os) <= 83):
        gradeBminus = "B-"
        return gradeBminus
        
    elif (78 <= float(os) <= 79):
        gradeCplus = "C+"
        return gradeCplus
        
    elif (75 <= float(os) <= 77):
        gradeC = "C"
        return gradeC
        
    elif (70 <= float(os) <= 74):
        gradeCminus = "C-"
        return gradeCminus
        
    elif (65 <= float(os) <= 69):
        gradeDplus = "D+"
        return gradeDplus
        
    elif (60 <= float(os) <= 64):
        gradeD = "D"
        return gradeD
        
    elif (float(os) < 60):
        gradeE = "E"
        return gradeE
        
    elif ((os < 0) or (os > 100)): # Error message given if os is below 0 or over 100.
        print("Invalid Grade!")
        print("Error: Grade not within range.")
        return False
    
os = input("Enter the score: ") # Prompt user to enter in numerical value.

if os.isdigit():
    os = float(os) # Convert user string input into floating point number.
        
print(convert_score(os)) # Call function and print result.
    
# 2) Assignment 4:
# Please implement a function named "identify_neighbor(point1, point2)", which takes two points as the input and determines whether the Euclidean distance between these two points is less than 536,000 meters. The function should return True if the distance is less than 536,000 meters and False otherwise.
# Please call the identify_neighbor(point1, point2) function in the loop to identify and print out the neighbor IDs of the central point.

# [ID, X coordinate, Y coordinate]
point2 = [[30, 536254.99137, 3659453.06343],
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
point1 = [1, 1073706.744,3658967.925]

def identify_neighbor(point1, point2): # Create a new function and define it.
    
    if (math.sqrt(((point[1] - point1[1]) ** 2) + ((point[2] - point1[2]) ** 2)) < 536000): # If the Euclidean distance is less than 536000.
        print((math.sqrt(((point[1] - point1[1]) ** 2) + ((point[2] - point1[2]) ** 2))))
        print("True")
        return True
    
    else: # If the Euclidean distance is not less than 536000.
        print((math.sqrt(((point[1] - point1[1]) ** 2) + ((point[2] - point1[2]) ** 2))))
        print("False")
        return False

neighbors = [] # Empty list to store values.

for point in point2:
    if (math.sqrt(((point[1] - point1[1]) ** 2) + ((point[2] - point1[2]) ** 2))):
        neighbors.append(point) # Add to neighbors list.
        print(point[0]) # Print IDs.
        identify_neighbor(point1, point2) # Call the function within the for loop.