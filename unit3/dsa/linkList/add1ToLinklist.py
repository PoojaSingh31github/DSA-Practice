
# class Node(1:

#     def __init__(self, data):   # data -> value stored in node
#         self.data = data
#         self.next = None
# '''

class Solution:
    def addOne(self,head):
        def reverse(head):
            if not head:
                return 
            after =None
            before = None
            curr = head
            while curr:
                after = curr.next
                curr.next = before
                before = curr
                curr = after
            return before
        head =  reverse(head)
        temp = head
        while temp:
            if temp.data != 9:
                temp.data = temp.data + 1
                break
            if temp.data == 9:
                temp.data = 0
                if temp.next is None:
                    newNode = Node(1)
                    temp.next = newNode
                    break
                else:
                    temp = temp.next
        
        head =  reverse(head)
        return head
                    