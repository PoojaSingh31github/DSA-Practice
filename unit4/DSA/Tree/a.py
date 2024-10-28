# Definition for a binary tree node.
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Solution:
    def __init__(self):
        self.ans = []  # To store the final result

    def find_nodes_at_distance_k(self, root, k):
        if not root or k < 0:
            return
        if k == 0:
            self.ans.append(root.val)
            return
        self.find_nodes_at_distance_k(root.left, k - 1)
        self.find_nodes_at_distance_k(root.right, k - 1)

    def distance_from_target(self, root, target, k):
        if not root:
            return -1
        if root.val == target:
            self.find_nodes_at_distance_k(root, k)
            return 0

        left_distance = self.distance_from_target(root.left, target, k)
        if left_distance != -1:
            if left_distance + 1 == k:
                self.ans.append(root.val)
            else:
                self.find_nodes_at_distance_k(root.right, k - left_distance - 2)
            return left_distance + 1

        right_distance = self.distance_from_target(root.right, target, k)
        if right_distance != -1:
            if right_distance + 1 == k:
                self.ans.append(root.val)
            else:
                self.find_nodes_at_distance_k(root.left, k - right_distance - 2)
            return right_distance + 1

        return -1

    def atDistanceK(self, root, target, k):
        self.distance_from_target(root, target, k)
        return self.ans
