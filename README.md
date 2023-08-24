# Linked List Implementation in Python

## Overview

This repository provides a basic implementation of a singly linked list in Python. The linked list consists of two main classes: `Node` and `LinkedList`. The `Node` class defines individual elements of the linked list, each containing a value and a reference to the next node. The `LinkedList` class manages the nodes and provides methods to perform various operations on the linked list.

## Node Class

The `Node` class defines the structure of each node in the linked list. Each node contains a `value` representing the data it holds, and a reference to the `next_node` that comes after it in the linked list. This class provides methods to access and modify these attributes.

### Constructor

```python
class Node:
    def __init__(self, value, next_node=None):
        # Initialize a new Node with a value and an optional next_node
        self.value = value
        self.next_node = next_node
The __init__ method creates a new node with the given value. The optional next_node parameter allows linking nodes together to form the linked list.

Methods
get_value(self): Returns the value stored in the node.

get_next_node(self): Returns the reference to the next node in the linked list.

set_next_node(self, next_node): Sets the reference to the next node.

python
Copy code
    def get_value(self):
        # Get the value of the Node
        return self.value
  
    def get_next_node(self):
        # Get the next_node of the Node
        return self.next_node
  
    def set_next_node(self, next_node):
        # Set the next_node of the Node
        self.next_node = next_node
The get_value method retrieves the value stored in the node, and the get_next_node method returns the reference to the next node. The set_next_node method allows changing the reference to the next node.

LinkedList Class
The LinkedList class manages a sequence of linked nodes. It includes methods for creating, modifying, and visualizing the linked list.

Constructor
python
Copy code
class LinkedList:
    def __init__(self, value=None):
        # Initialize a new LinkedList with a value (head_node)
        self.head_node = Node(value)
The LinkedList constructor initializes a new linked list with an optional initial value to be stored in the head node.

Methods
get_head_node(self): Returns the head node of the linked list.

insert_beginning(self, new_value): Inserts a new node with the given value at the beginning of the linked list.

stringify_list(self): Converts the linked list into a string for printing.

python
Copy code
    def get_head_node(self):
        # Get the head_node of the LinkedList
        return self.head_node
    
    def insert_beginning(self, new_value):
        # Insert a new Node with new_value at the beginning of the LinkedList
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        # Convert the LinkedList to a string for printing
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
Example Usage
For a detailed example and usage instructions, please refer to the provided code in this repository. The linked list implementation can be used to understand the basics of data structures and practice object-oriented programming concepts in Python.

Feel free to explore and modify the code to suit your needs!
