from collections import deque

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def insert(root, val):
    if root is None:
        return Node(val)
    else:
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
    return root

class Solution:
    def levelOrder(self, root):
        if not root:
            return  
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res


    def util(self, root, hd, level, freq):
        if not root:
            return
        
        if hd not in freq or level < freq[hd][1]:
            freq[hd] = (root.val, level)
        
        self.util(root.left, hd - 1, level + 1, freq)
        self.util(root.right, hd + 1, level + 1, freq)

    def topView(self, root):
        freq = {}
        self.util(root, 0, 0, freq)
        
        sortedVal = sorted(freq.keys())
        res = [freq[hd][0] for hd in sortedVal]
        
        return res


values = [5, 6, 4, 7, 2]
root = None


for value in values:
    root = insert(root, value)

solution = Solution()
# top_view = sorted(solution.levelOrder(root), reverse=True)
levelorder = solution.levelOrder(root)
print("Level order traversal :", levelorder)
# print("Top View of the Binary Tree:", top_view)