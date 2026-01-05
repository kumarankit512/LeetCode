class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        '''
        Greedy Approach

        Given an n x n matrix, perform the following operation any number of times: Pick two adjacent cells and multiply both by -1 to maximize the sum of all elements in the matrix.

        If the number of negative values is even
            - You can make all numbers positive
        If the number of negative values is odd
            - One number must remain negative
            - To minimize loss, keep the smallest absolute value negative
        
        Procedure:
        1) Traverse through the matrix
            - Add its absolute value to the total
            - Count how many numbers are negative
            - Track the minimum absolute value
        2) Check for negative count
            - If the number of negatives is even
                - Maximum sum = sum of absolute values
            - If the number of negatives is odd
                - One value must stay negative
                - Subtract 2 x minimum absolute value from the total
        
        For Example:
        Input -> matrix = [[1, -1], [-1, 1]]
        Absolute sum = 1 + 1 + 1 + 1 = 4
        Negative count = 2 (even)
        Maximum sum = 4
        '''

        total_sum = 0
        negative_count = 0
        min_abs = float('inf')

        for row in matrix:
            for val in row:
                total_sum += abs(val)
                if val < 0:
                    negative_count += 1
                min_abs = min(min_abs, abs(val))

        # If there are odd number of negative elements, subtract twice the smallest absolute value
        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs

        return total_sum

        #Time Complexity: O(n^2) - must visit every cell in the matrix
        #Space Complexity: O(1)