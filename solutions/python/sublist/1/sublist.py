"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'The first list is sublist of the second list'
SUPERLIST = 'The first list is superlist of the second list'
EQUAL = 'The two lists are equal'
UNEQUAL = 'The two lists are unequal'

def contains(long, short):
    size = len(short)
    for start in range(len(long) - size + 1):
        if long[start:start + size] == short:
            return True
    return False
    
def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
        
    if contains(list_one, list_two):
        return SUPERLIST
        
    if contains(list_two, list_one):
        return SUBLIST
        
    return UNEQUAL
        
        
