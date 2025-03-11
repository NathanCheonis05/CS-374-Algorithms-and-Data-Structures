'''

Authors: Nathan Cheonis

Description: This file contains a dictionary data structure containing populations
of countries that start with the letter'A'. 
'''

# The dictionary key is the name of the country and the value is the population of the country
# The population is an integer value

class populations:
    def __init__(self, size=10):
        self.size = size
        self.data = [None] * size
    
    def dict_hash(self, key):
        return len(key) % self.size
    
    