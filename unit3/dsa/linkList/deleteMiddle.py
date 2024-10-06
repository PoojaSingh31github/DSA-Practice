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

    def deleteMiddle(self):
        if not self.head or not self.head.next:
            self.head = None
            return
        slow = self.head
        fast = self.head
        prev = None
        
        while fast and fast.next:
            prev = slow  
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next  

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
l.deleteMiddle()
l.printList()
