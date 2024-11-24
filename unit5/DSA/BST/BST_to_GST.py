'''
#Definition of Binary Tree Node
#class Node:
#    def __init__(self, val):
#        self.left = None
#        self.right = None
#        self.data = data
'''
#Complete the function below, and return the head of new tree

def bstToGst(root):
  def reverse(node, acc_sum):
    if not node:
      return acc_sum
    
    acc_sum = reverse(node.right, acc_sum) 
    node.data +=acc_sum
    acc_sum = node.data
    
    acc_sum = reverse(node.left, acc_sum) 
    return acc_sum
  
  reverse(root, 0)  
  return root

