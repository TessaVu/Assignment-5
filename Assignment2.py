# Tessa Vu
# Dr. Edgar
# GEOG 1180-001
# 17 September 2020

# Assignment 2: Build a Simple Grading System

# 1) Write a script that will convert the grade (0~100) to final grade (A, B, C, D, etc.) based on the grade conversion rule in Table 1 below. Print the final grade (A, B, C, D, etc.).
# 2) If the original grade is out of range (> 100 or < 0), the program should print an error message.
# 3) Make sure that your program is precise enough to deal with decimal grades (i.e. if the grade is 93.4, the student will get an A-, but if the grade is 93.5, the user will get an A).
# 4) Add relevant comments where necessary.
# 5) Run the script five times each with a different given original grade to test your script. That is, each time, execute one of the grades while commenting out the others.

# Original grades given below by "Assignment2.py" file.

originalGrade = 93
#originalGrade = 86.6
#originalGrade = 102
#originalGrade = 59.2
#originalGrade = 73.2

if (94 <= round(originalGrade) <= 100):
    print("A")
    
elif (90 <= round(originalGrade) <= 93):
    print("A-")
    
elif (87 <= round(originalGrade) <= 89):
    print("B+")
    
elif (84 <= round(originalGrade) <= 86):
    print("B")
    
elif (80 <= round(originalGrade) <= 83):
    print("B-")
    
elif (78 <= round(originalGrade) <= 79):
    print("C+")
    
elif (75 <= round(originalGrade) <= 77):
    print("C")
    
elif (70 <= round(originalGrade) <= 74):
    print("C-")
    
elif (65 <= round(originalGrade) <= 69):
    print("D+")
    
elif (60 <= round(originalGrade) <= 64):
    print("D")
    
elif (round(originalGrade) < 60):
    print("E")
    
# Error message given if originalGrade is below 0 or over 100.
    
elif ((originalGrade < 0) or (originalGrade > 100)):
    print("Invalid Grade!")
    print("Error: Grade not within range.")