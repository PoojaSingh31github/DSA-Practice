'''
#Definition of Binary Tree Node
#class Node:
#    def __init__(self, val):
#        self.left = None
#        self.right = None
#        self.data = data
'''
#Complete the function below

def largestBst(root):
  def helper(node):
    if not node:
      return (True, 0, float("inf"), float("-inf"))
    left_bst, left_size, left_min, left_max = helper(node.left)
    right_bst, right_size, right_min, right_max = helper(node.right)    
    if left_bst and  right_bst and node.data > left_max and node.data < right_min:
      size = left_size + right_size + 1
      min_value = min(node.data, left_min)
      max_value = max(node.data, right_max)
      return (True, size, min_value, max_value)
    else:
      return (False, max(left_size,right_size ), 0, 0)
  _, largest_size , _, _ = helper(root)
  return largest_size
  
      
