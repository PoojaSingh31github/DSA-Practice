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

    # Function to split the linked list into two halves
    def split(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None  # Split the list into two halves
        return head, middle

    # Function to merge two sorted linked lists
    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        
        if left.data < right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)
        return result

    # Merge Sort function
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        
        left, right = self.split(head)
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        return self.merge(left, right)

    # Function to sort the linked list
    def sort(self):
        self.head = self.mergeSort(self.head)

    # Helper function to print the linked list
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print(None)

# Example usage:
l = LinkedList()
l.insertAtEnd(4)
l.insertAtEnd(2)
l.insertAtEnd(3)
l.insertAtEnd(1)
l.insertAtEnd(5)

print("Original list:")
l.printList()

# Sort the linked list
l.sort()

print("Sorted list:")
l.printList()
