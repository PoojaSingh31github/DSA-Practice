class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkList:
    def __init__(self):
        self.head = None

    def insertAtHead(self,data):
        x=Node(data)
        x.next = self.head
        self.head=x

    def printList(self):
        curr=self.head
        while curr:
            print(curr.data, end="->")
            curr=curr.next
        print(None)    

l=linkList()
l.insertAtHead(3)
l.insertAtHead(2)
l.insertAtHead(1)
l.insertAtHead(13)
l.insertAtHead(12)
l.insertAtHead(11)
l.insertAtHead(10)
l.printList()
