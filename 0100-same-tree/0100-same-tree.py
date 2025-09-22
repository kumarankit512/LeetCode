# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        1) Base cases
            - If both nodes are null, return true (both subtrees are empty)
            - If one node is null and the other is not, return false
            - If the values of the two nodes are not equal, return false
        2) Recursive check
            - Recursively check the left subtrees
            - Recursively check the right subtrees
        3) If both left and right subtrees are the same, return true false otherwise
        '''
        # If both are None, they are the same tree
        if not p and not q:
            return True
        
        # If one is None and the other is not, they are different
        if not p or not q:
            return False
        
        # If values are different that means the trees are different
        if p.val != q.val:
            return False
        
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#Time Complexity: O(n)
#Space Complexity: O(h) where h is the height of the tree