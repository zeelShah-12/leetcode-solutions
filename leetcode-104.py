# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node, level):
            if not node:
                return level - 1  # Return the current depth when reaching a leaf node.
            
            # Recursively calculate the depth of left and right subtrees.
            left_depth = helper(node.left, level + 1)
            right_depth = helper(node.right, level + 1)
            
            # Return the maximum depth.
            return max(left_depth, right_depth)
        
        return helper(root, 1)  # Start with level 1 for the root.