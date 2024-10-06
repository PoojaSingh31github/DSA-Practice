class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Helper function to add a node at the end
    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # Function to fill the gaps in a sorted list
    def fillGaps(self):
        curr = self.head
        while curr and curr.next:
            next_data = curr.next.data
            # If there's a gap between curr.data and next_data, fill it
            while curr.data + 1 < next_data:
                new_node = Node(curr.data + 1)
                new_node.next = curr.next
                curr.next = new_node
                curr = curr.next
            curr = curr.next

    # Helper function to print the linked list
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print(None)

# Example usage:
l = LinkedList()
l.insertAtEnd(1)
l.insertAtEnd(3)
l.insertAtEnd(6)
l.insertAtEnd(7)

print("Original list with gaps:")
l.printList()

# Fill the gaps
l.fillGaps()

print("List after filling gaps:")
l.printList()
