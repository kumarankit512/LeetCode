# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Procedure:
        1) Base case
            - If the current node is null, return null
        2) Swap children
            - Swap the left and right child of the current node
        3) Recurse
            - Recursively call the function on the left child
            - Recursively call the function on the right child
        4) Return root
            - After processing, return the root of the inverted subtree
        '''

        if root is None:
            return None

        # swap children
        root.left, root.right = root.right, root.left

        # recurse
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

#Time Complexity: O(n)
#Space Complexity: O(h)