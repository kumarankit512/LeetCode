# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        '''
        BFS Approach

        Procedure:
        1) Use a queue
            - Initialize a queue with the root node
            - This allows us to traverse the tree level by level
        2) Keep track of the key variables
            - 'level' -> current level number (start at 1)
            - 'max_sum' -> maximum level sum found so far 
            - 'answer_level' -> level that produced max_sum
        3) Check each level
            - Get the number of nodes at this level (level_size)
            - Initialize level_sum = 0
            - Process all nodes in this level
                - Add their values to level_sum
                - Push their children into the queue
        4) Update result
            - If level_sum > max_sum, update:
                - max_sum = level_sum
                - answer_level = level
        5) Increment to the next level
            - Continue until the queue is empty
        '''

        queue = deque([root])
        
        max_sum = float('-inf')
        answer_level = 1
        level = 1
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                answer_level = level
            
            level += 1
        
        return answer_level

        #Time Complexity: O(n)
        #Space Complexity: O(n)