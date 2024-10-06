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
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def addOne(self):
        self.reverse()
        curr = self.head
        carry = 1 
        while curr:
            new_val = curr.data + carry
            carry = new_val // 10
            curr.data = new_val % 10
            if carry == 0:
                break
            if curr.next is None and carry:
                curr.next = Node(carry) 
                break
            curr = curr.next
        self.reverse()
        
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print(None)

# Example usage
l = LinkedList()
l.insertAtEnd(1)
l.insertAtEnd(9)
l.insertAtEnd(9)

print("Original list:")
l.printList()

l.addOne()

print("List after adding 1:")
l.printList()
