from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque()
        q.append(root)
        serialized = []
        while q:
            node = q.popleft()
            if node:
                serialized.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                serialized.append(".")

        return " ".join(serialized)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        nodes = data.split(" ")

        if nodes[0] == ".":
            return None

        head = TreeNode(int(nodes[0]))
        nodes[0] = head
        currIndex = 0
        childIndex = 1
        print(nodes)
        while childIndex < len(nodes):
            if not nodes[currIndex]:
                currIndex += 1
                continue

            if nodes[childIndex] != ".":
                nodes[currIndex].left = TreeNode(int(nodes[childIndex]))
                nodes[childIndex] = nodes[currIndex].left
            else:
                nodes[childIndex] = None
            childIndex += 1

            if childIndex >= len(nodes):
                break

            if nodes[childIndex] != ".":
                nodes[currIndex].right = TreeNode(int(nodes[childIndex]))
                nodes[childIndex] = nodes[currIndex].right
            else:
                nodes[childIndex] = None
            childIndex += 1

            currIndex += 1

        return head
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
