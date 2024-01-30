#!/usr/bin/python3
def weight_average(my_list=[]):
    weights = 0
    average = 0
    for i in my_list:
        average += i[0] * i[1]
        weights += i[1]
    if weights != 0:
        average = average / weights
    return average
