'''

test.py

Author: Nathan Cheonis

This file contains a list of tuples containing the names and populations of the 
top 5 populus countries accoridng to www.worldometers.info

URL: https://www.worldometers.info/world-population/population-by-country/
'''


from hashtable import Hashtable

populations = [
    ('India', 1450935791),
    ('China', 1419321278),
    ('USA', 345426371),
    ('Indonesia', 283487931),
    ('Pakistan', 251269164)
]

pop_hash = Hashtable(populations)

pop_hash.__str__()