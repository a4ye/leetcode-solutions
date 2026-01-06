# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelSums = []
        def sumLevel(root, level):
            if root is None:
                return
            
            if level >= len(levelSums):
                levelSums.append(root.val)
            else:
                levelSums[level] += root.val

            sumLevel(root.left, level + 1)
            sumLevel(root.right, level + 1)

        sumLevel(root, 0)

        maxLevel = 0
        maxSum = levelSums[0]
        for i in range(1, len(levelSums)):
            if levelSums[i] > maxSum:
                maxSum = levelSums[i]
                maxLevel = i

        return maxLevel + 1
