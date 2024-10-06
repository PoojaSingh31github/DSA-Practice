class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linklist:
    def __init__(self):
        self.head = None

    def insertAtpos(self,data,position):
        x = Node(data)
        if position == 0:
            x.next = self.head
            self.head = x
            return 
        curr=self.head
        for i in range(position - 1):
            if curr is None:
                 print("curr is None")
            curr = curr.next 
        x.next=curr.next
        curr.next = x

    def printList(self):
        curr=self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next                     
        print(None)
l=linklist()
l.insertAtpos(3, 0)
l.insertAtpos(8, 1)
l.insertAtpos(7, 2)
l.insertAtpos(6, 2)
l.insertAtpos(6, 2)
l.insertAtpos(1, 2)
l.printList()


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insertAtpos(self, data, position):
#         new_node = Node(data)
        
#         # Inserting at position 0 (head of the list)
#         if position == 0:
#             new_node.next = self.head
#             self.head = new_node
#             return
        
#         # Traverse to the node before the desired position
#         current = self.head
#         for i in range(position - 1):
#             if current is None:  # If the position is out of bounds
#                 raise IndexError("Position out of bounds")
#             current = current.next
        
#         # Insert the new node at the desired position
#         new_node.next = current.next
#         current.next = new_node

#     def printList(self):
#         curr = self.head
#         while curr:
#             print(curr.data, end=" -> ")
#             curr = curr.next
#         print(None)

# # Example usage:
# l = LinkedList()
# l.insertAtpos(3, 0)  # Insert 3 at position 0
# l.insertAtpos(8, 1)  # Insert 8 at position 1
# l.insertAtpos(7, 2)  # Insert 7 at position 2
# l.insertAtpos(6, 2)  # Insert 6 at position 2 (push 7 and 8 further down)
# l.insertAtpos(1, 2)  # Insert 1 at position 2

# l.printList()
