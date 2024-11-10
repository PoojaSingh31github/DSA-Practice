# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below and use the array given

main_arr = []

class Solution:
    def atKDist(self, root, k):
      if not root:
        return 
      if k==0:
        main_arr.append(root.val)
      self.atKDist(root.left, k-1)  
      self.atKDist(root.right, k-1)  
      return main_arr
      
