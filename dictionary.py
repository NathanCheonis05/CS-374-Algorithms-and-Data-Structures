'''

Authors: Nathan Cheonis

Description: This file contains a dictionary class that uses  . 
'''

# The dictionary key is the name of the country and the value is the population of the country
# The population is an integer value

class Dictionary:
    def __init__(self, size=10):
        # Initializing the dictionary with empty buckets
        self.size = size
        self.data = [None] * size
    
    def _hash(self, key):
        # Hash function to determine the index of the key
        return hash(key) % self.size
    
    def set(self, key, value):
        # Inserting a key-value pair into the dictionary
        index = self._hash(key)
        start_index = index
        # Using a while loop to handle collisons
        
        while self.data[index] is not None:
            current_key, _ = self.data[index]
            if current_key == key:
                # If the key already exists in the dictionary, update the value
                self.data[index] = (key, value)
                return
            index = (index + 1) % self.size
            if index == start_index:
                raise Exception("Dictioanry is Full")
        
        self.data[index] = (key, value)
        
    def get(self, key):
        # the get function return the value of a key
        index = self._hash(key)
        start_index = index
        
        while self.data[index] is not None:
            current_key, value = self.data[index]
            if current_key == key:
                return value
            index = (index + 1) % self.size
            if index == start_index:
                return None
    
    def delete(self, key):
        # The delete function removes a key-value pair from the dictionary
        index = self._hash(key)
        start_index = index
        
        while self.data[index] is not None:
            current_key, _ = self.data[index]
            if current_key == key:
                self.data[index] = None
                self._rehash(index)
                return True
            index = (index + 1) % self.size
        if index == start_index:
            return False
        
    def _rehash(self, delete_index):
        index = (delete_index + 1) % self.size
        while self.data[index] is not None:
            key, value = self.data[index]
            # Remove the key-value pair from the dictionary
            self.data[index] = None
            self.set(key, value)
            index = (index + 1) % self
    
    def display(self):
        # Displays the data stored in the dictionary
        for i in range(self.size):
            if self.data[i] is not None:
                print(self.data[i])
                