"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
  the run time difference.. when you add to an array it takes time to move ALL the values over to fit new value. 
   in linked list all you have to do is update the head and tail.
   it will be O(n) when adding to tail/head

"""
""" IMPORTING FROM AN OUTER DIRECTORY WONT WORK FOR SOME REASON.
import sys 
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList
"""

from copiedSinglyLinked import LinkedList 




class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        print(self.size , " - this is reflecting size changes!!!!")
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            node = self.storage.remove_head()
            return node

        
