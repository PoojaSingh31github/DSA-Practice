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

    # Function to rotate the linked list by k positions
    def rotate(self, k):
        if not self.head or k == 0:
            return

        # Step 1: Find the length of the list
        curr = self.head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1

        # Step 2: Link the last node to the head to make it circular
        curr.next = self.head

        # Step 3: Calculate effective k (k % length)
        k = k % length

        # Step 4: Traverse to the (length - k)-th node
        curr = self.head
        for _ in range(length - k - 1):
            curr = curr.next

        # Step 5: Make the (length - k)-th node the new tail, and set new head
        self.head = curr.next
        curr.next = None

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

# Rotate the list by 2 positions
l.rotate(2)

print("List after rotating by 2 positions:")
l.printList()
