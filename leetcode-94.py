# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
             stack.append(cur)  # Push current node to stack
             cur = cur.left     # Move to the left child
            cur = stack.pop()       # Pop the top of the stack
            result.append(cur.val)  # Add the node's value to result
            cur = cur.right         # Move to the right child
        return result
