# Calulate Paint Area Cans
import math
h = int(input("Enter Height"))
w = int(input("Enter Width"))
cover = 5


def getInput(height, width, coverage):
    number_of_cans = (height*width)/coverage
    return math.ceil(number_of_cans)


print(f"To cover this area, we will need {getInput(h, w, cover)} cans.")
