# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below

class Solution:
  def __init__(self):
    self.ans=0
  def diameter(self, root):
    def dfs(root):
      if root is None:
          return 0
      left_depth = dfs(root.left)
      right_depth = dfs(root.right)
      self.ans = max(self.ans, left_depth + right_depth+1)
      return max(left_depth, right_depth) + 1

    dfs(root)
    return self.ans