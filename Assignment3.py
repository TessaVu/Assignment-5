# Tessa Vu
# Dr. Edgar
# GEOG 1180-001
# 24 September 2020

# Assignment 3: Summation

# 1) Write a while-loop that asks the user to input integers one by one until the user inputs "End". When the loop stops, print the summation of the input integers.
    # Hint: The stop condition is the input == "End".
    
# 2) The input is considered valid if it is an integer. Any other input is considered to be invalid. If the input is invalid, print "Error" and ask the user to input a new number.

num = 0

while input != "End":
    number = input("Enter an integer: ")
    if number.isdigit() is True:
        number = int(number)
        number += num
        continue
    elif number.isdigit() is False:
        print ("Error:", number, "is not a valid integer. Try again.")
        continue
    elif input == "End":
        print(number)
        break