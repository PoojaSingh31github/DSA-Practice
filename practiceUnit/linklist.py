class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insertion at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Insertion after a given node
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node must exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Deletion at the beginning
    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    # Deletion at the end
    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next and temp.next.next:
            temp = temp.next
        temp.next = None

    # Deletion by key
    def delete_by_key(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if not temp:
            print("Key not found")
            return
        prev.next = temp.next
        temp = None

    # Search for an element
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Driver code to test the above implementation

# Create a linked list
llist = LinkedList()

# Insert elements at the beginning
llist.insert_at_beginning(10)
llist.insert_at_beginning(20)

# Insert elements at the end
llist.insert_at_end(30)
llist.insert_at_end(40)

# Insert after a specific node (insert 25 after node with value 20)
node = llist.head
while node and node.data != 20:
    node = node.next
llist.insert_after_node(node, 25)

# Print list
print("Linked List:")
llist.print_list()

# Delete element by key
llist.delete_by_key(25)
print("\nAfter deleting 25:")
llist.print_list()

# Reverse the linked list
llist.reverse()
print("\nAfter reversing:")
llist.print_list()

# Delete element at the beginning
llist.delete_at_beginning()
print("\nAfter deleting at beginning:")
llist.print_list()

# Delete element at the end
llist.delete_at_end()
print("\nAfter deleting at end:")
llist.print_list()

# Search for an element
print("\nIs 30 in the list?", llist.search(30))
print("Is 25 in the list?", llist.search(25))
