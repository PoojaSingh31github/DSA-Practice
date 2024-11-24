'''
#Definition of Binary Tree Node
#class Node:
#    def __init__(self, val):
#        self.left = None
#        self.right = None
#        self.data = data
'''
#Complete the function below, and inorder successor of the node X, or else -1.

def inorderSuccessor(root, X):
  p=None
  curr=root
  while curr:
    if X.data < curr.data:
      p=curr
      curr = curr.left
      
    elif X.data > curr.data:
      curr=curr.right
      
    else:
      if curr.right:
        temp = curr.right
        
        while temp.left:
          temp = temp.left
        p=temp
      break
  return p.data if p else -1
