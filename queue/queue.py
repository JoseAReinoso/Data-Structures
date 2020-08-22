"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   "Same thing as stack except you're just adding to the head and removing from the tail
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

""" NOTE= For some reason this is not working when trying to import from another directory
import sys 
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList
"""
#Created a local copy  of the singly_linked_list.py as import would work this way
#and then just imported the module using its local copy vervsion
from copiedSinglyLinked import LinkedList 

#print(LinkedList())


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        print(self.size)
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        value = self.storage.remove_head()
        print(value)
        return value
        
