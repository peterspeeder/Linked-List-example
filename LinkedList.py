class Node:
    def __init__(self, value, next_node=None):
        # Initialize a new Node with a value and an optional next_node
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        # Get the value of the Node
        return self.value
  
    def get_next_node(self):
        # Get the next_node of the Node
        return self.next_node
  
    def set_next_node(self, next_node):
        # Set the next_node of the Node
        self.next_node = next_node

class LinkedList:
    def __init__(self, value=None):
        # Initialize a new LinkedList with a value (head_node)
        self.head_node = Node(value)
      
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


def remove_node(self, value_to_remove):
    current_node = self.get_head_node()  # Get the head_node of the LinkedList
    if current_node.get_value() == value_to_remove:
        # If the head_node's value matches the value to remove,
        # set the head_node to the next_node
        self.head_node = current_node.get_next_node()
    else:
        while current_node:
            next_node = current_node.get_next_node()  # Get the next_node
            if next_node.get_value() == value_to_remove:
                # If the next_node's value matches the value to remove,
                # skip over the next_node by setting the current_node's next_node
                # to the next_node's next_node
                current_node.set_next_node(next_node.get_next_node())
                current_node = None  # Exit the loop by setting current_node to None
            else:
                current_node = next_node  # Move to the next_node for further checking




# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)  # Create a LinkedList with a head node of value 5
ll.insert_beginning(70)  # Insert a new node at the beginning with value 70
ll.insert_beginning(5675)  # Insert another node at the beginning with value 5675
ll.insert_beginning(90)  # Insert yet another node at the beginning with value 90
print(ll.stringify_list())  # Print the values in the LinkedList
