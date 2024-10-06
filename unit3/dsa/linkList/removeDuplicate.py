class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Function to add a node at the end
    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # Function to remove duplicates from the linked list
    def remove_duplicates(self):
        current = self.head
        seen = set()
        prev = None
        
        while current:
            if current.data in seen:
                # Remove the duplicate node
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            
            current = current.next

    # Function to print the linked list
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print(None)

# Example usage:
l = LinkedList()
l.insertAtEnd(1)
l.insertAtEnd(2)
l.insertAtEnd(3)
l.insertAtEnd(2)  # Duplicate
l.insertAtEnd(4)
l.insertAtEnd(1)  # Duplicate

print("Original linked list:")
l.printList()

# Remove duplicates
l.remove_duplicates()

print("Linked list after removing duplicates:")
l.printList()
