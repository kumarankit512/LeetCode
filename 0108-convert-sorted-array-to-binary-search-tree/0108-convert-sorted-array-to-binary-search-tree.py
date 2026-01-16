# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        '''
        Procedure:
        1) Base case
            -> If the array (or subarray) is empty, return None
        2) Find the middle element
            -> Compute mid = (left + right) // 2
            -> This element becomes the root of the current subtree
        3) Create the Root Node
            -> Create a TreeNode with value nums[mid]
        4) Build the Left Subtree
            -> Recursively apply the same logic to the left half:
                -> left to mid - 1
        5) Build the Right Subtree
            -> Recursively apply the same logic to the right half:
                -> mid + 1 to right
        6) Return the Root
            -> The recursive calls connect the entire tree
        '''

        def build(left: int, right: int) -> Optional[TreeNode]:

            if left > right:
                return None

            # Find the middle element
            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            # Recursively build left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)

        #Time Complexity: O(n)
        #Space Complexity: O(log n) -> Due to the recursion stack for a height-balanced BST