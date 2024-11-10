from collections import defaultdict, deque

"""
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
class Solution:
  def diagonalTraversal(self, root):
    if not root:
      return []
      
    dic = defaultdict(list)
    queue = deque([(root, 0)])

    while queue:
      node, hd = queue.popleft()
      dic[hd].append(node.data)
      if node.left:
        queue.append((node.left, hd + 1))
      if node.right:
        queue.append((node.right, hd))
        
    result = []
    for diagonal in sorted(dic.keys()):
        result.extend(dic[diagonal])

    return result    
    pass
