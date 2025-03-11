'''

Authors: Nathan Cheonis

Description: This file contains a dictionary class that uses . 
'''

# The dictionary key is the name of the country and the value is the population of the country
# The population is an integer value

class dictionary:
    def __init__(self, size=10):
        # Initializing the dictionary with empty buckets
        self.size = size
        self.data = [None] * size
    
    def dict_hash(self, key):
        # Hash function to determine the index of the key
        return len(key) % self.size
    
    def set(self, key, value):
        # Inserting a key-value pair into the dictionary
        index = self.dict_hash(key)
        
        # Using a while loop to handle collisons
        
        while self.data[index] is not None:
            sorted_key, _ = self.data[index]
            if sorted_key == key:
                # If the key already exists in the dictionary, update the value
                self.data[index] = (key, value)
                return
            index = (index + 1) % self.size
        
        self.data[index] = (key, value)
        
    def get(self, key):
        # the get function return the value of a key
        index = self.dict_hash(key)
        
        while self.data[index] is not None:
            sorted_key, value = self.data[index]
            if sorted_key == key:
                return value
            index = (index + 1) % self.size
        
        return None
    
    def delete(self, key):
        # The delete function removes a key-value pair from the dictionary
        index = self.dict_hash(key)
        
        while self.data[index] is not None:
            sorted_key, _ = self.data[index]
            if sorted_key == key:
                self.data[index] = None
                return
            index = (index + 1) % self.size
        
        return False
    
    def display(self):
        # Displays the data stored in the dictionary
        for i in range(self.size):
            if self.data[i] is not None:
                print(self.data[i])
                