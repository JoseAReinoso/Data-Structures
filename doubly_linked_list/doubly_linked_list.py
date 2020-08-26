"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

 #adding a delete method to apply DRY principle when needing to delete
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        print(new_node.value,"- getting a view of the values")
        self.length += 1
        # If list is empty
        if not self.head and not self.tail:
          self.head = new_node
          self.tail = new_node
          
        else:
          new_node.next = self.head
          self.head.prev = new_node
          self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
      #storing the head value here
        value = self.head.value
      #deleting head pointer of the original head
        self.delete(self.head)
      #pointing the head to our new value
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        # If list is empty
        if not self.head and not self.tail:
          self.head = new_node
          self.tail = new_node
        else:
          #this handles the old tails value by setting the value to none then making the value just before none the tail
          new_node.prev = self.tail
          self.tail.next = new_node
          self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
      #storing the tail value here
        value = self.tail.value
      #deleting the tail pointer
        self.delete(self.tail)
      #adding the tail pointer to the new value thats replacing the old tail
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
      #if input node is already the head return itself
        if node is self.head:
            return
      # otherwise store the nodes value
        value = node.value
      # delete the node (removes the head pointer)
        self.delete(node)
      # inserting back into the list but giving it the head value
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
      # if list is empty return nothing
        if not self.head and not self.tail:
            return
        self.length -= 1
      # if the list is only 1 node long
        if self.head == self.tail:
          self.head = None
          self.tail = None
      # assign the head to the next node (next equals none which deletes the head node)
        elif self.head is node:
          self.head = node.next
          node.delete()
      # assign the tail to the previous node which also points to none which deletes the tail pointer which also deletes the tail node
        elif self.tail is node:
          self.tail = node.prev
          node.delete()
        else:
          node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None:
            return None
        current_node = self.head.next
        max = self.head.value
        while current_node is not None:
            if current_node.value > max:
                max = current_node.value
            current_node = current_node.next
        return max