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

    # Function to add two linked lists
    def add_two_linked_lists(self, l1, l2):
        dummy = Node(0)  # Dummy node to simplify code
        p = l1.head
        q = l2.head
        current = dummy
        carry = 0
        
        while p is not None or q is not None:
            x = p.data if p is not None else 0
            y = q.data if q is not None else 0
            
            # Calculate sum and carry
            total = carry + x + y
            carry = total // 10
            current.next = Node(total % 10)  # Create a new node with the sum's digit
            current = current.next
            
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        
        if carry > 0:
            current.next = Node(carry)  # If there's a carry left, add it as a new node
        
        return LinkedList.from_node(dummy.next)  # Return the new linked list

    # Function to create a linked list from a given node (for return value)
    @staticmethod
    def from_node(node):
        linked_list = LinkedList()
        while node:
            linked_list.insertAtEnd(node.data)
            node = node.next
        return linked_list

    # Function to print the linked list
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print(None)

# Example usage:
l1 = LinkedList()
l1.insertAtEnd(2)
l1.insertAtEnd(4)
l1.insertAtEnd(3)  # Represents the number 342

l2 = LinkedList()
l2.insertAtEnd(5)
l2.insertAtEnd(6)
l2.insertAtEnd(4)  # Represents the number 465

print("Linked List 1:")
l1.printList()

print("Linked List 2:")
l2.printList()

# Add the two linked lists
result = l1.add_two_linked_lists(l1, l2)

print("Result Linked List after adding:")
result.printList()
