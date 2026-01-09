# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        '''
        Postorder DFS Solution

        Procedure:
        1) Define a DFS function
        2) Check for base case
            -> If there are no nodes
                -> Return 0
        3) Run the DFS function on the Left and Right
        4) Compare the depths 
        5) Call DFS on root and return subtree root
        '''
        
        def dfs(node):
            if not node:
                return 0, None
            
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)
            
            if left_depth > right_depth:
                return left_depth + 1, left_node
            elif right_depth > left_depth:
                return right_depth + 1, right_node
            else:
                return left_depth + 1, node
        
        return dfs(root)[1]

        #Time Complexity: O(n)
        #Space Complexity: O(h)