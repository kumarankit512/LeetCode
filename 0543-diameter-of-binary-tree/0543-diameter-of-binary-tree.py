# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Procedure:
        1) Define a helper function that computes the height (max depth) of a subtree
            - Height of a node = 1 + max(left height, right height)
        2) While computing height, also check the longest path that goes through that node
            - Path length = left height + right height
        3) Keep track of the maximum diameter seen so far in a variable
        4) Return result after DFS traversal finishes
        '''

        self.maxDiameter = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # Update diameter
            self.maxDiameter = max(self.maxDiameter, left + right)

            # Return height of subtree
            return 1 + max(left, right)

        dfs(root)
        return self.maxDiameter

#Time Complexity: O(n)
#Space Complexity: O(h)