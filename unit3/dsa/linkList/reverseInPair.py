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

    # Function to reverse the linked list in pairs
    def reverseInPairs(self):
        if not self.head or not self.head.next:
            return self.head

        # Initialize previous and current pointers
        prev = None
        curr = self.head
        self.head = curr.next  # New head of the list after reversing the first pair

        # Traverse the list and reverse in pairs
        while curr and curr.next:
            next_pair = curr.next.next  # Keep track of the next pair
            second = curr.next          # Second node of the current pair

            # Swap the current pair
            second.next = curr
            curr.next = next_pair

            # Update the previous pair to point to the new head of this reversed pair
            if prev:
                prev.next = second

            # Move to the next pair
            prev = curr
            curr = next_pair

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
l.insertAtEnd(2)
l.insertAtEnd(3)
l.insertAtEnd(4)
l.insertAtEnd(5)

print("Original list:")
l.printList()

# Reverse the list in pairs
l.reverseInPairs()

print("List after reversing in pairs:")
l.printList()
