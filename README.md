# Linked List Implementation in Python

This repository provides a basic implementation of a singly linked list in Python. The linked list consists of two main classes: `Node` and `LinkedList`. It's a fundamental data structure with the `Node` class representing individual elements and the `LinkedList` class managing them.

## Node Class

The `Node` class defines the structure of each node in the linked list. It holds a `value` and a reference to the `next_node` which points to the following node.

### Constructor

```python
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
```

methods
get_value(self): Retrieve the value stored in the node.
get_next_node(self): Get the reference to the next node.
set_next_node(self, next_node): Set the reference to the next node.

## LinkedList Class
The LinkedList class manages a sequence of linked nodes and offers various methods for working with the list.

### Constructor 
```python
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
```
Methods:

get_head_node(self): Get the head node of the linked list.
insert_beginning(self, new_value): Insert a new node with the given value at the beginning.
stringify_list(self): Convert the linked list to a printable string.

## Removing Nodes
Additionally, there's a method to remove nodes from the linked list:
```python
def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    # ... (Code to remove a node by value)
```
This repository is a useful resource for understanding linked lists and practicing object-oriented programming in Python. Feel free to explore and adapt the code to your needs.

For a detailed example and usage instructions, check the provided code in this repository.
