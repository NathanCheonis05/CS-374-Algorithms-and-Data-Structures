'''

Authors: Nathan Cheonis

Description: This file contains a Hashtable class that uses hasing to set, get, delete, rehash, 
and displays the value(s) of a Hashtable. 
'''

# The dictionary key is the name of the country and the value is the population of the country
# The population is an integer value

class Hashtbale:
    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.elements = [[] for i in range(self.bucket_size)]
        self.assign_buckets(elements)
    
    def assign_buckets(self, elements):
        for key, value in elements:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size
            self.elements[index].append((key, value))
    
    def get_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        bucket = self.elements[index]
        for key, value in bucket:
            if key == input_key:
                return(value)
        return None
    
    def delete_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        bucket = self.elements[index]
        for i in range(len(bucket)):
            if bucket[i][0] == input_key:
                del bucket[i]
                return True
        return False
    
    def __str__(self):
        return str(self.elements)