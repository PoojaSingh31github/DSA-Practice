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

    # Helper function to reverse a linked list
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    # Function to check if the linked list is a palindrome
    def isPalindrome(self):
        # if not self.head or not self.head.next:
        #     return True

        # # Step 1: Find the middle of the linked list
        # slow, fast = self.head, self.head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # # Step 2: Reverse the second half of the linked list
        # second_half_start = self.reverse(slow)

        # # Step 3: Compare the first and second halves
        # first_half_start = self.head
        # second_half_copy = second_half_start  # Keep a copy to restore the list later
        # is_palindrome = True
        # while second_half_start:
        #     if first_half_start.data != second_half_start.data:
        #         is_palindrome = False
        #         break
        #     first_half_start = first_half_start.next
        #     second_half_start = second_half_start.next

        # # Step 4: Restore the second half of the list (optional)
        # self.reverse(second_half_copy)

        # return is_palindrome
        res=[]
        curr=self.head
        while curr:
            res.append(curr.data)
            curr=curr.next
        return res==res[::-1] 

    # Helper function to print the linked list
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
l.insertAtEnd(2)
l.insertAtEnd(1)

l.printList()

if l.isPalindrome():
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
