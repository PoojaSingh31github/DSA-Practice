class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def detectCycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                print("Cycle detected!")
                return True

        print("No cycle detected.")
        return False

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
l.insert
