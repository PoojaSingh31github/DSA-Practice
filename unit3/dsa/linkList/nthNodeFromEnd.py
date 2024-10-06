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

    def findNthFromEnd(self, n):
        fast = self.head
        slow = self.head

        for _ in range(n):
            if fast is None:
                print(f"The list has less than {n} nodes.")
                return None
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        print(f"The {n}th node from the end is: {slow.data}")
        return slow

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

l.printList()

l.findNthFromEnd(2)
