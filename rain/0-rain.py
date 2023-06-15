#!/usr/bin/python3
""" Rain module """


def rain(walls):
    """ Rain method """
    total_units = 0
    width = 0
    height = 0
    last_wall = 0

    for i in range(len(walls)):
        if walls[i] != 0:
            height = last_wall if last_wall < walls[i] else walls[i]
            total_units += height * width
            last_wall = walls[i]
            width = 0
        else:
            width += 1

    return total_units
