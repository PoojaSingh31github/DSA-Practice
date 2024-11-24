
 # Definition for a binary tree TreeNode.
 # class Node:
 # def __init__(self, key):
 # 	self.left = None
 # 	self.right = None
 # 	self.val = key
 

def inorderPredecessor(root, key):
  p=None
  curr=root
  while curr:
    if key > curr.val:
      p=curr
      curr= curr.right
    elif key<curr.val:
      curr=curr.left
    else:
      if curr.left:
        temp = curr.left
        while temp.right:
          temp=temp.right
        p=temp
      break
  return p.val if p else -1
    
