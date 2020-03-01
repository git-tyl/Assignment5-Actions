import math


def firstrun():
    return "Success"


# get the area of a circle
def get_area_of_circle(radius):
    return math.pi * radius * radius


# return the first and last element in an array
def get_first_and_last_elements(array):

    length_of_array = len(array)

    if len(array) >= 2:
        return [array[0], array[length_of_array - 1]]

    return "Invalid Input"
