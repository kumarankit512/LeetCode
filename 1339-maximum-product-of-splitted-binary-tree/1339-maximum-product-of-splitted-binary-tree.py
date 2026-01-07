# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        '''
        DFS Solution

        Procedure:
        1) Compute the total tree sum
            - Use DFS to sum all nodes in the tree
        2) Use DFS again to compute subtree sums for each node
            - Compute the sum of the subtree rooted at that node
            - Treat this subtree as one side of a possible split
            - Compute the product
        3) Return the Maximum Product (mod 10^9 + 7)
        '''

        MOD = 10**9 + 7
        self.max_product = 0

        # Get total sum of tree
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)

        total = totalSum(root)

        #DFS function to compute subtree sums and products
        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            subtree_sum = node.val + left_sum + right_sum

            # Compute product by splitting here
            self.max_product = max(
                self.max_product,
                subtree_sum * (total - subtree_sum)
            )

            return subtree_sum

        dfs(root)

        return self.max_product % MOD

        #Time Complexity: O(n)
        #Space Complexity: O(n)