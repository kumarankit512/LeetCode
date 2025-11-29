# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Procedure:
        1) Start from the root
        2) Recursively traverse the left subtree
        3) Visit the current node (add value to the result list)
        4) Recursively traverse the right subtree
        5) If node is NULL, do nothing
        '''

        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            node = stack.pop()
            result.append(node.val)
            current = node.right

        return result

#Time Complexity: O(n)
#Space Complexity: O(n)