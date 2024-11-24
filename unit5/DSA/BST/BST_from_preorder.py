'''
#Definition of Binary Tree Node
#class Node:
#    def __init__(self, val):
#        self.left = None
#        self.right = None
#        self.data = data
'''
#Complete the function below, and return the node of bst

def BSTFromPreorder(arr):
  index = [0]  # Mutable variable to track the current index
  N = len(arr)
  
  def construct_bst(bounds):
      # If we've processed all elements or the current element is out of bounds, return None
      if index[0] >= N or arr[index[0]] < bounds[0] or arr[index[0]] > bounds[1]:
          return None

      # Get the current value and increment the index
      root_val = arr[index[0]]
      index[0] += 1
      
      # Create a new node
      node = Node(root_val)

      # Construct the left and right subtrees with updated bounds
      node.left = construct_bst((bounds[0], root_val))  # Left subtree values are smaller than root_val
      node.right = construct_bst((root_val, bounds[1])) # Right subtree values are greater than root_val
      
      return node
  
  # Call the recursive function with initial bounds
  return construct_bst((float("-inf"), float("inf")))