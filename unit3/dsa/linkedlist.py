# insert an node in starting 
# \0 : character used to represent null
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Traversing a Linked List / print all elements of list
def printlist(head):
    curr=head
    while curr!=None:
        print(curr.data, end=" -> ")
    curr=curr.next   

# Adding an Element at the begnning
def addElementInStarting(head, data):
    x=Node(data)
    x.next=head
    return x

# Adding an Element at the end
def addElementInEnding(head,data):
    x=Node(data)
    if head==None:
        return x
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=x
    return head


# Adding an Element after a particular element 
def addElementAfter(head,target,data):
    curr = head
    while curr is not None:
        if curr.data == target:  # Find the target node
            x = Node(data)            # Create a new node
            x.next = curr.next        # Link new node to the next of current
            curr.next = x             # Link current node to the new node
            return head
        curr = curr.next
    print(f"Element {target} not found in the list.")  # If target not found
    return head


# Adding an Element before a particular element 
def addElementBefore(head,target, data):
    if head is None:  # If the list is empty
        print("List is empty")
        return head

    if head.data == target:  # If target is the head
        return addElementInStarting(head, data)

    curr = head
    while curr.next is not None:
        if curr.next.data == target:  # Find the node before the target
            x = Node(data)                 # Create a new node
            x.next = curr.next             # Link new node to the target node
            curr.next = x                  # Link current node to new node
            return head
        curr = curr.next
    print(f"Element {target} not found in the list.")  # If target not found
    return head

# node practiceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNodeAtHead(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        current = self.head
        while current:
            print(current.data,"vbnm", end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    ll = LinkedList()
    n = 4
    value = [1, 2, 4, 5]
    for i in value:
        ll.insertNodeAtHead(i)
        ll.printList()



