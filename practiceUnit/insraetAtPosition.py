class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty linked list

    # Insert a node at a specific position
    def insert_at_position(self, data, position):
        new_node = Node(data)
        
        # If inserting at the head (position 0)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse to the node just before the desired position
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        
        # If the position is beyond the current list length
        if not current:
            print("Position out of bounds")
            return

        # Insert the new node
        new_node.next = current.next
        current.next = new_node

    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.insert_at_position(10, 0)  # Insert at head
ll.insert_at_position(20, 1)  # Insert at position 1
ll.insert_at_position(30, 1)  # Insert at position 1 again
ll.insert_at_position(40, 5)  # Invalid position
ll.display()  # Output: 10 -> 30 -> 20 -> None
