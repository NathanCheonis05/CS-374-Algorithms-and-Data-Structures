'''

Author: Nathan Cheonis

Description: This file contains a Hashtable class that uses hasing to assign buckets, 
get, delete, and displays the value(s) of a Hashtable. 
'''



class Hashtable:
    # This sets the size of the bucket and creates initializes the elements as an empty list
    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.elements = [[] for i in range(self.bucket_size)]
        self.assign_buckets(elements)
    
    def assign_buckets(self, elements):
        # Loops over the elements and assigns them to a bucket
        # This is done by using the hash function to get the index of the bucket
        for key, value in elements:
            hashed_element = hash(key)
            # The modulo operator is used to map the hash to a bucket
            index = hashed_element % self.bucket_size
            self.elements[index].append((key, value))
    
    def get_value(self, input_key):
        # Gets the values of a key by hashing the key and finding the index of the bucket
        hashed_element = hash(input_key)
        index = hashed_element % self.bucket_size
        bucket = self.elements[index]
        # Iterates over the bucket to find the key and return the value
        for key, value in bucket:
            if key == input_key:
                return(value)
        return None
    
    def delete_value(self, input_key):
        # Computes the hash of a key and finds the index of the bucket
        hashed_element = hash(input_key)
        index = hashed_element % self.bucket_size
        bucket = self.elements[index]
        # Loops over the bucket to find the key and then it is deleted
        for i in range(len(bucket)):
            if bucket[i][0] == input_key:
                del bucket[i]
                return True
        return False
    
    def __str__(self):
        # Returns the elements of the Hashtable
        return str(self.elements)