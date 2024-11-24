'''
#Definition of Binary Tree Node
#class Node:
#    def __init__(self, val):
#        self.left = None
#        self.right = None
#        self.data = data
'''
#Complete the function below, and return the kth smallest element

def kthSmallest(root, k):
  def inorder(root,k,count):
    if not root:
      return None
      
    left = inorder(root.left, k,count)
    if left is not None:
      return left
      
    count[0] +=1
    
    if count[0] ==k:
      return root.data
      
    return inorder(root.right, k, count)   
    
    
  count =[0]
  return inorder(root,k,count)
  
  
  
  
  
  
