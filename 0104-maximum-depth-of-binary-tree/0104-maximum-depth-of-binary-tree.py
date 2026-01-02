# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        '''
        Recursive DFS Solution

        Procedure:
        1) If root is None, return 0
        2) Recursively find:
            - left_depth = maxDepth(root.left)
            - right_depth = maxDepth(root.right)
        3) Add the left and right depth
            - Return 1 + max(left_depth, right_depth)
        '''

        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)

        #Time Complexity: O(n)
        #Space Complexity: O(h)