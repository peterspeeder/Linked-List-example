# Linked List Implementation in Python

This repository contains a basic implementation of a singly linked list in Python. The linked list consists of two main classes: `Node` and `LinkedList`. The `Node` class defines individual elements of the linked list, each containing a value and a reference to the next node. The `LinkedList` class manages the nodes and provides methods to perform various operations on the linked list.

## Node Class

The `Node` class defines the structure of each node in the linked list. It contains the following methods:

```python
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
  
    def get_next_node(self):
        return self.next_node
  
    def set_next_node(self, next_node):
        self.next_node = next_node
