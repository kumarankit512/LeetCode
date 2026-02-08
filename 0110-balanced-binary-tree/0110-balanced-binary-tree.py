# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        '''
        Procedure:
        1) Define a dfs function 
            - Return the height of the subtree if it is balanced else -1
        2) If node is None, return height 0
        3) Recursively compute:
            left_height = dfs(node.left)
            right_height = dfs(node.right)
        4) If either side returns -1, propagate -1 upward
        5) If abs(left_height - right_height) > 1:
            - Tree is unbalanced -> return -1
            Otherwise:
            - Return 1 + max(left_height, right_height)
        6) In the end
            - If dfs(root) == -1 -> not balanced
            - Else -> balanced
        '''

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            if left == -1:
                return -1
            
            right = dfs(node.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
        
        return dfs(root) != -1
    
    #Time Complexity: O(n)
    #Space Complexity: O(h)